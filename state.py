from page import MenuPage, GamePage, GameOverPage

class State():
    def __init__(self):
        self.running = True # the program is running
        self.score = 0
        self.exploded = False 
        self.menu_state = MenuPage(self)
        self.game_state = GamePage(self)
        self.game_over_state = GameOverPage(self)
        self.curr_state = self.game_state #self.menu_state

    