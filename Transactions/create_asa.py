import os
from algosdk.future.transaction import AssetConfigTxn
from Transactions.utility import Utility


class CreateASA():

    def __init__(self, asset_name, creator_pk, creator_sk, asset_amount = 10000000000, strict_empty_address_check = False, manager_pk = "", reserve_pk = "", freeze_pk = "", clawback_pk=""):
        self.utility = Utility()
        self.asset_name = asset_name # the name of the asset to be created
        self.asset_amount = asset_amount # the amount of the asset to be created
        self.creator_pk = creator_pk  # the address of the account sending the transaction
        self.creator_sk = creator_sk # the secret key used for signing the transaction
        self.manager_pk = manager_pk # what does a manager do?
        self.reserve_pk = reserve_pk # what is this for?
        self.freeze_pk = freeze_pk # this address can send a transaction to freeze the assets in a wallet
        self.clawback_pk = clawback_pk # this address can take the assets from another wallet
        self.strict_empty_address_check = strict_empty_address_check # if False then you can set empty values for the manager/ clawback etc.
        self.params = self.utility.algod_client.suggested_params()

    def send_transaction(self):
        txn = AssetConfigTxn(
        sender= self.creator_pk,
        sp= self.params,
        total= self.asset_amount,  
        default_frozen=False,
        unit_name= self.asset_name.upper()[0:3], # first 4 letters in upper case
        asset_name= self.asset_name,
        manager= self.manager_pk,
        reserve= self.reserve_pk,
        freeze= self.freeze_pk,
        clawback= self.clawback_pk,
        strict_empty_address_check = self.strict_empty_address_check, 
        url= None,
        decimals=0
        )
        txid = self.utility.algod_client.send_transaction(txn.sign(self.creator_sk)) 
        self.utility.wait_for_confirmation(txid)
        return txid

    def save_asset_details(self, txid):
        try:
            # get asset id from transaction
            # get the new asset's information from the creator account
            ptx = self.utility.algod_client.pending_transaction_info(txid)
            asset_id = ptx["asset-index"]
            self.utility.write_to_file(os.path.join("Transactions","asset_id.txt"), str(asset_id)) # write the newly created asset id to file so it can be referenced later.
            self.utility.print_created_asset(self.creator_pk, asset_id)
            self.utility.print_asset_holding(self.creator_pk, asset_id)
        except Exception as e:
            print(f"Exception: {e}")




###########
## SETUP ##
###########

#utility = Utility()

########################
## Create Transaction ##
########################

# get the network parameters for transactions
#params = utility.algod_client.suggested_params()

# Asset creation transaction:
# Account 1 creates an asset called latinum and sets...
# Account 2 as the manager, reserve, freeze and clawback address.

#account1_pk = utility.account_credentials[1]['pk']
#account2_pk = utility.account_credentials[2]['pk']
#asset_name = "mixologist" # change this to be anything you like

#txn = AssetConfigTxn(
#    sender= account1_pk,
#    sp= params,
#    total=10000000000, # 10 bn 
#    default_frozen=False,
#    unit_name= asset_name.upper()[0:3], # first 4 letters in upper case
#    asset_name= asset_name,
#    manager= account2_pk,
#    reserve= account2_pk,
#    freeze= account2_pk,
#    clawback= account2_pk, 
#    url= None,
#    decimals=0)

##########################
## Sign the transaction ##
##########################

#stxn = txn.sign(utility.account_credentials[1]['sk']) # signing with the secret key

###########################################################################
## Send the create ASA transaction to the blockchain and print the TXNID ##
###########################################################################

# send the transaction to the network and retrieve the transaction id
#txid = utility.algod_client.send_transaction(stxn) 
#print(f"Transaction ID: {txid}")

# Retrieve the asset ID of the newly created asset by:
# 1. ensuring that the creation transaction was confirmed, and;
# 2. then grabbing the asset id from the transaction.

# wait for the transaction to be confirmed
#utility.wait_for_confirmation(txid)




