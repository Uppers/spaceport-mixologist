import json
from algosdk.v2client import algod
from algosdk import account, mnemonic
from algosdk.future.transaction import AssetConfigTxn
import Transactions.private_info as pi # this file is included in the gitignore file.

class Utility():
    def __init__(self):
        self.algod_client = algod.AlgodClient(algod_token=pi.algod_token, algod_address=pi.algod_address)
        self.account_credentials = self._accounts()

    def account_details(self, string_mnemonic):
        public_key = mnemonic.to_public_key(string_mnemonic)
        secret_key = mnemonic.to_private_key(string_mnemonic)
        return {'pk':public_key, 'sk':secret_key, 'mn':string_mnemonic}

    
    def _accounts(self):
        accounts = {}
        counter = 1
        for m in [pi.account1_mnemonic, pi.account2_mnemonic, pi.player_mnemonic]:
            accounts[counter] = {}
            accounts[counter]['pk'] = mnemonic.to_public_key(m)
            accounts[counter]['sk'] = mnemonic.to_private_key(m)
            counter += 1
        return accounts

    def wait_for_confirmation(self, txid):
        """
        Utility function to wait until the transaction is
        confirmed before proceeding.
        """
        last_round = self.algod_client.status().get('last-round')
        txinfo = self.algod_client.pending_transaction_info(txid)
        while not (txinfo.get('confirmed-round') and txinfo.get('confirmed-round') > 0):
            print("Waiting for confirmation")
            last_round += 1
            self.algod_client.status_after_block(last_round)
            txinfo = self.algod_client.pending_transaction_info(txid)
        print("Transaction {} confirmed in round {}.".format(txid, txinfo.get('confirmed-round')))
        return txinfo

    #   Utility function used to print created asset for account and assetid
    def print_created_asset(self, account, assetid):    
        # note: if you have an indexer instance available it is easier to just use this
        # response = myindexer.accounts(asset_id = assetid)
        # then use 'account_info['created-assets'][0] to get info on the created asset
        account_info = self.algod_client.account_info(account)
        idx = 0
        for my_account_info in account_info['created-assets']:
            scrutinized_asset = account_info['created-assets'][idx]
            idx = idx + 1       
            if (scrutinized_asset['index'] == assetid):
                print("Asset ID: {}".format(scrutinized_asset['index']))
                print(json.dumps(my_account_info['params'], indent=4))
                break


    #   Utility function used to print asset holding for account and assetid
    def print_asset_holding(self, account, assetid):
        # note: if you have an indexer instance available it is easier to just use this
        # response = myindexer.accounts(asset_id = assetid)
        # then loop thru the accounts returned and match the account you are looking for
        account_info = self.algod_client.account_info(account)
        idx = 0
        for my_account_info in account_info['assets']:
            scrutinized_asset = account_info['assets'][idx]
            idx = idx + 1        
            if (scrutinized_asset['asset-id'] == assetid):
                print("Asset ID: {}".format(scrutinized_asset['asset-id']))
                print(json.dumps(scrutinized_asset, indent=4))
                break

    # writes a string to a txt file
    def write_to_file(self, filename, string):
        with open(filename, 'w') as f:
            f.write(string)

    # reads a string from a text file
    def read_from_file(self, filename):
        with open(filename, 'r') as f:
            return f.read()

    # reads json from a text file 
    def read_json_from_file(self, filename):
        try:
            f = open(filename, 'r')
            return json.loads(f.read())
        except:
            return {'pk': "", "sk": ""}