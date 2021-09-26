import os
import sys
from datetime import datetime
from Transactions.utility import Utility
from algosdk.future.transaction import AssetTransferTxn
from algosdk.error import AlgodHTTPError
from Transactions.private_info import account1_mnemonic, account2_mnemonic, player_mnemonic


class Transaction():

    def __init__(self, sender_pk, sender_sk, recipient_pk):
        self.sender_pk = sender_pk # the public address of the sender
        self.sender_sk = sender_sk # the secret key of the sender
        self.recipient_pk = recipient_pk # the public address of the recipient
        self.utility = Utility()
        self.asset_id = int(self.utility.read_from_file(os.path.join("Transactions","asset_id.txt")))
        self.params = self.utility.algod_client.suggested_params() 

    def send_transaction(self, transfer_amount, note_addition=None):
        note = {'timestamp': datetime.now()} # this ensures uniqueness
        if note_addition:
            note['addition'] = note_addition # this allows an extra piece of information, such as when the game started.f
        txn = AssetTransferTxn(
        sender = self.sender_pk,
        sp= self.params,
        receiver= self.recipient_pk,
        amt = transfer_amount, 
        index = self.asset_id,
        note = str(note).encode()
        )
        txid = self.utility.algod_client.send_transaction(txn.sign(self.sender_sk))
        #self.utility.wait_for_confirmation(txid)
        print(transfer_amount)
        return txid

class QueryTransaction():
    def __init__(self, sender_pk, sender_sk):
        self.sender_pk = sender_pk
        self.sender_sk = sender_sk
        self.utility = Utility()
        self.params = self.utility.algod_client.suggested_params() 
        self.asset_id = int(self.utility.read_from_file(os.path.join("Transactions","asset_id.txt")))

    def _send_transaction(self, recipient_pk):
        note = {'timestamp': datetime.now()} # this ensures uniqueness
        txn = AssetTransferTxn(
        sender = self.sender_pk,
        sp= self.params,
        receiver= recipient_pk,
        amt = 1, 
        index = self.asset_id,
        note = str(note).encode()
        )
        txid = self.utility.algod_client.send_transaction(txn.sign(self.sender_sk))
        #self.utility.wait_for_confirmation(txid)
        return txid


    def is_opted_in(self, recipient_pk):
        try:
            self._send_transaction(recipient_pk)
        except AlgodHTTPError:
            print("here") 
            return False
        return True  

#from Transactions.utility import Utility


#utility = Utility()

#sender_account = utility.account_details(account1_mnemonic)
#sender_account2 = utility.account_details(account2_mnemonic)
#sender_player = utility.account_details(player_mnemonic)

#transaction = Transaction(sender_account['pk'], sender_account['sk'], sender_player['pk'])

#print(transaction)

#sender_account = 1
#recipient_account = 3

# account public keys
#sender_pk = utility.account_credentials[sender_account]['pk']
#recipient_pk = utility.account_credentials[recipient_account]['pk']

# set up the transaction


# sender account secret key
#sender_sk = utility.account_credentials[sender_account]['sk']

# sign the transfer transaction 
#stxn = txn.sign(sender_sk)

# send the transaction 
#txid = utility.algod_client.send_transaction(stxn)
#print(txid)

# wait for the transaction to be confirmed
#utility.wait_for_confirmation(txid)

# the balance should have increased by 10
#utility.print_asset_holding(recipient_pk, ASSET_ID)
