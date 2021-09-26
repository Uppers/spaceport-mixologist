import pygame 
import cv2
import os
import random
import datetime
from Game.glass import Glass
from Game.button import Button, TextButton
from Game.ingredient import Gin, Ice, Tonic, Vermouth, Vodka
from Game.cocktail import GinAndTonic, VesperMartini
from Game.customer_as_sprite import CustomerAsSprite
from Game.earth import Earth
from Game.interaction import Interaction
from Game.display import Display
from Game.textbox import Textbox
from Transactions.transaction import Transaction, QueryTransaction
from Transactions.utility import Utility
from Transactions.private_info import account1_mnemonic
from Transactions.queries import Queries



class Page():
    """ The class that provides the template for how pages operate """
    def __init__(self, state_obj):
        # get dimentions of background imagegit 
        self.image = cv2.imread(os.path.join("Assets","bar_template.png"))
        self.SCREEN_HEIGHT, self.SCREEN_WIDTH, self.IMAGE_TYPE = self.image.shape
        #create a surface that has the dimentions of the background image
        self.WIN = pygame.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT))   
        #screen = pygame.display.set_mode((900, 500))
        self.background_image = pygame.image.load(os.path.join("Assets","bar_template.png"))
        #set up for fps
        self.clock = pygame.time.Clock()
        # to determine if the page should be shown and the while loop should be running
        self.running = True
        self.state = state_obj
        

    def page_loop(self):
        while self.running:
            # do something 
            pass

class CreatePlayer(Page):
    """ This is the page where you add the public address of your account """
    def __init__(self, state_obj):
        super().__init__(state_obj)
        self.font = os.path.join("Assets", "fonts","8-BIT WONDER.TTF")
        self.public_key_box = Textbox(int(self.SCREEN_WIDTH/2)-300, int(self.SCREEN_HEIGHT/2),600, 50, 10, 58, "YOUR PUBLIC KEY", is_uppercase= True) 
        self.ig_handle_box = Textbox(int(self.SCREEN_WIDTH/2)-300, int(self.SCREEN_HEIGHT/2)+100,(600/58)*20, 50, 10, 20, "IG HANDLE / USERNAME") 
        self.submit_button = TextButton(self.SCREEN_WIDTH-200, int(self.SCREEN_HEIGHT/2)+100, "SUBMIT", font_colour= pygame.Color("Grey"), background_colour= pygame.Color("Black"), font_size=20)
        self.public_key_box.active = True
        self._queries = Queries()
        self._utility = Utility()
        #self._transactions = Transaction(sender_pk, sender_sk, recipient_pk)
        self.account_details = self._utility.account_details(account1_mnemonic)
        self.transaction = QueryTransaction(self.account_details['pk'], self.account_details['sk'])
        self._account_doesnt_exist_flag = True # True if account does not exist
        self._account_not_opted_in_flag = True # True if account is not opted in
        self._submit_button_flag = False # True if the Submit button has been pressed

    def page_loop(self):
        self.running = True
        while self.running:
             # the background
            self.WIN.fill((255,255,255))
            self.WIN.blit(self.background_image,(0,0))

            # TEXT
            title = TextButton(int(self.SCREEN_WIDTH/2)-300, int(self.SCREEN_HEIGHT/2)-100, "ENTER DETAILS", font_size = 30, font_colour=pygame.Color("White"), background_colour=pygame.Color("Black"))
            title.draw(self.WIN)

            # Add public key
            self.public_key_box.write_text(self.WIN)
            self.public_key_box.draw_box(self.WIN)

            # Add IG Handle / Username
            self.ig_handle_box.write_text(self.WIN)
            self.ig_handle_box.draw_box(self.WIN)

            # Add TextButton for submitting data
            
            if len(self.public_key_box.player_input)==58 and len(self.ig_handle_box.player_input)>0: # button is clickable when there are valid inputs
                self.submit_button.change_colour(colour=pygame.Color("Gold")) # when button is clickable the colour changes
                self.submit_button.draw(self.WIN)
                if self.submit_button.clicked:
                    # player has clicked the submit button
                    #transactions = Transaction(self.account_details['pk'], self.account_details['sk'], self.public_key_box.player_input) # get ready to test opt in status
                    self._submit_button_flag = True
                    if self._queries.account_exists(self.public_key_box.player_input): # if account exists
                        # you get to this point if the account exists 
                        self._account_doesnt_exist_flag = False
                    else:
                        # you get here if the account does not exist
                        self._account_doesnt_exist_flag = True
                    #if self._queries.account_opted_in(self.public_key_box.player_input, self._utilities.read_from_file(os.path.join("Transactions","asset_id.txt"))):
                    if self.transaction.is_opted_in(self.public_key_box.player_input):
                        # you get here if the account is opted in
                        self._account_not_opted_in_flag = False
                    else:
                        # you get here if the account is not opted in
                        self._account_not_opted_in_flag = True
                        
                    
            else:
                # the submit button cannot be pressed if essential data is missing
                self.submit_button.change_colour(colour=pygame.Color("Grey"))
                self.submit_button.draw(self.WIN)
                # if the player is editing data then warning messages should be reset
                self._account_doesnt_exist_flag = True
                self._account_not_opted_in_flag = True
                self._submit_button_flag = False

            
            if self._submit_button_flag and self._account_doesnt_exist_flag:
                warning = TextButton(int(self.SCREEN_WIDTH/2)-300, int(self.SCREEN_HEIGHT/2)+55, "Account Does not Exist", font_size = 10, font_colour=pygame.Color("Red"), background_colour=pygame.Color("Black"))
                warning.draw(self.WIN)
            elif self._submit_button_flag and self._account_not_opted_in_flag:
                not_opted_in_warning = TextButton(int(self.SCREEN_WIDTH/2)-300, int(self.SCREEN_HEIGHT/2)+55, "First You Need to Opt-in Your Account", font_size = 10, font_colour=pygame.Color("Red"), background_colour=pygame.Color("Black"))
                not_opted_in_warning.draw(self.WIN)
            elif self._submit_button_flag and self._account_doesnt_exist_flag == False and self._account_not_opted_in_flag == False:
                # save the account details and re-route to the main menu
                print("account details saved")




            # event handling, gets all event from the event queue
            for event in pygame.event.get():
                # only do something if the event is of type QUIT
                if event.type == pygame.QUIT:
                    #change the value to False, to exit the main loop
                    self.running = False
                    self.state.running = False

            #update the screen 
            pygame.display.update()
            # fps
            self.clock.tick(30)
        


