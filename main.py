from cocktail import GinAndTonic, VesperMartini
import pygame 
import cv2
import os
import random
from glass import Glass
from queue import Queue 
from button import Button
from ingredient import Gin, Ice, Tonic, Vermouth, Vodka
from interaction import Interaction
from display import Display
from customer_as_sprite import CustomerAsSprite
from earth import Earth

def main():

    # initialize the pygame module
    pygame.init()
    # caption 
    pygame.display.set_caption("SPACEPORT MIXOLOGIST")

    # get dimentions of background imagegit 
    image = cv2.imread(os.path.join("Assets","bar_template.png"))
    SCREEN_HEIGHT, SCREEN_WIDTH, IMAGE_TYPE = image.shape
    #create a surface that has the dimentions of the background image
    WIN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    #screen = pygame.display.set_mode((900, 500))
    background_image = pygame.image.load(os.path.join("Assets","bar_template.png"))

    #set up for fps
    clock = pygame.time.Clock()

    # these are the coordinates of the 3 spaces on a bar that a customer can appear
    #customer_coordinates = ((200, 150), (400, 150), (600, 150))

    # automatically initialise customers in their location on the bar
    #customer_queue = Queue(customer_coordinates)

    interaction = Interaction()

    display = Display()
    
    martini_glass_name = "Martini Glass"
    lowball_glass_name = "Lowball Glass"

    # instantiate glasses 
    martini_glass = Glass(martini_glass_name)
    lowball_glass = Glass(lowball_glass_name)

    # buttons for empty glasses
    martini_glass_button = Button(300,300, martini_glass.image)
    lowball_glass_button = Button(350, 300, lowball_glass.image)

    # this is how we can link the martini glass type with the buttons
    glasses = (martini_glass, lowball_glass)
    glass_buttons = {martini_glass_name:martini_glass_button, lowball_glass_name:lowball_glass_button}

    # used to find the correct image for the made cocktails  
    gin_and_tonic_ingredients = interaction.cocktail_ingredients_list(GinAndTonic())
    vesper_martini_ingredients = interaction.cocktail_ingredients_list(VesperMartini())
    cocktail_ingredients_map = {
        "Gin and Tonic": gin_and_tonic_ingredients,
        "Vesper Martini": vesper_martini_ingredients,
    }
    cocktail_name_map = {
        "Gin and Tonic": GinAndTonic(),
        "Vesper Martini": VesperMartini(),
    }

    # generate customers and give logic for when clicked
#    def populate_customers_and_logic(customer_queue):
#        # this bit of code generates customers and customer interactivity
#        for i in range(0, len(customer_queue.customer_list)):
#            current_customer = customer_queue.customer_list[i]
#            #current_customer = customer_as_sprite_group.sprites()[i]
#            if current_customer:
#                display.display_customer(current_customer, WIN)
#                print(current_customer.names)
#                if current_customer.switch: # if customer is toggled by player
#                    display.display_customer_order_as_text_button(current_customer, WIN)
#                    #print("on")
#                    if current_customer.clicked:
#                        interaction.place_customer_order(current_customer.order, i)
#                        #print("Click")

    # sprite groups
    customer_as_sprite_group = pygame.sprite.Group()
    earth_as_group = pygame.sprite.Group()

    earth = Earth(357, 1800)
    earth_as_group.add(earth)

    def create_customers_as_sprite():
    # generate customers as a sprite
        low_range = 12160
        high_range = 12220
        for row in range(100): # there are 100 rows
            low_range-=121 # each row has progressively less patience so that when the row appears at...
            high_range-=121 # ... the top of the screen it has the same amount of patience.
            for item in range(10):
                customer = CustomerAsSprite(150+item*50, -2960+row*30, round(random.uniform(low_range,high_range)), earth_as_group )
                customer_as_sprite_group.add(customer)
    
    create_customers_as_sprite()

    selected_customer = None 

    count_clicks = 0


    # define a variable to control the main loop
    running = True 

    #main loop
    while running:
        WIN.fill((255,255,255))
        WIN.blit(background_image,(0,0))

        earth_as_group.update()
        earth_as_group.draw(WIN)

        customer_as_sprite_group.update()
        customer_as_sprite_group.draw(WIN)

        pos = pygame.mouse.get_pos()
        for customer in customer_as_sprite_group:
            if customer.rect.collidepoint(pos):
                if pygame.mouse.get_pressed()[0] == 1 and count_clicks == 0:
                    count_clicks = 1 # to prevent multiple clicks
                    if customer == selected_customer:
                        selected_customer = None
                    else:
                        selected_customer = customer
                # mousebutton up allows for clicks again
                if pygame.mouse.get_pressed()[0] == 0:
                    count_clicks = 0

        
        # if a customer has been selected and not deleted then display their order
        if selected_customer and selected_customer in customer_as_sprite_group:
            display.display_customer_order_as_text_button(selected_customer, WIN)
            interaction.place_customer_order(selected_customer)
        else: # if a customer has been deleted from the group then they should no longer be selected.
            selected_customer = None
            #print(selected_customer)

        
        # Customer Interaction 
        #customer_queue.update_customer_list()

        # this bit of code checks for a customer who left because they werent served in time.
        # it then resets all the parameters associated with serving that customer.
        #interaction.customer_not_served_in_time(customer_queue)

        # this bit of code generates customers and customer interactivity
        #populate_customers_and_logic(customer_queue)

        # Available Ingredients
        gin_button = display.draw_ingredient_button(Gin(), 10, 300, WIN)
        vodka_button = display.draw_ingredient_button(Vodka(), 60, 300, WIN)
        vermouth_button = display.draw_ingredient_button(Vermouth(), 110, 300, WIN)
        tonic_button = display.draw_ingredient_button(Tonic(), 160, 300, WIN)
        ice_button = display.draw_ingredient_button(Ice(), 210, 300, WIN)

        ingredient_buttons = [gin_button, vodka_button, vermouth_button, tonic_button, ice_button]
        interaction.ingredient_button_clicked(ingredient_buttons) # if ingredient is clicked.

        # Available Glasses
        martini_glass_button.draw(WIN)
        lowball_glass_button.draw(WIN)

        interaction.glass_button_clicked(glasses, glass_buttons)
        
        # images of the cocktails that the user has made.
        list_of_drinks_images = interaction.convert_made_coctails_to_images(cocktail_ingredients_map, cocktail_name_map, interaction.drinks_created)
        
        # show drinks created by player
        display.display_drinks_created(list_of_drinks_images, WIN)

        # has the order been satisfied? if so then:..
        #interaction.order_satisfied(customer_queue)
        interaction.order_satisfied()

        # print the total on the page
        display.display_score(interaction.money_made, WIN) 

        # event handling, gets all event from the event queue
        for event in pygame.event.get():
            # only do something if the event is of type QUIT
            if event.type == pygame.QUIT:
                #change the value to False, to exit the main loop
                running = False
            if event.type == pygame.MOUSEBUTTONUP:
                interaction.add_ingredient = dict.fromkeys(interaction.add_ingredient, True) # sets all values to true 

        pygame.display.update()
        # fps
        clock.tick(30)
        
    pygame.quit()

# run the main function only if this module is executed as the main script 
# if you import this as a module then nothing is executed.
if __name__=="__main__":
    main()