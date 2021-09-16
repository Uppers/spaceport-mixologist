import pygame 
from state import State
from page import GamePage, MenuPage

def main():

    # initialize the pygame module
    pygame.init()
    # caption 
    pygame.display.set_caption("SPACEPORT MIXOLOGIST")

    game_state = State()

    #main loop
    while game_state.running:
       game_state.curr_state.page_loop()


    pygame.quit()

# run the main function only if this module is executed as the main script 
# if you import this as a module then nothing is executed.
if __name__=="__main__":
    main()