class GameOverPage(Page):
    """ Only go here after the game ends """
    def __init__(self, state_obj):
        super().__init__(state_obj)
        self.earth_image = pygame.image.load(os.path.join("Assets","the_earth.png"))
        self.page_header_font = pygame.font.Font(os.path.join("Assets", "fonts","8-BIT WONDER.TTF"), 30)
        self.table_header_font = pygame.font.Font(os.path.join("Assets", "fonts","8-BIT WONDER.TTF"), 20)
        self.content_font = pygame.font.Font(os.path.join("Assets", "fonts","8-BIT WONDER.TTF"), 10)
        self.header_text = self.page_header_font.render('HIGH SCORES', True, pygame.Color("White"), pygame.Color("Black"))
        self.rank_header_text = self.table_header_font.render('Rank', True, pygame.Color("White"), pygame.Color("Black"))
        self.name_header_text = self.table_header_font.render('IG Handle', True, pygame.Color("White"), pygame.Color("Black"))
        self.score_header_text = self.table_header_font.render('Score', True, pygame.Color("White"), pygame.Color("Black"))
        self.header_text_rect = self.header_text.get_rect()
        self.rank_header_text_rect = self.rank_header_text.get_rect()
        self.name_header_text_rect = self.name_header_text.get_rect()
        self.score_header_text_rect = self.score_header_text.get_rect()
        self.header_text_rect.center = (int(self.SCREEN_WIDTH/2), int(self.SCREEN_HEIGHT*(1/3))-50) # placing the header on screen
        self.rank_column_x = int(self.SCREEN_WIDTH/2)-150
        self.name_column_x = int(self.SCREEN_WIDTH/2)
        self.score_column_x = int(self.SCREEN_WIDTH/2)+150
        self.table_header_row_y = int(self.SCREEN_HEIGHT*(1/3))
        self.rank_header_text_rect.center = (self.rank_column_x, self.table_header_row_y)
        self.name_header_text_rect.center = (self.name_column_x, self.table_header_row_y)
        self.score_header_text_rect.center = (self.score_column_x, self.table_header_row_y)
        self.high_scores = (
            (1, "@pretty_girl", 10001), 
            (2, "@gym_bro", 9999), 
            (3, "@top_influencer", 8765),
            (4, "@hanny_loves_oranges", 6092),
            (5, "@peanut_enjoyer", 5432),
            ) # these are fictional high scores to add to the high scores page. 

    def high_score_text_generator(self):
        column_x = (self.rank_column_x, self.name_column_x, self.score_column_x) # placed in array so they can be looped through
        for r in range(0,len(self.high_scores)):
            for c in range(0, len(self.high_scores[r])):
                item = self.high_scores[r][c] # unpack the high score data
                text = self.content_font.render(str(item), True, pygame.Color("White"), pygame.Color("Black"))
                rect = text.get_rect()
                rect.center = (column_x[c], self.table_header_row_y+30*(r+1))
                self.WIN.blit(text, rect)

    def your_score_text_generator(self):
        data = (11, "Your score:", self.state.score)
        column_x = (self.rank_column_x, self.name_column_x, self.score_column_x)
        for c in range(0,len(data)):
            text = self.content_font.render(str(data[c]), True, pygame.Color("Gold"), pygame.Color("Black"))
            rect = text.get_rect()
            rect.center = (column_x[c], self.table_header_row_y+180)
            self.WIN.blit(text, rect)

    def page_loop(self):
        self.running = True
        while self.running:
            # the background
            self.WIN.fill((255,255,255))
            self.WIN.blit(self.background_image,(0,0))
            
            # the earth as an image rather than a sprite
            self.WIN.blit(self.earth_image, (357, 1800))

            # blit the header to screen
            self.WIN.blit(self.header_text, self.header_text_rect) # HIGH SCORES
            self.WIN.blit(self.rank_header_text, self.rank_header_text_rect) # Rank
            self.WIN.blit(self.name_header_text, self.name_header_text_rect) # IG Handle
            self.WIN.blit(self.score_header_text, self.score_header_text_rect) # Score
            self.high_score_text_generator()
            self.your_score_text_generator()


            # event handling, gets all event from the event queue
            for event in pygame.event.get():
                # only do something if the event is of type QUIT
                if event.type == pygame.QUIT:
                    #change the value to False, to exit the main loop
                    self.running = False
                    self.state.running = False
            #update the screen 
            pygame.display.update()
            # fps
            self.clock.tick(30)


