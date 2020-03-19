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
raw_data = bytes.fromhex('0a0212462208055912e38b80f75e40f083f5c5f12d5aa3010804129e010a30747970652e676f6f676c65617069732e636f6d2f70726f746f636f6c2e566f74655769746e657373436f6e7472616374126a0a1541d70b00b6f9311fbc8d4de53cb666cf1d0ad6a25c121a0a154178c842ee63b253f8f0d2955bbc582c661a078c9d10b817121a0a1541d25855804e4e65de904faf3ac74b0bdfc53fac7610b81712190a15414a193c92cd631c1911b99ca964da8fd342f4cddd100370efb8f1c5f12d')

# raw_data = bytes.fromhex('0a02d33222081a2ce1f1010d5fe540d0f685e8f12d5a68080112640a2d747970652e676f6f676c65617069732e636f6d2f70726f746f636f6c2e5472616e73666572436f6e747261637412330a15419cf784b4cc7531f1598c4c322de9afdc597fe760121541340967e825557559dc46bbf0eabe5ccf99fd134e18c0e7fb0a70ccaf82e8f12d')

# raw_data = bytes.fromhex('0a0282a522085d553a3cdee4975e40c0e386eff12d5a76080212720a32747970652e676f6f676c65617069732e636f6d2f70726f746f636f6c2e5472616e736665724173736574436f6e7472616374123c0a0731303032303030121541c7134806175a06712225761a2f0673a3444f14521a154118b2811f31e8c923b9d5651bafdadebee4ba966620a0f8fa0570d09c83eff12d')

# raw_data = bytes.fromhex('0a029f9122082fc729fb70fb41514098d7d790f32d5a860108041281010a30747970652e676f6f676c65617069732e636f6d2f70726f746f636f6c2e566f74655769746e657373436f6e7472616374124d0a1541340967e825557559dc46bbf0eabe5ccf99fd134e12190a1541f16412b9a17ee9408646e2a21e16478f72ed1e95100312190a1541f1a0466076c57c9f6d07decc86021ddbf8bae0b2100570c392d490f32d')


raw_data = bytes.fromhex('0A021B05220803535967FF5DBD8B40A0D8C5E28E2E5AD001082E12CB010A3C747970652E676F6F676C65617069732E636F6D2F70726F746F636F6C2E4163636F756E745065726D697373696F6E557064617465436F6E7472616374128A010A154186E2825C8ECADECBC3D4839180297E0158F2D5F712241A056F776E657220013A190A154186E2825C8ECADECBC3D4839180297E0158F2D5F71001224B080210021A06616374697665200232207FFF1FC0033E01000000000000000000000000000000000000000000000000003A190A154186E2825C8ECADECBC3D4839180297E0158F2D5F7100270E185C2E28E2E')

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
    print('  owner', base58.b58encode_check(vote_contract.owner_address))
    for vote in vote_contract.votes:
        print('  vote', base58.b58encode_check(vote.vote_address))

elif contract.type == tron_pb.Transaction.Contract.TriggerSmartContract:
    assert contract.parameter.type_url == 'type.googleapis.com/protocol.TriggerSmartContract'
    trigger = contract_pb.TriggerSmartContract.FromString(contract.parameter.value)
    print(trigger)

elif contract.type == tron_pb.Transaction.Contract.TransferAssetContract:
    trxfer = contract_pb.TransferAssetContract.FromString(contract.parameter.value)
    print(trxfer)

elif contract.type == tron_pb.Transaction.Contract.AccountPermissionUpdateContract:
    trxfer = contract_pb.AccountPermissionUpdateContract.FromString(contract.parameter.value)
    print(trxfer)

raise SystemExit



print("-" * 80)
raw_data = bytes.fromhex('0a1541b5f8a2ab78bfb1afea17558f8a32d1c988283019121541e42d76d15b7ecd27a92cc9551738c2635c63b71c1880ab8f122244a3082be900000000000000000000000000000000000000000000000000000000000000060000000000000000000000000000000000000000000000000000000000000001')

