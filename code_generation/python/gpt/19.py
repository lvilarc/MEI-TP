# Minimal JWT implementation using:
# - Manual Base64URL encoding
# - Manual SHA-256
# - Manual HMAC-SHA256
#
# Educational example only. Do not use this in production.

BASE64URL_ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789-_"


def base64url_encode(data: bytes) -> str:
    """
    Manually encode bytes using Base64URL without padding.
    """
    result = []

    for i in range(0, len(data), 3):
        chunk = data[i:i + 3]

        # Pad chunk to 3 bytes for processing
        padding_needed = 3 - len(chunk)
        chunk += b"\x00" * padding_needed

        # Convert 3 bytes into a 24-bit integer
        value = (chunk[0] << 16) | (chunk[1] << 8) | chunk[2]

        # Split into four 6-bit values
        indexes = [
            (value >> 18) & 0x3F,
            (value >> 12) & 0x3F,
            (value >> 6) & 0x3F,
            value & 0x3F,
        ]

        # Convert indexes to Base64URL characters
        chars = [BASE64URL_ALPHABET[index] for index in indexes]

        # Remove characters that would have been padding
        if padding_needed:
            chars = chars[:-padding_needed]

        result.extend(chars)

    return "".join(result)


def right_rotate(value: int, bits: int) -> int:
    return ((value >> bits) | (value << (32 - bits))) & 0xFFFFFFFF


def sha256(data: bytes) -> bytes:
    """
    Manual SHA-256 implementation.
    Returns the 32-byte digest.
    """

    # Initial hash values
    h = [
        0x6A09E667,
        0xBB67AE85,
        0x3C6EF372,
        0xA54FF53A,
        0x510E527F,
        0x9B05688C,
        0x1F83D9AB,
        0x5BE0CD19,
    ]

    # SHA-256 round constants
    k = [
        0x428A2F98, 0x71374491, 0xB5C0FBCF, 0xE9B5DBA5,
        0x3956C25B, 0x59F111F1, 0x923F82A4, 0xAB1C5ED5,
        0xD807AA98, 0x12835B01, 0x243185BE, 0x550C7DC3,
        0x72BE5D74, 0x80DEB1FE, 0x9BDC06A7, 0xC19BF174,
        0xE49B69C1, 0xEFBE4786, 0x0FC19DC6, 0x240CA1CC,
        0x2DE92C6F, 0x4A7484AA, 0x5CB0A9DC, 0x76F988DA,
        0x983E5152, 0xA831C66D, 0xB00327C8, 0xBF597FC7,
        0xC6E00BF3, 0xD5A79147, 0x06CA6351, 0x14292967,
        0x27B70A85, 0x2E1B2138, 0x4D2C6DFC, 0x53380D13,
        0x650A7354, 0x766A0ABB, 0x81C2C92E, 0x92722C85,
        0xA2BFE8A1, 0xA81A664B, 0xC24B8B70, 0xC76C51A3,
        0xD192E819, 0xD6990624, 0xF40E3585, 0x106AA070,
        0x19A4C116, 0x1E376C08, 0x2748774C, 0x34B0BCB5,
        0x391C0CB3, 0x4ED8AA4A, 0x5B9CCA4F, 0x682E6FF3,
        0x748F82EE, 0x78A5636F, 0x84C87814, 0x8CC70208,
        0x90BEFFFA, 0xA4506CEB, 0xBEF9A3F7, 0xC67178F2,
    ]

    original_bit_length = len(data) * 8

    # Padding
    data += b"\x80"

    while len(data) % 64 != 56:
        data += b"\x00"

    data += original_bit_length.to_bytes(8, byteorder="big")

    # Process 512-bit chunks
    for chunk_start in range(0, len(data), 64):
        chunk = data[chunk_start:chunk_start + 64]

        # Message schedule
        w = []

        for i in range(16):
            word = int.from_bytes(chunk[i * 4:i * 4 + 4], byteorder="big")
            w.append(word)

        for i in range(16, 64):
            s0 = (
                right_rotate(w[i - 15], 7)
                ^ right_rotate(w[i - 15], 18)
                ^ (w[i - 15] >> 3)
            )

            s1 = (
                right_rotate(w[i - 2], 17)
                ^ right_rotate(w[i - 2], 19)
                ^ (w[i - 2] >> 10)
            )

            word = (w[i - 16] + s0 + w[i - 7] + s1) & 0xFFFFFFFF
            w.append(word)

        a, b, c, d, e, f, g, current_h = h

        # Compression loop
        for i in range(64):
            big_sigma_1 = (
                right_rotate(e, 6)
                ^ right_rotate(e, 11)
                ^ right_rotate(e, 25)
            )

            choose = (e & f) ^ ((~e) & g)

            temp1 = (
                current_h
                + big_sigma_1
                + choose
                + k[i]
                + w[i]
            ) & 0xFFFFFFFF

            big_sigma_0 = (
                right_rotate(a, 2)
                ^ right_rotate(a, 13)
                ^ right_rotate(a, 22)
            )

            majority = (a & b) ^ (a & c) ^ (b & c)

            temp2 = (big_sigma_0 + majority) & 0xFFFFFFFF

            current_h = g
            g = f
            f = e
            e = (d + temp1) & 0xFFFFFFFF
            d = c
            c = b
            b = a
            a = (temp1 + temp2) & 0xFFFFFFFF

        h = [
            (h[0] + a) & 0xFFFFFFFF,
            (h[1] + b) & 0xFFFFFFFF,
            (h[2] + c) & 0xFFFFFFFF,
            (h[3] + d) & 0xFFFFFFFF,
            (h[4] + e) & 0xFFFFFFFF,
            (h[5] + f) & 0xFFFFFFFF,
            (h[6] + g) & 0xFFFFFFFF,
            (h[7] + current_h) & 0xFFFFFFFF,
        ]

    digest = b""

    for value in h:
        digest += value.to_bytes(4, byteorder="big")

    return digest


