import os
from datetime import datetime
from Transactions.utility import Utility
from algosdk.future.transaction import AssetTransferTxn
from algosdk.error import AlgodHTTPError, WrongChecksumError



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
        except (AlgodHTTPError, WrongChecksumError):
            print("here") 
            return False
        return True  

