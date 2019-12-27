from time import time as unix_time
from pprint import pprint
import requests
import hashlib

import base58
import ecdsa
from eth_hash.auto import keccak as keccak_256

resp = requests.post('https://api.shasta.trongrid.io/wallet/getblockbylatestnum', json={"num": 1})


block = resp.json()['block'][0]

# pprint(block)

ref_block_num = block['block_header']['raw_data']['number']
ref_block_hash = bytes.fromhex(block['blockID'])

ref_block_num = int.to_bytes(ref_block_num, 8, 'big')[6:8].hex()
ref_block_hash = ref_block_hash[8:16].hex()

print(ref_block_num, ref_block_hash)


raw_priv_key = bytes.fromhex('d705fc17c82942f85848ab522e42d986279028d09d12ad881bdc0e1327031976')

priv_key = ecdsa.SigningKey.from_string(raw_priv_key, curve=ecdsa.SECP256k1)
pub_key = priv_key.get_verifying_key().to_string()

print('Pub Key:', pub_key.hex())

primitive_addr = b'\x41' + keccak_256(pub_key)[-20:]
addr = base58.b58encode_check(primitive_addr)

TO_ADDR = base58.b58decode_check('TEiMQZpHs4N4HuTKP3xcCKZ68XSQSfEbMW').hex()

print('Addr:', addr)

transaction = {
    "to_address": TO_ADDR,
    "owner_address": primitive_addr.hex(),
    "amount": 1000,
}

print('=> createtransaction')
resp = requests.post('https://api.shasta.trongrid.io/wallet/createtransaction', json=transaction)
payload = resp.json()

pprint(payload)

def signencode(r, s, order):
    # order is stable for curves
    print((r, s))

    return r.to_bytes(32, 'big') + s.to_bytes(32, 'big')

raw_data = bytes.fromhex(payload['raw_data_hex'])
signature = priv_key.sign_deterministic(raw_data, hashfunc=hashlib.sha256, sigencode=signencode)


# calculate v?
def verifying_key_to_addr(key):
    pub_key = key.to_string()
    primitive_addr = b'\x41' + keccak_256(pub_key)[-20:]
    addr = base58.b58encode_check(primitive_addr)
    return addr

pub_keys = ecdsa.VerifyingKey.from_public_key_recovery(
    signature[:64], raw_data, curve=ecdsa.SECP256k1,
    hashfunc=hashlib.sha256
)

print(pub_keys)

for pk in pub_keys:
    print(verifying_key_to_addr(pk))

v = 1
signature += bytes([v])

print('signature =', signature.hex())


payload['signature'] = [signature.hex()]

# pprint(payload)

print('=> broadcasttransaction')
resp = requests.post('https://api.shasta.trongrid.io/wallet/broadcasttransaction', json=payload)

result = resp.json()

pprint(result)
if 'message' in result:
    print('MSG:', bytes.fromhex(result['message']))
