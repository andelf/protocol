import ecdsa
import base58
import ecdsa

from eth_hash.auto import keccak as keccak_256


def get_signing_key(raw_priv):
    return ecdsa.SigningKey.from_string(raw_priv, curve=ecdsa.SECP256k1)


def verifying_key_to_addr(key):
    pub_key = key.to_string()
    primitive_addr = b'\x41' + keccak_256(pub_key)[-20:]
    addr = base58.b58encode_check(primitive_addr)
    return addr


for i in range(1, 16-1):
    raw = hex(i)[-1] * 64
    # print(raw)
    key = get_signing_key(bytes.fromhex(raw))
    print(verifying_key_to_addr(key.get_verifying_key()).decode())
