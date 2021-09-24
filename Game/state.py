from Game.page import MenuPage, GamePage, GameOverPage
from Transactions.private_info import player

class State():
    def __init__(self):
        self.running = True # the program is running
        self.username = "@tom_is_playing" # players username
        self.player_pk = player
        self.score = 0
        self.menu_state = MenuPage(self)
        self.game_state = GamePage(self)
        self.game_over_state = GameOverPage(self)
        self.curr_state = self.menu_state

    