def hmac_sha256(key: bytes, message: bytes) -> bytes:
    """
    Manual HMAC-SHA256 implementation.
    """

    block_size = 64

    if len(key) > block_size:
        key = sha256(key)

    if len(key) < block_size:
        key += b"\x00" * (block_size - len(key))

    outer_key_pad = bytes(byte ^ 0x5C for byte in key)
    inner_key_pad = bytes(byte ^ 0x36 for byte in key)

    inner_hash = sha256(inner_key_pad + message)
    final_hash = sha256(outer_key_pad + inner_hash)

    return final_hash


def constant_time_compare(a: str, b: str) -> bool:
    """
    Compare two strings without returning early on the first mismatch.
    """

    if len(a) != len(b):
        return False

    result = 0

    for x, y in zip(a.encode("utf-8"), b.encode("utf-8")):
        result |= x ^ y

    return result == 0


def create_jwt(header: str, payload: str, secret: str) -> str:
    encoded_header = base64url_encode(header.encode("utf-8"))
    encoded_payload = base64url_encode(payload.encode("utf-8"))

    signing_input = f"{encoded_header}.{encoded_payload}".encode("utf-8")

    signature = hmac_sha256(secret.encode("utf-8"), signing_input)
    encoded_signature = base64url_encode(signature)

    return f"{encoded_header}.{encoded_payload}.{encoded_signature}"


def verify_jwt(token: str, secret: str) -> bool:
    parts = token.split(".")

    if len(parts) != 3:
        return False

    encoded_header, encoded_payload, encoded_signature = parts

    signing_input = f"{encoded_header}.{encoded_payload}".encode("utf-8")

    expected_signature = hmac_sha256(secret.encode("utf-8"), signing_input)
    expected_encoded_signature = base64url_encode(expected_signature)

    return constant_time_compare(encoded_signature, expected_encoded_signature)


if __name__ == "__main__":
    header = '{"alg":"HS256","typ":"JWT"}'
    payload = '{"sub":"1234567890","name":"Miguel","admin":true}'
    secret = "my-secret-key"

    token = create_jwt(header, payload, secret)

    print("Generated JWT:")
    print(token)

    print()
    print("Verification result:")
    print(verify_jwt(token, secret))

    print()
    print("Verification with wrong secret:")
    print(verify_jwt(token, "wrong-secret"))