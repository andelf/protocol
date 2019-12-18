import sys

sys.path.insert(0, './proto')

import proto.core.Tron_pb2 as tron_pb
import proto.core.Contract_pb2 as contract_pb


raw_data = bytes.fromhex(
    '0a026d492208cd8eca44b3ab8af14098b6dbc2f12d5a69080112650a2d747970652e676f6f676c65617069732e636f6d2f70726f746f636f6c2e5472616e73666572436f6e747261637412340a15419cf784b4cc7531f1598c4c322de9afdc597fe760121541340967e825557559dc46bbf0eabe5ccf99fd134e1880cab5ee017088ecd7c2f12d'
)

raw_data = bytes.fromhex(
    '0a0271b62208a181edb673c1a24140f0f0aac4f12d5a6a080412660a30747970652e676f6f676c65617069732e636f6d2f70726f746f636f6c2e566f74655769746e657373436f6e747261637412320a1541340967e825557559dc46bbf0eabe5ccf99fd134e12190a1541f16412b9a17ee9408646e2a21e16478f72ed1e95100270ca9ea7c4f12d'
)

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
