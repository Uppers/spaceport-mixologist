import os
from Game.page import MenuPage, GamePage, GameOverPage, CreatePlayer
from Transactions.utility import Utility
from Transactions.private_info import player

class State():
    def __init__(self):
        self.running = True # the program is running
        self.account_info = Utility().read_json_from_file(os.path.join("Transactions","account_info.txt"))
        #self.username = "@tom_is_playing" # players username
        #self.player_pk = player
        self.score = 0
        self.create_player_state = CreatePlayer(self)
        self.menu_state = MenuPage(self)
        self.game_state = GamePage(self)
        self.game_over_state = GameOverPage(self)
        self.curr_state = self.menu_state

    