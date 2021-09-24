import os 
import pygame
from pathlib import Path 
from Game.state import State
from Transactions.private_info import *
from Transactions.utility import Utility
from Transactions.create_asa import CreateASA

def create_asa():
    # create the assets and save the name
    utility = Utility()
    creator_account = utility.account_details(account1_mnemonic)
    manager_account = utility.account_details(account2_mnemonic)

    asset_name = "game coin"
    creator_pk = creator_account['pk'] 
    creator_sk = creator_account['sk']
    manager_pk = manager_account['pk']
    create_asset = CreateASA(asset_name, creator_pk, creator_sk, manager_pk = manager_pk, reserve_pk = manager_pk, freeze_pk = manager_pk)
    txid = create_asset.send_transaction()
    create_asset.save_asset_details(txid)

def start():
    # starts the game
    pygame.init()
    # caption 
    pygame.display.set_caption("SPACEPORT MIXOLOGIST")
    game_state = State()
    #main loop
    while game_state.running:
        game_state.curr_state.page_loop()
    pygame.quit()


def main():

    asset_id_path = os.path.join("Transactions","asset_id.txt")
    my_file = Path(asset_id_path)
    while not my_file.is_file():
        # if you have not created an asset yet then this creates the asset
        # YOU WILL NEED TO ACTIVATE YOUR WALLET BEFORE PLAYING THE GAME
        create_asa()
    # start the game.
    print("starting the game")
    start()




# run the main function only if this module is executed as the main script 
# if you import this as a module then nothing is executed.
if __name__=="__main__":
    main()
