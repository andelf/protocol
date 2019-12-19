import sys

sys.path.insert(0, './proto')

import hashlib
import base58

import proto.core.Tron_pb2 as tron_pb
import proto.core.Contract_pb2 as contract_pb


raw_data = bytes.fromhex(
    '0a026d492208cd8eca44b3ab8af14098b6dbc2f12d5a69080112650a2d747970652e676f6f676c65617069732e636f6d2f70726f746f636f6c2e5472616e73666572436f6e747261637412340a15419cf784b4cc7531f1598c4c322de9afdc597fe760121541340967e825557559dc46bbf0eabe5ccf99fd134e1880cab5ee017088ecd7c2f12d'
)

#raw_data = bytes.fromhex(
#    '0a0271b62208a181edb673c1a24140f0f0aac4f12d5a6a080412660a30747970652e676f6f676c65617069732e636f6d2f70726f746f636f6c2e566f74655769746e657373436f6e747261637412320a1541340967e825557559dc46bbf0eabe5ccf99fd134e12190a1541f16412b9a17ee9408646e2a21e16478f72ed1e95100270ca9ea7c4f12d'
#)

# raw_data = bytes.fromhex(
#     '0a02c02b2208282687d679ec312140d8d389e1f12d5a68080112640a2d747970652e676f6f676c65617069732e636f6d2f70726f746f636f6c2e5472616e73666572436f6e747261637412330a15419cf784b4cc7531f1598c4c322de9afdc597fe760121541340967e825557559dc46bbf0eabe5ccf99fd134e18c0f0f50b70c28f86e1f12d'
# )

# transaction with memo
# raw_data = bytes.fromhex('0a025d052208b1d45a4ddb568ca440b2c5b1e1f12d5216202053656e742066726f6d2054726f6e57616c6c65745a68080112640a2d747970652e676f6f676c65617069732e636f6d2f70726f746f636f6c2e5472616e73666572436f6e747261637412330a154143458c9f0ffbff6d093093668e76e80d567c6ec51215412b9f0c78c974855a4a33028094bef4538acc8e2718f891881a70f3b682a4b511')

# trigger smart contract
# raw_data = bytes.fromhex('0a025e5b2208cbdd62dee287ae7d4090d4e4e1f12d5aae01081f12a9010a31747970652e676f6f676c65617069732e636f6d2f70726f746f636f6c2e54726967676572536d617274436f6e747261637412740a1541dafa937dd5c79d6d0bd885fae3f841b7bf2b143d12154174472e7d35395a6b5add427eecb7f4b62ad2b0712244a9059cbb0000000000000000000000007754b125e780b84b709382e3fe68ee0b7d003fc500000000000000000000000000000000000000000000000000000593ccabf8cf70e088e1e1f12d900180ade204')

# raw_data = bytes.fromhex('0a02c6ab220866db818d157748b240d8abbae3f12d5a69080112650a2d747970652e676f6f676c65617069732e636f6d2f70726f746f636f6c2e5472616e73666572436f6e747261637412340a15419cf784b4cc7531f1598c4c322de9afdc597fe760121541340967e825557559dc46bbf0eabe5ccf99fd134e18a8cab5d40370d7e7b6e3f12d')

# vote for 3 sr
# raw_data = bytes.fromhex('0a0212462208055912e38b80f75e40f083f5c5f12d5aa3010804129e010a30747970652e676f6f676c65617069732e636f6d2f70726f746f636f6c2e566f74655769746e657373436f6e7472616374126a0a1541d70b00b6f9311fbc8d4de53cb666cf1d0ad6a25c121a0a154178c842ee63b253f8f0d2955bbc582c661a078c9d10b817121a0a1541d25855804e4e65de904faf3ac74b0bdfc53fac7610b81712190a15414a193c92cd631c1911b99ca964da8fd342f4cddd100370efb8f1c5f12d')



#raw_data = bytes.fromhex('0a02d33222081a2ce1f1010d5fe540d0f685e8f12d5a68080112640a2d747970652e676f6f676c65617069732e636f6d2f70726f746f636f6c2e5472616e73666572436f6e747261637412330a15419cf784b4cc7531f1598c4c322de9afdc597fe760121541340967e825557559dc46bbf0eabe5ccf99fd134e18c0e7fb0a70ccaf82e8f12d')

raw_data = bytes.fromhex('0a0282a522085d553a3cdee4975e40c0e386eff12d5a76080212720a32747970652e676f6f676c65617069732e636f6d2f70726f746f636f6c2e5472616e736665724173736574436f6e7472616374123c0a0731303032303030121541c7134806175a06712225761a2f0673a3444f14521a154118b2811f31e8c923b9d5651bafdadebee4ba966620a0f8fa0570d09c83eff12d')

raw_obj = tron_pb.Transaction.raw.FromString(raw_data)
print(raw_obj)

contract = raw_obj.contract[0]  # only 1

print(contract)


tx_id = hashlib.sha256(raw_data).digest()
print('TX', tx_id.hex())


if contract.type == tron_pb.Transaction.Contract.TransferContract:
    print('yep')
    # contract.parameter is googleapis.Any
    print('type =', contract.parameter.type_url)

    assert contract.parameter.type_url == "type.googleapis.com/protocol.TransferContract"
    trxfer = contract_pb.TransferContract.FromString(contract.parameter.value)
    print(trxfer)

    print(base58.b58encode_check(trxfer.owner_address), '=>', base58.b58encode_check(trxfer.to_address))

elif contract.type == tron_pb.Transaction.Contract.VoteWitnessContract:
    assert contract.parameter.type_url == 'type.googleapis.com/protocol.VoteWitnessContract'
    vote_contract = contract_pb.VoteWitnessContract.FromString(contract.parameter.value)
    print(vote_contract)
    for vote in vote_contract.votes:
        print('  vote', base58.b58encode_check(vote.vote_address))

elif contract.type == tron_pb.Transaction.Contract.TriggerSmartContract:
    assert contract.parameter.type_url == 'type.googleapis.com/protocol.TriggerSmartContract'
    trigger = contract_pb.TriggerSmartContract.FromString(contract.parameter.value)
    print(trigger)

elif contract.type == tron_pb.Transaction.Contract.TransferAssetContract:
    trxfer = contract_pb.TransferAssetContract.FromString(contract.parameter.value)
    print(trxfer)
