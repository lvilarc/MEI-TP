#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <string.h>

/*
    Minimal JWT implementation using HS256.

    This is educational code:
    - No external libraries
    - Manual Base64URL encoding
    - Manual SHA-256
    - Manual HMAC-SHA256

    Not intended for production security use.
*/

/* =========================
   SHA-256 IMPLEMENTATION
   ========================= */

#define ROTRIGHT(a, b) (((a) >> (b)) | ((a) << (32 - (b))))

#define CH(x, y, z)  (((x) & (y)) ^ (~(x) & (z)))
#define MAJ(x, y, z) (((x) & (y)) ^ ((x) & (z)) ^ ((y) & (z)))

#define EP0(x) (ROTRIGHT(x, 2) ^ ROTRIGHT(x, 13) ^ ROTRIGHT(x, 22))
#define EP1(x) (ROTRIGHT(x, 6) ^ ROTRIGHT(x, 11) ^ ROTRIGHT(x, 25))

#define SIG0(x) (ROTRIGHT(x, 7) ^ ROTRIGHT(x, 18) ^ ((x) >> 3))
#define SIG1(x) (ROTRIGHT(x, 17) ^ ROTRIGHT(x, 19) ^ ((x) >> 10))

static const uint32_t k[64] = {
    0x428a2f98, 0x71374491, 0xb5c0fbcf, 0xe9b5dba5,
    0x3956c25b, 0x59f111f1, 0x923f82a4, 0xab1c5ed5,
    0xd807aa98, 0x12835b01, 0x243185be, 0x550c7dc3,
    0x72be5d74, 0x80deb1fe, 0x9bdc06a7, 0xc19bf174,
    0xe49b69c1, 0xefbe4786, 0x0fc19dc6, 0x240ca1cc,
    0x2de92c6f, 0x4a7484aa, 0x5cb0a9dc, 0x76f988da,
    0x983e5152, 0xa831c66d, 0xb00327c8, 0xbf597fc7,
    0xc6e00bf3, 0xd5a79147, 0x06ca6351, 0x14292967,
    0x27b70a85, 0x2e1b2138, 0x4d2c6dfc, 0x53380d13,
    0x650a7354, 0x766a0abb, 0x81c2c92e, 0x92722c85,
    0xa2bfe8a1, 0xa81a664b, 0xc24b8b70, 0xc76c51a3,
    0xd192e819, 0xd6990624, 0xf40e3585, 0x106aa070,
    0x19a4c116, 0x1e376c08, 0x2748774c, 0x34b0bcb5,
    0x391c0cb3, 0x4ed8aa4a, 0x5b9cca4f, 0x682e6ff3,
    0x748f82ee, 0x78a5636f, 0x84c87814, 0x8cc70208,
    0x90befffa, 0xa4506ceb, 0xbef9a3f7, 0xc67178f2
};

