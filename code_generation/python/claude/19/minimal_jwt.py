#!/usr/bin/env python3
"""
Minimal JWT (JSON Web Token) implementation using only Python's standard library.
Implements: Base64URL encoding and HMAC-SHA256 — both from scratch.
"""

import struct
import hashlib  # Used only for SHA-256 block; HMAC is built manually


# ─────────────────────────────────────────────
#  SHA-256 — Manual Implementation
# ─────────────────────────────────────────────

def _rotr(x, n):
    return ((x >> n) | (x << (32 - n))) & 0xFFFFFFFF

def sha256(message: bytes) -> bytes:
    """Pure-Python SHA-256."""
    # Initial hash values (first 32 bits of fractional parts of sqrt of first 8 primes)
    h0 = 0x6a09e667; h1 = 0xbb67ae85; h2 = 0x3c6ef372; h3 = 0xa54ff53a
    h4 = 0x510e527f; h5 = 0x9b05688c; h6 = 0x1f83d9ab; h7 = 0x5be0cd19

    # Round constants (first 32 bits of fractional parts of cbrt of first 64 primes)
    K = [
        0x428a2f98,0x71374491,0xb5c0fbcf,0xe9b5dba5,0x3956c25b,0x59f111f1,0x923f82a4,0xab1c5ed5,
        0xd807aa98,0x12835b01,0x243185be,0x550c7dc3,0x72be5d74,0x80deb1fe,0x9bdc06a7,0xc19bf174,
        0xe49b69c1,0xefbe4786,0x0fc19dc6,0x240ca1cc,0x2de92c6f,0x4a7484aa,0x5cb0a9dc,0x76f988da,
        0x983e5152,0xa831c66d,0xb00327c8,0xbf597fc7,0xc6e00bf3,0xd5a79147,0x06ca6351,0x14292967,
        0x27b70a85,0x2e1b2138,0x4d2c6dfc,0x53380d13,0x650a7354,0x766a0abb,0x81c2c92e,0x92722c85,
        0xa2bfe8a1,0xa81a664b,0xc24b8b70,0xc76c51a3,0xd192e819,0xd6990624,0xf40e3585,0x106aa070,
        0x19a4c116,0x1e376c08,0x2748774c,0x34b0bcb5,0x391c0cb3,0x4ed8aa4a,0x5b9cca4f,0x682e6ff3,
        0x748f82ee,0x78a5636f,0x84c87814,0x8cc70208,0x90befffa,0xa4506ceb,0xbef9a3f7,0xc67178f2,
    ]

    # Pre-processing: padding
    msg = bytearray(message)
    orig_len_bits = len(message) * 8
    msg.append(0x80)
    while len(msg) % 64 != 56:
        msg.append(0x00)
    msg += struct.pack('>Q', orig_len_bits)

    # Process each 512-bit (64-byte) chunk
    for i in range(0, len(msg), 64):
        chunk = msg[i:i+64]
        w = list(struct.unpack('>16I', chunk)) + [0] * 48
        for j in range(16, 64):
            s0 = _rotr(w[j-15], 7) ^ _rotr(w[j-15], 18) ^ (w[j-15] >> 3)
            s1 = _rotr(w[j-2], 17) ^ _rotr(w[j-2], 19) ^ (w[j-2] >> 10)
            w[j] = (w[j-16] + s0 + w[j-7] + s1) & 0xFFFFFFFF

        a,b,c,d,e,f,g,h = h0,h1,h2,h3,h4,h5,h6,h7

        for j in range(64):
            S1   = _rotr(e,6) ^ _rotr(e,11) ^ _rotr(e,25)
            ch   = (e & f) ^ ((~e) & g)
            temp1 = (h + S1 + ch + K[j] + w[j]) & 0xFFFFFFFF
            S0   = _rotr(a,2) ^ _rotr(a,13) ^ _rotr(a,22)
            maj  = (a & b) ^ (a & c) ^ (b & c)
            temp2 = (S0 + maj) & 0xFFFFFFFF

            h=g; g=f; f=e; e=(d+temp1)&0xFFFFFFFF
            d=c; c=b; b=a; a=(temp1+temp2)&0xFFFFFFFF

        h0=(h0+a)&0xFFFFFFFF; h1=(h1+b)&0xFFFFFFFF
        h2=(h2+c)&0xFFFFFFFF; h3=(h3+d)&0xFFFFFFFF
        h4=(h4+e)&0xFFFFFFFF; h5=(h5+f)&0xFFFFFFFF
        h6=(h6+g)&0xFFFFFFFF; h7=(h7+h)&0xFFFFFFFF

    return struct.pack('>8I', h0,h1,h2,h3,h4,h5,h6,h7)


# ─────────────────────────────────────────────
#  HMAC-SHA256 — Manual Implementation
# ─────────────────────────────────────────────

def hmac_sha256(key: bytes, message: bytes) -> bytes:
    """HMAC using our manual SHA-256 (RFC 2104)."""
    BLOCK_SIZE = 64

    # Keys longer than block size are hashed
    if len(key) > BLOCK_SIZE:
        key = sha256(key)
    # Keys shorter than block size are zero-padded
    key = key.ljust(BLOCK_SIZE, b'\x00')

    opad = bytes(b ^ 0x5C for b in key)  # outer padding
    ipad = bytes(b ^ 0x36 for b in key)  # inner padding

    inner = sha256(ipad + message)
    return sha256(opad + inner)


# ─────────────────────────────────────────────
#  Base64URL — Manual Implementation
# ─────────────────────────────────────────────

_B64_CHARS = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"

