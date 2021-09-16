from page import MenuPage, GamePage

class State():
    def __init__(self):
        self.running = True # the program is running
        self.score = 0 
        self.menu_state = MenuPage(self)
        self.game_state = GamePage(self)
        self.curr_state = self.menu_state

    