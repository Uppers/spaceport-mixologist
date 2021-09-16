import pygame 
import cv2
import os
import random
from glass import Glass
from button import Button, TextButton
from ingredient import Gin, Ice, Tonic, Vermouth, Vodka
from cocktail import GinAndTonic, VesperMartini
from customer_as_sprite import CustomerAsSprite
from earth import Earth
from interaction import Interaction
from display import Display


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

class GameOver(Page):
    def __init__(self, state_obj):
        super().__init__(state_obj)
        pass

class MenuPage(Page):
    def __init__(self, state_obj):
        super().__init__(state_obj)
        self.font = os.path.join("Assets", "fonts","8-BIT WONDER.TTF")


    def page_loop(self):
        self.running = True
        while self.running:
            # the background
            self.WIN.fill((255,255,255))
            self.WIN.blit(self.background_image,(0,0))

            #print(self.background_image)

            # TEXT
            title = TextButton(int(self.SCREEN_WIDTH/2)-300, int(self.SCREEN_HEIGHT/2)-100, "SPACEPORT MIXOLOGIST", font_size = 30, font_colour=pygame.Color("White"), background_colour=pygame.Color("Black"))
            play_game_button = TextButton(int(self.SCREEN_WIDTH/2)-100, int(self.SCREEN_HEIGHT/2), "START GAME", font_size=20, font_colour=pygame.Color("White"), background_colour=pygame.Color("Black"))
            
            
            title.draw(self.WIN)
            play_game_button.draw(self.WIN)
            

            if play_game_button.switch:
                self.state.curr_state = self.state.game_state # if the start game button is pressed
                self.running = False 

            # the coordinates of the mouse
            #pos = pygame.mouse.get_pos()

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
        self.cocktail_ingredients_map = {
            "Gin and Tonic": self.gin_and_tonic_ingredients,
            "Vesper Martini": self.vesper_martini_ingredients,
            }
        self.cocktail_name_map = {
            "Gin and Tonic": GinAndTonic(),
            "Vesper Martini": VesperMartini(),
        }


    def create_customers_as_sprite(self):
    # generate customers as a sprite
        low_range = 12160
        high_range = 12220
        for row in range(100): # there are 100 rows
            low_range-=121 # each row has progressively less patience so that when the row appears at...
            high_range-=121 # ... the top of the screen it has the same amount of patience.
            for item in range(10):
                customer = CustomerAsSprite(150+item*50, -2960+row*30, round(random.uniform(low_range,high_range)), self.earth_as_group )
                self.customer_as_sprite_group.add(customer)

    
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
                        if customer == self.selected_customer:
                            self.interaction.customer_not_served_in_time()
                            customer.attacking_customer_destroyed = True
                            self.selected_customer = None 
                        else:
                            #self.interaction.customer_not_served_in_time()
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
            self.interaction.order_satisfied()

            # print the total on the page
            self.display.display_score(self.interaction.money_made, self.WIN) 

            # update the state with the score
            self.state.score = self.interaction.money_made

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
    

