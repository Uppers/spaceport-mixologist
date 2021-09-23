from algosdk.v2client import algod
import json

# connect to sandbox node on testnet
algod_address = "http://localhost:4001"
algod_token = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
algod_client = algod.AlgodClient(algod_token, algod_address)

# check the status of this node
status = algod_client.status()
print(json.dumps(status, indent=4))

# check that you are connected to the correct node / network.
#try:
#    params = algod_client.suggested_params()
#    print(json.dumps(vars(params), indent=4))
#except Exception as e:
#    print(e)
