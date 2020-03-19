import ecdsa
import base58
import ecdsa
import random

from eth_hash.auto import keccak as keccak_256


def get_signing_key(raw_priv):
    return ecdsa.SigningKey.from_string(raw_priv, curve=ecdsa.SECP256k1)


def verifying_key_to_addr(key):
    pub_key = key.to_string()
    primitive_addr = b'\x41' + keccak_256(pub_key)[-20:]
    addr = base58.b58encode_check(primitive_addr)
    return addr


while True:
    raw = bytes(random.sample(range(0, 256), 32))
    key = get_signing_key(raw)
    addr = verifying_key_to_addr(key.get_verifying_key()).decode()
    # 0 (zero), O (capital o), I (capital i) and l (lower case L)
    if addr.lower().endswith('mono'):
        print(addr)
        print('    :', raw.hex())
        raise SystemExit