class MenuPage(Page):
    def __init__(self, state_obj):
        super().__init__(state_obj)
        self.font = os.path.join("Assets", "fonts","8-BIT WONDER.TTF")
        self.is_pressed = False


    def page_loop(self):
        self.running = True
        while self.running:
            # the background
            self.WIN.fill((255,255,255))
            self.WIN.blit(self.background_image,(0,0))

            # TEXT
            title = TextButton(int(self.SCREEN_WIDTH/2)-300, int(self.SCREEN_HEIGHT/2)-100, "SPACEPORT MIXOLOGIST", font_size = 30, font_colour=pygame.Color("White"), background_colour=pygame.Color("Black"))
            title.draw(self.WIN)

            if self.is_pressed:
                # if the START GAME button is pressed, if there is a delay in switching to the game play page  
                play_game_button = TextButton(int(self.SCREEN_WIDTH/2)-100, int(self.SCREEN_HEIGHT/2), "LOADING...", font_size=20, font_colour=pygame.Color("White"), background_colour=pygame.Color("Black"))
                play_game_button.draw(self.WIN)
                self.state.curr_state = self.state.game_state # if the start game button is pressed
                self.running = False 
            else:
                play_game_button = TextButton(int(self.SCREEN_WIDTH/2)-100, int(self.SCREEN_HEIGHT/2), "START GAME", font_size=20, font_colour=pygame.Color("White"), background_colour=pygame.Color("Black"))
                play_game_button.draw(self.WIN)

            create_player_button = TextButton(int(self.SCREEN_WIDTH/2)-130, int(self.SCREEN_HEIGHT/2)+50, "CREATE PLAYER", font_size=20, font_colour=pygame.Color("White"), background_colour=pygame.Color("Black"))
            create_player_button.draw(self.WIN)
            
            if play_game_button.switch:
                self.is_pressed = True

            if create_player_button.switch:
                self.state.curr_state = self.state.create_player_state # if the start game button is pressed
                self.running = False 
            


            # event handling, gets all event from the event queue
            for event in pygame.event.get():
                # only do something if the event is of type QUIT
                if event.type == pygame.QUIT:
                    #change the value to False, to exit the main loop
                    #self.state.curr_state = self.state.game_state
                    self.running = False
                    self.state.running = False
            pygame.display.update()
            # fps
            self.clock.tick(30)
                    


 