def base64url_encode(data: bytes) -> str:
    """Standard Base64 encoding, then URL-safe swap, no padding."""
    result = []
    # Process every 3-byte group
    for i in range(0, len(data), 3):
        group = data[i:i+3]
        b = int.from_bytes(group.ljust(3, b'\x00'), 'big')
        # Extract four 6-bit indices
        result.append(_B64_CHARS[(b >> 18) & 0x3F])
        result.append(_B64_CHARS[(b >> 12) & 0x3F])
        if len(group) >= 2:
            result.append(_B64_CHARS[(b >> 6) & 0x3F])
        if len(group) == 3:
            result.append(_B64_CHARS[b & 0x3F])

    b64 = "".join(result)
    # URL-safe: replace + with -, / with _, strip = padding
    return b64.replace("+", "-").replace("/", "_")


def base64url_decode(s: str) -> bytes:
    """Decode a Base64URL string back to bytes."""
    # Restore standard Base64 characters
    s = s.replace("-", "+").replace("_", "/")
    # Re-add padding if needed
    pad = (4 - len(s) % 4) % 4
    s += "=" * pad

    # Decode character by character
    lookup = {c: i for i, c in enumerate(_B64_CHARS)}
    lookup["="] = 0  # padding is treated as 0

    result = []
    for i in range(0, len(s), 4):
        group = s[i:i+4]
        b = (lookup[group[0]] << 18 | lookup[group[1]] << 12 |
             lookup[group[2]] << 6  | lookup[group[3]])
        result.append((b >> 16) & 0xFF)
        if group[2] != "=":
            result.append((b >> 8) & 0xFF)
        if group[3] != "=":
            result.append(b & 0xFF)

    return bytes(result)


# ─────────────────────────────────────────────
#  JWT Create & Verify
# ─────────────────────────────────────────────

def create_jwt(header: str, payload: str, secret: str) -> str:
    """
    Create a JWT token.
    header and payload are JSON strings.
    Returns: base64url(header).base64url(payload).base64url(signature)
    """
    encoded_header  = base64url_encode(header.encode("utf-8"))
    encoded_payload = base64url_encode(payload.encode("utf-8"))

    signing_input = f"{encoded_header}.{encoded_payload}"
    signature = hmac_sha256(secret.encode("utf-8"), signing_input.encode("utf-8"))
    encoded_signature = base64url_encode(signature)

    return f"{signing_input}.{encoded_signature}"


def verify_jwt(token: str, secret: str) -> bool:
    """
    Verify a JWT token by recomputing the signature.
    Returns True if valid, False otherwise.
    """
    parts = token.split(".")
    if len(parts) != 3:
        print("[ERROR] Token does not have exactly 3 parts.")
        return False

    header_b64, payload_b64, provided_sig_b64 = parts

    # Recompute signature over header.payload
    signing_input = f"{header_b64}.{payload_b64}"
    expected_sig = hmac_sha256(secret.encode("utf-8"), signing_input.encode("utf-8"))
    expected_sig_b64 = base64url_encode(expected_sig)

    # Constant-time comparison to prevent timing attacks
    if len(provided_sig_b64) != len(expected_sig_b64):
        return False
    result = 0
    for a, b in zip(provided_sig_b64, expected_sig_b64):
        result |= ord(a) ^ ord(b)
    return result == 0


# ─────────────────────────────────────────────
#  Demonstration
# ─────────────────────────────────────────────

if __name__ == "__main__":
    SECRET = "my-super-secret-key"

    HEADER  = '{"alg":"HS256","typ":"JWT"}'
    PAYLOAD = '{"sub":"1234567890","name":"Miguel","iat":1718900000}'

    print("=" * 60)
    print("  Minimal JWT System — HS256 (no external libraries)")
    print("=" * 60)
    print()
    print(f"Header  : {HEADER}")
    print(f"Payload : {PAYLOAD}")
    print(f"Secret  : {SECRET}")
    print()

    token = create_jwt(HEADER, PAYLOAD, SECRET)
    print(f"Generated Token:")
    print(f"  {token}")
    print()

    # Show the three parts clearly
    parts = token.split(".")
    print(f"Token Parts:")
    print(f"  [1] Header    : {parts[0]}")
    print(f"  [2] Payload   : {parts[1]}")
    print(f"  [3] Signature : {parts[2]}")
    print()

    # Verify the valid token
    is_valid = verify_jwt(token, SECRET)
    print(f"Verification with correct secret  : {'✓ VALID' if is_valid else '✗ INVALID'}")

    # Tamper with the secret
    is_valid_wrong = verify_jwt(token, "wrong-secret")
    print(f"Verification with wrong secret    : {'✓ VALID' if is_valid_wrong else '✗ INVALID'}")

    # Tamper with the payload
    tampered = token[:-5] + "XXXXX"
    is_valid_tampered = verify_jwt(tampered, SECRET)
    print(f"Verification of tampered token    : {'✓ VALID' if is_valid_tampered else '✗ INVALID'}")

    # Cross-check our SHA-256 against Python's hashlib
    import hashlib, hmac as hmac_lib
    ref_sig = hmac_lib.new(SECRET.encode(), f"{parts[0]}.{parts[1]}".encode(), hashlib.sha256).digest()
    ref_b64 = base64url_encode(ref_sig)
    print()
    print(f"Cross-check vs. stdlib HMAC-SHA256:")
    print(f"  Our signature : {parts[2]}")
    print(f"  stdlib sig    : {ref_b64}")
    print(f"  Match         : {'✓ YES' if parts[2] == ref_b64 else '✗ NO'}")
    print()
    print("=" * 60)
