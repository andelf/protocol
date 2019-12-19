import hashlib

import base58
import ecdsa
from eth_hash.auto import keccak as keccak_256

# secp256k1
# 32bytes, 256bits

# key = ecdsa.SigningKey.from_string(bytes.fromhex('1' * 64), curve=ecdsa.SECP256k1)
# x = key.privkey.public_key.point.x()
# y = key.privkey.public_key.point.y()

# '%064s' % hex(x)[2:] + '%064s' % hex(y)[2:]

# generate address
priv_key = ecdsa.SigningKey.generate(curve=ecdsa.SECP256k1)
pub_key = priv_key.get_verifying_key().to_string()
primitive_addr = b'\x41' + keccak_256(pub_key)[-20:]
addr = base58.b58encode_check(primitive_addr)

print(addr)

# address from priv_key
priv_key = ecdsa.SigningKey.from_string(
    bytes.fromhex('d705fc17c82942f85848ab522e42d986279028d09d12ad881bdc0e1327031976'), curve=ecdsa.SECP256k1
)
pub_key = priv_key.get_verifying_key().to_string()
primitive_addr = b'\x41' + keccak_256(pub_key)[-20:]
addr = base58.b58encode_check(primitive_addr)

print(addr)
print(primitive_addr.hex())

class Address(object):
    @classmethod
    def from_priv_key(cls, key):
        pass


"""
TRX_MESSAGE_HEADER = b'\x19TRON Signed Message:\n'
header = TRX_MESSAGE_HEADER + str(len(raw_data)).encode()

raw_data_hash = keccak_256(header + raw_data)
sign = priv_key.sign( hashlib.sha256(raw_data_hash).digest())

print(sign.hex())

"""
print('-' * 80)

tx_id = bytes.fromhex('1275ac815e624f3a0e59c5d598f19ee2d5a50dd1736e37659e6b0c40f19cdeec')

# sign transaction
raw_data = bytes.fromhex('0a02d33222081a2ce1f1010d5fe540d0f685e8f12d5a68080112640a2d747970652e676f6f676c65617069732e636f6d2f70726f746f636f6c2e5472616e73666572436f6e747261637412330a15419cf784b4cc7531f1598c4c322de9afdc597fe760121541340967e825557559dc46bbf0eabe5ccf99fd134e18c0e7fb0a70ccaf82e8f12d')
sign = priv_key.sign_deterministic(raw_data, hashfunc=hashlib.sha256)

print('sign', sign.hex())

print('orig', 'dc2c6b3f97f64e043a3dfe37d7686dbb1ab21e3271b372c6de1c6ba0a4ff609b8e62254629ce9027d247c3eca49bf481f3bc8eee7bcca4dc1a28c6b158519c0300')

# r, s, v=0

# transaction
"""
=> POST https://api.shasta.trongrid.io/wallet/createtransaction
{
    "to_address": "41340967e825557559dc46bbf0eabe5ccf99fd134e",
    "owner_address": "419cf784b4cc7531f1598c4c322de9afdc597fe760",
    "amount": 23000000,
}

<=
{
    "visible": false,
    "txID": "167a4986be77b4c3e8a96d9f39ce270deaa659c224476c043ef2f461ba6e9a50",
    "raw_data": {
        "contract": [ ....
        ],
        "ref_block_bytes": "d332",
        "ref_block_hash": "1a2ce1f1010d5fe5",
        "expiration": 1576739634000,
        "timestamp": 1576739575486,
    },
    "raw_data_hex": "0a02d33222081a2ce1f1010d5fe540d0f685e8f12d5a68080112640a2d747970652e676f6f676c65617069732e636f6d2f70726f746f636f6c2e5472616e73666572436f6e747261637412330a15419cf784b4cc7531f1598c4c322de9afdc597fe760121541340967e825557559dc46bbf0eabe5ccf99fd134e18c0e7fb0a70bead82e8f12d",
}

=> POST https://api.shasta.trongrid.io/wallet/broadcasttransaction
{
    "visible": false,
    "txID": "1275ac815e624f3a0e59c5d598f19ee2d5a50dd1736e37659e6b0c40f19cdeec",
    "raw_data": {
        "contract": [ ....
        ],
        "ref_block_bytes": "d332",
        "ref_block_hash": "1a2ce1f1010d5fe5",
        "expiration": 1576739634000,
        "timestamp": 1576739575756,
    },
    "raw_data_hex": "0a02d33222081a2ce1f1010d5fe540d0f685e8f12d5a68080112640a2d747970652e676f6f676c65617069732e636f6d2f70726f746f636f6c2e5472616e73666572436f6e747261637412330a15419cf784b4cc7531f1598c4c322de9afdc597fe760121541340967e825557559dc46bbf0eabe5ccf99fd134e18c0e7fb0a70ccaf82e8f12d",
    "signature": [
        "dc2c6b3f97f64e043a3dfe37d7686dbb1ab21e3271b372c6de1c6ba0a4ff609b8e62254629ce9027d247c3eca49bf481f3bc8eee7bcca4dc1a28c6b158519c0300"
    ],
}

"""


# how to get txID
# print(hashlib.sha256(bytes.fromhex('0a02d33222081a2ce1f1010d5fe540d0f685e8f12d5a68080112640a2d747970652e676f6f676c65617069732e636f6d2f70726f746f636f6c2e5472616e73666572436f6e747261637412330a15419cf784b4cc7531f1598c4c322de9afdc597fe760121541340967e825557559dc46bbf0eabe5ccf99fd134e18c0e7fb0a70ccaf82e8f12d')).hexdigest())
# print('1275ac815e624f3a0e59c5d598f19ee2d5a50dd1736e37659e6b0c40f19cdeec')