void sha256(const uint8_t *data, size_t len, uint8_t hash[32]) {
    uint32_t h[8] = {
        0x6a09e667,
        0xbb67ae85,
        0x3c6ef372,
        0xa54ff53a,
        0x510e527f,
        0x9b05688c,
        0x1f83d9ab,
        0x5be0cd19
    };

    size_t new_len = len + 1;

    while (new_len % 64 != 56) {
        new_len++;
    }

    uint8_t *msg = calloc(new_len + 8, 1);
    if (!msg) {
        fprintf(stderr, "Memory allocation failed\n");
        exit(1);
    }

    memcpy(msg, data, len);
    msg[len] = 0x80;

    uint64_t bit_len = (uint64_t)len * 8;

    for (int i = 0; i < 8; i++) {
        msg[new_len + i] = (uint8_t)(bit_len >> (56 - 8 * i));
    }

    for (size_t offset = 0; offset < new_len + 8; offset += 64) {
        uint32_t w[64];

        for (int i = 0; i < 16; i++) {
            w[i] =
                ((uint32_t)msg[offset + i * 4] << 24) |
                ((uint32_t)msg[offset + i * 4 + 1] << 16) |
                ((uint32_t)msg[offset + i * 4 + 2] << 8) |
                ((uint32_t)msg[offset + i * 4 + 3]);
        }

        for (int i = 16; i < 64; i++) {
            w[i] = SIG1(w[i - 2]) + w[i - 7] + SIG0(w[i - 15]) + w[i - 16];
        }

        uint32_t a = h[0];
        uint32_t b = h[1];
        uint32_t c = h[2];
        uint32_t d = h[3];
        uint32_t e = h[4];
        uint32_t f = h[5];
        uint32_t g = h[6];
        uint32_t hh = h[7];

        for (int i = 0; i < 64; i++) {
            uint32_t t1 = hh + EP1(e) + CH(e, f, g) + k[i] + w[i];
            uint32_t t2 = EP0(a) + MAJ(a, b, c);

            hh = g;
            g = f;
            f = e;
            e = d + t1;
            d = c;
            c = b;
            b = a;
            a = t1 + t2;
        }

        h[0] += a;
        h[1] += b;
        h[2] += c;
        h[3] += d;
        h[4] += e;
        h[5] += f;
        h[6] += g;
        h[7] += hh;
    }

    free(msg);

    for (int i = 0; i < 8; i++) {
        hash[i * 4]     = (uint8_t)(h[i] >> 24);
        hash[i * 4 + 1] = (uint8_t)(h[i] >> 16);
        hash[i * 4 + 2] = (uint8_t)(h[i] >> 8);
        hash[i * 4 + 3] = (uint8_t)(h[i]);
    }
}

/* =========================
   HMAC-SHA256 IMPLEMENTATION
   ========================= */

void hmac_sha256(
    const uint8_t *key,
    size_t key_len,
    const uint8_t *data,
    size_t data_len,
    uint8_t output[32]
) {
    uint8_t key_block[64];
    uint8_t inner_hash[32];
    uint8_t o_key_pad[64];
    uint8_t i_key_pad[64];

    memset(key_block, 0, sizeof(key_block));

    if (key_len > 64) {
        sha256(key, key_len, key_block);
    } else {
        memcpy(key_block, key, key_len);
    }

    for (int i = 0; i < 64; i++) {
        i_key_pad[i] = key_block[i] ^ 0x36;
        o_key_pad[i] = key_block[i] ^ 0x5c;
    }

    uint8_t *inner_data = malloc(64 + data_len);
    if (!inner_data) {
        fprintf(stderr, "Memory allocation failed\n");
        exit(1);
    }

    memcpy(inner_data, i_key_pad, 64);
    memcpy(inner_data + 64, data, data_len);

    sha256(inner_data, 64 + data_len, inner_hash);
    free(inner_data);

    uint8_t outer_data[64 + 32];

    memcpy(outer_data, o_key_pad, 64);
    memcpy(outer_data + 64, inner_hash, 32);

    sha256(outer_data, sizeof(outer_data), output);
}

/* =========================
   BASE64URL ENCODING
   ========================= */

char *base64url_encode(const uint8_t *data, size_t len) {
    static const char table[] =
        "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        "abcdefghijklmnopqrstuvwxyz"
        "0123456789-_";

    size_t out_len = 4 * ((len + 2) / 3);

    if (len % 3 == 1) {
        out_len -= 2;
    } else if (len % 3 == 2) {
        out_len -= 1;
    }

    char *out = malloc(out_len + 1);
    if (!out) {
        fprintf(stderr, "Memory allocation failed\n");
        exit(1);
    }

    size_t i = 0;
    size_t j = 0;

    while (i < len) {
        size_t remaining = len - i;

        uint32_t octet_a = data[i++];
        uint32_t octet_b = remaining > 1 ? data[i++] : 0;
        uint32_t octet_c = remaining > 2 ? data[i++] : 0;

        uint32_t triple = (octet_a << 16) | (octet_b << 8) | octet_c;

        out[j++] = table[(triple >> 18) & 0x3f];
        out[j++] = table[(triple >> 12) & 0x3f];

        if (remaining > 1) {
            out[j++] = table[(triple >> 6) & 0x3f];
        }

        if (remaining > 2) {
            out[j++] = table[triple & 0x3f];
        }
    }

    out[j] = '\0';

    return out;
}

