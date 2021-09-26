import os
from Transactions.private_info import player_mnemonic 
from Transactions.opt_in import OptIn
from Transactions.utility import Utility

utility = Utility()
account_to_opt_in_mnemonic = player_mnemonic # "player_mnemonic is imported from the private_info file not included in the git repo"
if not len(account_to_opt_in_mnemonic):
    print("please enter the mnemonic for the account you want to opt in")
else:
    account_details = utility.account_details(account_to_opt_in_mnemonic)
    account_pk = account_details['pk']
    account_sk = account_details['sk']
    try:
        asset_id = utility.read_from_file(os.path.join("Transactions", "asset_id.txt"))
    except:
        print("you need to run main.py first to generate an asset_id")
    if asset_id:
        opt_in = OptIn(asset_id, account_pk)
        opt_in.send_transaction(account_sk)


