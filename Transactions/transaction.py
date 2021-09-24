import os
from datetime import datetime
from Transactions.utility import Utility
from algosdk.future.transaction import AssetTransferTxn


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