/* =========================
   JWT CREATION
   ========================= */

char *create_jwt(const char *header, const char *payload, const char *secret) {
    char *encoded_header = base64url_encode(
        (const uint8_t *)header,
        strlen(header)
    );

    char *encoded_payload = base64url_encode(
        (const uint8_t *)payload,
        strlen(payload)
    );

    size_t signing_input_len =
        strlen(encoded_header) + 1 + strlen(encoded_payload);

    char *signing_input = malloc(signing_input_len + 1);
    if (!signing_input) {
        fprintf(stderr, "Memory allocation failed\n");
        exit(1);
    }

    snprintf(
        signing_input,
        signing_input_len + 1,
        "%s.%s",
        encoded_header,
        encoded_payload
    );

    uint8_t signature[32];

    hmac_sha256(
        (const uint8_t *)secret,
        strlen(secret),
        (const uint8_t *)signing_input,
        strlen(signing_input),
        signature
    );

    char *encoded_signature = base64url_encode(signature, 32);

    size_t token_len =
        strlen(signing_input) + 1 + strlen(encoded_signature);

    char *token = malloc(token_len + 1);
    if (!token) {
        fprintf(stderr, "Memory allocation failed\n");
        exit(1);
    }

    snprintf(
        token,
        token_len + 1,
        "%s.%s",
        signing_input,
        encoded_signature
    );

    free(encoded_header);
    free(encoded_payload);
    free(signing_input);
    free(encoded_signature);

    return token;
}

/* =========================
   JWT VERIFICATION
   ========================= */

int constant_time_string_equal(const char *a, const char *b) {
    size_t len_a = strlen(a);
    size_t len_b = strlen(b);

    size_t max_len = len_a > len_b ? len_a : len_b;

    unsigned char diff = (unsigned char)(len_a ^ len_b);

    for (size_t i = 0; i < max_len; i++) {
        unsigned char ca = i < len_a ? (unsigned char)a[i] : 0;
        unsigned char cb = i < len_b ? (unsigned char)b[i] : 0;

        diff |= ca ^ cb;
    }

    return diff == 0;
}

int verify_jwt(const char *token, const char *secret) {
    const char *dot1 = strchr(token, '.');

    if (!dot1) {
        return 0;
    }

    const char *dot2 = strchr(dot1 + 1, '.');

    if (!dot2) {
        return 0;
    }

    if (strchr(dot2 + 1, '.')) {
        return 0;
    }

    size_t signing_input_len = (size_t)(dot2 - token);

    char *signing_input = malloc(signing_input_len + 1);
    if (!signing_input) {
        fprintf(stderr, "Memory allocation failed\n");
        exit(1);
    }

    memcpy(signing_input, token, signing_input_len);
    signing_input[signing_input_len] = '\0';

    const char *provided_signature = dot2 + 1;

    uint8_t expected_signature_raw[32];

    hmac_sha256(
        (const uint8_t *)secret,
        strlen(secret),
        (const uint8_t *)signing_input,
        signing_input_len,
        expected_signature_raw
    );

    char *expected_signature =
        base64url_encode(expected_signature_raw, 32);

    int valid = constant_time_string_equal(
        provided_signature,
        expected_signature
    );

    free(signing_input);
    free(expected_signature);

    return valid;
}

/* =========================
   DEMO
   ========================= */

int main(void) {
    const char *header =
        "{\"alg\":\"HS256\",\"typ\":\"JWT\"}";

    const char *payload =
        "{\"sub\":\"1234567890\",\"name\":\"John Doe\",\"admin\":true}";

    const char *secret =
        "my-secret-key";

    char *token = create_jwt(header, payload, secret);

    printf("Generated JWT:\n%s\n\n", token);

    int valid = verify_jwt(token, secret);

    printf("Verification result: %s\n", valid ? "valid" : "invalid");

    const char *wrong_secret = "wrong-secret-key";

    int valid_with_wrong_secret = verify_jwt(token, wrong_secret);

    printf(
        "Verification with wrong secret: %s\n",
        valid_with_wrong_secret ? "valid" : "invalid"
    );

    free(token);

    return 0;
}
