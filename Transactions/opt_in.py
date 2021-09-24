from utility import Utility
from algosdk.future.transaction import AssetTransferTxn

############
## Opt In ##
############


class OptIn():

    def __init__(self, asset_id, account_pk):
        self.utility = Utility()
        self.asset_id = asset_id
        self.params = self.utility.algod_client.suggested_params()
        self.account_pk = account_pk
        

    def is_opted_in(self): # checks to see if the account is already opted in.
        account_info = self.utility.algod_client.account_info(self.account_pk)
        holding = False
        idx = 0
        for my_account_info in account_info['assets']:
            scrutinized_asset = account_info['assets'][idx]
            idx+=1
            if scrutinized_asset['asset-id'] == self.asset_id:
                holding = True
        return holding

    def send_transaction(self, account_sk): # opts the account in
        if self.is_opted_in() == False:
        # use the AssetTransferTxn class to transfer assets and opt-in
            txn = AssetTransferTxn(
                sender=self.account_pk,
                sp=self.params,
                receiver=self.account_pk,
                amt=0,
                index=self.asset_id
            )
            txid = self.utility.algod_client.send_transaction(txn.sign(account_sk))
            self.utility.wait_for_confirmation(txid)
            self.utility.print_asset_holding(self.account_pk, self.asset_id)



# The reusable utility functions and variables 
#utility = Utility()

# the asset id for which you are preparing your account
#ASSET_ID = 5

#params = utility.algod_client.suggested_params()

# public key for account 3
#account3_pk = utility.account_credentials[3]['pk']


#account_info = utility.algod_client.account_info(account3_pk)

#holding = None

#idx = 0

#for my_account_info in account_info['assets']:
#    scrutinized_asset = account_info['assets'][idx]
#    idx+=1
#    if scrutinized_asset['asset-id'] == ASSET_ID:
#        holding = True
#        break

#if not holding:
#    # use the AssetTransferTxn class to transfer assets and opt-in
#    txn = AssetTransferTxn(
#        sender=account3_pk,
#        sp=params,
#        receiver=account3_pk,
#        amt=0,
#        index=ASSET_ID
#    )

# sender account's secret key
#account3_sk = utility.account_credentials[3]['sk']

# sign transaction
#stxn = txn.sign(account3_sk)

# send the transaction
#txid = utility.algod_client.send_transaction(stxn)
#print(txid)

# wait for the transaction to be confirmed
#utility.wait_for_confirmation(txid)

# check the asset holding for that account
# this should show a holding with a balance of 0
#utility.print_asset_holding(account3_pk, ASSET_ID)