class GamePage(Page):
    def __init__(self, state_obj):
        super().__init__(state_obj)
        self.martini_glass_name = "Martini Glass"
        self.lowball_glass_name = "Lowball Glass"
        self.martini_glass = Glass(self.martini_glass_name)
        self.lowball_glass = Glass(self.lowball_glass_name)
        self.martini_glass_button = Button(300,300, self.martini_glass.image)
        self.lowball_glass_button = Button(350, 300, self.lowball_glass.image)
        self.glasses = (self.martini_glass, self.lowball_glass)
        self.glass_buttons = {self.martini_glass_name:self.martini_glass_button, self.lowball_glass_name:self.lowball_glass_button}
        self.interaction = Interaction()
        self.display = Display()
        # used to find the correct image for the made cocktails  
        self.gin_and_tonic_ingredients = self.interaction.cocktail_ingredients_list(GinAndTonic())
        self.vesper_martini_ingredients = self.interaction.cocktail_ingredients_list(VesperMartini())
        # sprite groups
        self.customer_as_sprite_group = pygame.sprite.Group()
        self.earth_as_group = pygame.sprite.Group()
        self.earth = Earth(357, 1800)
        self.earth_as_group.add(self.earth)
        self.selected_customer = None 
        self.count_clicks = 0
        self.count_loops = 0
        self.running = False
        self.explosion_timestamp = None
        self.cocktail_ingredients_map = {
            "Gin and Tonic": self.gin_and_tonic_ingredients,
            "Vesper Martini": self.vesper_martini_ingredients,
            }
        self.cocktail_name_map = {
            "Gin and Tonic": GinAndTonic(),
            "Vesper Martini": VesperMartini(),
        }
        self.game_start_timestamp = datetime.datetime.now()
        self.utility = Utility()
        self.account_details = self.utility.account_details(account1_mnemonic)
        self.transactions = Transaction(self.account_details['pk'], self.account_details['sk'], self.state.player_pk)


    def create_customers_as_sprite(self):
    # generate customers as a sprite
        low_range = 12160
        high_range = 12220
        for row in range(100): # there are 100 rows
            low_range-=121 # each row has progressively less patience so that when the row appears at...
            high_range-=121 # ... the top of the screen it has the same amount of patience.
            for item in range(10):
                customer = CustomerAsSprite(150+item*50, -2960+row*30, round(random.uniform(low_range,high_range)), self.earth_as_group, self.state)
                self.customer_as_sprite_group.add(customer)

    def checkCollision(self, customer_sprite, earth_sprite):
        # checks if the earth has been destroyed by a collision with customer
        # https://stackoverflow.com/questions/16227616/how-to-use-sprite-collide-in-pygame
        col = pygame.sprite.collide_rect(customer_sprite, earth_sprite)
        if col == True and self.explosion_timestamp==None:
            self.explosion_timestamp = datetime.datetime.now()


    def page_loop(self):
        self.running = True
        while self.running:
            if self.count_loops == 0: # customers only get created on first iteration of while loop
                self.count_loops += 1
                self.create_customers_as_sprite() # creates the customers in the game and adds them to the customer_as_sprite_group

            self.WIN.fill((255,255,255))
            self.WIN.blit(self.background_image,(0,0))

            self.earth_as_group.update()
            self.earth_as_group.draw(self.WIN)

            self.customer_as_sprite_group.update()
            self.customer_as_sprite_group.draw(self.WIN)


            pos = pygame.mouse.get_pos()
            for customer in self.customer_as_sprite_group:
                self.interaction.customer_obj = customer
                if self.explosion_timestamp is None: # checks that there has not already been a collision between customer and earth
                    self.checkCollision(customer, self.earth) # check if a collision has happened and set the timestamp.
                # get the order from the customer you clicked on.
                if customer.rect.collidepoint(pos) and customer.mood != "attack":
                    if pygame.mouse.get_pressed()[0] == 1 and self.count_clicks == 0:
                        self.count_clicks = 1 # to prevent multiple clicks
                        if customer == self.selected_customer:
                            self.selected_customer = None
                        else:
                            self.selected_customer = customer
                    # mousebutton up allows for clicks again
                    if pygame.mouse.get_pressed()[0] == 0:
                        self.count_clicks = 0
                # clicking on attacking customer to destroy them before they hit earth
                if customer.rect.collidepoint(pos) and customer.mood == "attack":
                    if pygame.mouse.get_pressed()[0] == 1:
                        if customer == self.selected_customer: # if this is the customer you are currently serving
                            self.interaction.customer_not_served_in_time()
                            customer.attacking_customer_destroyed = True
                            self.selected_customer = None 
                        else: # if not the customer you are currently serving
                            customer.attacking_customer_destroyed = True

            
            # if a customer has been selected and not deleted then display their order
            if self.selected_customer and self.selected_customer in self.customer_as_sprite_group:
                self.display.display_customer_order_as_text_button(self.selected_customer, self.WIN)
                self.interaction.place_customer_order(self.selected_customer)
            else: # if a customer has been deleted from the group then they should no longer be selected.
                self.selected_customer = None

            # Available Ingredients
            gin_button = self.display.draw_ingredient_button(Gin(), 10, 300, self.WIN)
            vodka_button = self.display.draw_ingredient_button(Vodka(), 60, 300, self.WIN)
            vermouth_button = self.display.draw_ingredient_button(Vermouth(), 110, 300, self.WIN)
            tonic_button = self.display.draw_ingredient_button(Tonic(), 160, 300, self.WIN)
            ice_button = self.display.draw_ingredient_button(Ice(), 210, 300, self.WIN)

            ingredient_buttons = [gin_button, vodka_button, vermouth_button, tonic_button, ice_button]
            self.interaction.ingredient_button_clicked(ingredient_buttons) # if ingredient is clicked.

            # Available Glasses
            self.martini_glass_button.draw(self.WIN)
            self.lowball_glass_button.draw(self.WIN)

            self.interaction.glass_button_clicked(self.glasses, self.glass_buttons)
            
            # images of the cocktails that the user has made.
            list_of_drinks_images = self.interaction.convert_made_coctails_to_images(self.cocktail_ingredients_map, self.cocktail_name_map, self.interaction.drinks_created)
            
            # show drinks created by player
            self.display.display_drinks_created(list_of_drinks_images, self.WIN)

            # has the order been satisfied? if so then:..
            #interaction.order_satisfied(customer_queue)
            if self.interaction.order_satisfied():
                self.transactions.send_transaction(self.interaction.revenue_from_most_recent, self.game_start_timestamp)

            # print the total on the page
            self.display.display_score(self.interaction.money_made, self.WIN) 

            # update the state with the score
            self.state.score = self.interaction.money_made

            # this is needed in order to give time for the explosion animation to happen when customer hits earth.
            time_delta = self.interaction.seconds_difference(self.explosion_timestamp, datetime.datetime.now())
            if time_delta is not None:
                if time_delta>1:
                    self.state.curr_state = self.state.game_over_state
                    self.running = False

            # event handling, gets all event from the event queue
            for event in pygame.event.get():
                # only do something if the event is of type QUIT
                if event.type == pygame.QUIT:
                    #change the value to False, to exit the main loop
                    self.running = False
                    self.state.running = False
                if event.type == pygame.MOUSEBUTTONUP:
                    self.interaction.add_ingredient = dict.fromkeys(self.interaction.add_ingredient, True) # sets all values to true 

            pygame.display.update()
            # fps
            self.clock.tick(30)
    

