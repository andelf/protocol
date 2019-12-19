import sys

sys.path.insert(0, './proto')

import proto.core.Tron_pb2 as tron_pb
import proto.core.Contract_pb2 as contract_pb


raw_data = bytes.fromhex(
    '0a026d492208cd8eca44b3ab8af14098b6dbc2f12d5a69080112650a2d747970652e676f6f676c65617069732e636f6d2f70726f746f636f6c2e5472616e73666572436f6e747261637412340a15419cf784b4cc7531f1598c4c322de9afdc597fe760121541340967e825557559dc46bbf0eabe5ccf99fd134e1880cab5ee017088ecd7c2f12d'
)

#raw_data = bytes.fromhex(
#    '0a0271b62208a181edb673c1a24140f0f0aac4f12d5a6a080412660a30747970652e676f6f676c65617069732e636f6d2f70726f746f636f6c2e566f74655769746e657373436f6e747261637412320a1541340967e825557559dc46bbf0eabe5ccf99fd134e12190a1541f16412b9a17ee9408646e2a21e16478f72ed1e95100270ca9ea7c4f12d'
#)

raw_data = bytes.fromhex(
    '0a02c02b2208282687d679ec312140d8d389e1f12d5a68080112640a2d747970652e676f6f676c65617069732e636f6d2f70726f746f636f6c2e5472616e73666572436f6e747261637412330a15419cf784b4cc7531f1598c4c322de9afdc597fe760121541340967e825557559dc46bbf0eabe5ccf99fd134e18c0f0f50b70c28f86e1f12d'
)

raw_data = bytes.fromhex('0a025d052208b1d45a4ddb568ca440b2c5b1e1f12d5216202053656e742066726f6d2054726f6e57616c6c65745a68080112640a2d747970652e676f6f676c65617069732e636f6d2f70726f746f636f6c2e5472616e73666572436f6e747261637412330a154143458c9f0ffbff6d093093668e76e80d567c6ec51215412b9f0c78c974855a4a33028094bef4538acc8e2718f891881a70f3b682a4b511')

raw_data = bytes.fromhex('0a025e5b2208cbdd62dee287ae7d4090d4e4e1f12d5aae01081f12a9010a31747970652e676f6f676c65617069732e636f6d2f70726f746f636f6c2e54726967676572536d617274436f6e747261637412740a1541dafa937dd5c79d6d0bd885fae3f841b7bf2b143d12154174472e7d35395a6b5add427eecb7f4b62ad2b0712244a9059cbb0000000000000000000000007754b125e780b84b709382e3fe68ee0b7d003fc500000000000000000000000000000000000000000000000000000593ccabf8cf70e088e1e1f12d900180ade204')

raw_obj = tron_pb.Transaction.raw.FromString(raw_data)
print(raw_obj)

contract = raw_obj.contract[0]  # only 1

print(contract)

if contract.type == tron_pb.Transaction.Contract.TransferContract:
    print('yep')
    # contract.parameter is googleapis.Any
    print('type =', contract.parameter.type_url)

    assert contract.parameter.type_url == "type.googleapis.com/protocol.TransferContract"
    trxfer = contract_pb.TransferContract.FromString(contract.parameter.value)
    print(trxfer)

elif contract.type == tron_pb.Transaction.Contract.VoteWitnessContract:
    assert contract.parameter.type_url == 'type.googleapis.com/protocol.VoteWitnessContract'
    vote = contract_pb.VoteWitnessContract.FromString(contract.parameter.value)
    print(vote)

elif contract.type == tron_pb.Transaction.Contract.TriggerSmartContract:
    assert contract.parameter.type_url == 'type.googleapis.com/protocol.TriggerSmartContract'
    trigger = contract_pb.TriggerSmartContract.FromString(contract.parameter.value)
    print(trigger)