trigger = contract_pb.TriggerSmartContract.FromString(raw_data)
print(trigger)
print(trigger.data[:4])

print(trigger.data[:4].hex())

from eth_hash.auto import keccak as keccak_256

print(keccak_256(b'GoodLuck(uint256,uint256)')[:4])


raw_data = bytes.fromhex('''0a154146a23e25df9a0f6c18729dda9ad1af3b6a1311601080dac40922c2070a20720476792dd2f01b5ff441cb38d4b29d10b52c1c8e6dfeea13f89d547e3c14d1122004a631b9ac0e0da0891f459f6a881164a4fd76ad48e5
a77268de8fd104975a5f1a20c54db69e4f1de8c66237cc0f1074c6b4096ef7323a65633af221948eea1c095822c404f1522886257a4a35e386ebf608f15470188e9bf5c956ec5c5a708a3b030fb05469dd68244c3c3f56b452d75bed7374c111a275b7
de7fa6a6ce424fcec87357f2a2eb97ac3dd1e90b184b35b4aee25507d306b6fe438e8c5128579d15f30301dde60e8506d36dc7788f01e7d5f94cc96be2efd1e70c1c25baccaf62f8d90610c1eb921f5058a1daa275c446e7bc3f1e2cf499c463abb21b
062452d3273dc90a00b690604e4eef6e665fb63ab4294d0404cca203dc6105e840b034684790dd71de8a99116ce576ebe1e9a39cc7076eb05384275f43c19b04928897f4ef7082302e4ec7879e46fa788c9aade675ded4b4c1acc756eb7b20418f5c0c
ac1f32f7021baee5e6961c02236afffa880bb24a33f575983389b5ea86dd25497f1b8427abc548a0ce7d499d544ddf69f181a6474e3dc2d1e24a5291c287864c13fd3be17b455f35fd510422e853bd19f068c3cfab69a06d4d5260406bac13ab950cf7
e6ed211521664b7acdd10288c785962690663b8fa194b9d0e86fd10643c09cb2c2ef11e9e66c612f2cca89c67dc2f16781c13a2f08bcf6e49fd80e0a852b1c38ebae2677825ba18e5a4b70050ad333fd182260d0d40ca314ccbc1981569c6e9642fee5
b507c9933969dd704a741a3c2ce225b3afa06ee4bea0e333193a3a06df1cb8eda396bf7d950b70a7f1fb1d47998508f628e658af3bdbbb5cdb97251a1264be0d8e0dd43711f3cefa4ea5f45f609e7d7403a0ffcad717cd1453d25120a0ae8c0adfe893
5371608046d5d3579b6ef719a5fc5ab95ccdb6adc23b3ebeeab8a6905a140377e92a5062d197aa06f0d9bca9885256ddd0e100b2b6f7fd260e062e04bc40371d193d967dec04df56bbcb8af9d2fd95c742619f13fdafeb08629d18e219261e67b9dd32
ef4c5906acc8cc2e78cb399584ec8f6132c00198b11ac7cc6e38ff358863e5d68f50178f023b7e12c241977e4d24e934db8d68ef40df5adb7bdaa260372364c380644f948c086f54c4e86f5b70f74c9662b5441bfe53375bfc29c9e7fae2d7e1bde0ca
d75d6043f34454bb198152ab40632d781961985e799713bb6585f256ed8b324d7f63a0f513052058bea3d71c074e13d0f14343d8072d054f47ba913e02229c6493b00b98c82cb9d2a98d4c479ffb965a853e6a654af659ddefe424ea774eb8267bf6fb
0a925a77febfd8dd8fc1be392d2a40f2d69df9ce92abd5a0c424a03842a0997fb56b8159b81f85684fe9d001aa9e48f6e7d3c9488e13a187e248deeb7dac76adf63f2ee82f271a6035b13e59c52306''')

shielded = contract_pb.ShieldedTransferContract.FromString(raw_data)
print(shielded)


print('-' * 80)

raw_data = bytes.fromhex("...")

shielded = contract_pb.CreateSmartContract.FromString(raw_data)
print(shielded)
