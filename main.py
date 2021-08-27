from cocktail import GinAndTonic, VesperMartini
import pygame 
import cv2
import os
from glass import Glass
from queue import Queue 
from button import Button, TextButton 
from ingredient import Gin, Ice, Tonic, Vermouth, Vodka
from interaction import Interaction

def main():

    # initialize the pygame module
    pygame.init()
    # caption 
    pygame.display.set_caption("BarFly")

    # get dimentions of background image
    image = cv2.imread(os.path.join("Assets","bar_template.png"))
    SCREEN_HEIGHT, SCREEN_WIDTH, IMAGE_TYPE = image.shape
    #create a surface that has the dimentions of the background image
    WIN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    #screen = pygame.display.set_mode((900, 500))
    background_image = pygame.image.load(os.path.join("Assets","bar_template.png"))

    #set up for fps
    clock = pygame.time.Clock()

    # these are the coordinates of the 3 spaces on a bar that a customer can appear
    customer_coordinates = ((200, 150), (400, 150), (600, 150))

    # automatically initialise customers in their location on the bar
    customer_queue = Queue(customer_coordinates)

    interaction = Interaction()
    
    martini_glass_name = "Martini Glass"
    lowball_glass_name = "Lowball Glass"

    # instantiate glasses 
    martini_glass = Glass(martini_glass_name)
    lowball_glass = Glass(lowball_glass_name)

    # buttons for empty glasses
    martini_glass_button = Button(300,300, martini_glass.image)
    lowball_glass_button = Button(350, 300, lowball_glass.image)

    # this is how we can link the martini glass type with the buttons
    glasses = [martini_glass, lowball_glass]
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

    def display_drinks_created(drinks_created, screen):
        list_of_drinks_images = interaction.convert_made_coctails_to_images(cocktail_ingredients_map, cocktail_name_map, drinks_created)
        x_axis = 390
        for image in list_of_drinks_images:
            x_axis += 50
            drink_button = Button(x_axis,300, image)
            drink_button.draw(screen)

    def display_score(money_made, screen): # displays amount of money the player has made on screen
        total_amount_spent = TextButton(650,270, str(money_made))
        total_amount_spent.draw(screen)

    # makes the buttons for the ingredients such as ice, vodka etc.
    def draw_ingredient_button(drink_obj, x, y, screen):
        button = Button(x,y, drink_obj.image)
        button.draw(screen)
        return {"name": drink_obj.name, "button": button}

    def display_customer_order_as_text_button(current_customer, screen):
        # (when customer is toggled) the customer order is displayed
        text = TextButton(10,10, current_customer.order_for_display)
        text.draw(screen)

    def display_customer(current_customer, screen):
        # displays the customers on screen
        current_customer.update_customer_status()
        current_customer.draw(screen)

    # generate customers and give logic for when clicked
    def populate_customers_and_logic(customer_queue):
        # this bit of code generates customers and customer interactivity
        for i in range(0, len(customer_queue.customer_list)):
            current_customer = customer_queue.customer_list[i]
            if current_customer:
                display_customer(current_customer, WIN)
                if current_customer.switch: # if customer is toggled by player
                    display_customer_order_as_text_button(current_customer, WIN)
                    if current_customer.clicked:
                        interaction.place_customer_order(current_customer.order, i)

    # define a variable to control the main loop
    running = True 

    #main loop
    while running:
        WIN.fill((255,255,255))
        WIN.blit(background_image,(0,0))
        
        # Customer Interaction 
        customer_queue.update_customer_list()

        # this bit of code checks for a customer who left because they werent served in time.
        # it then resets all the parameters associated with serving that customer.
        interaction.customer_not_served_in_time(customer_queue)

        # this bit of code generates customers and customer interactivity
        populate_customers_and_logic(customer_queue)

        # Available Ingredients
        gin_button = draw_ingredient_button(Gin(), 10, 300, WIN)
        vodka_button = draw_ingredient_button(Vodka(), 60, 300, WIN)
        vermouth_button = draw_ingredient_button(Vermouth(), 110, 300, WIN)
        tonic_button = draw_ingredient_button(Tonic(), 160, 300, WIN)
        ice_button = draw_ingredient_button(Ice(), 210, 300, WIN)

        ingredient_buttons = [gin_button, vodka_button, vermouth_button, tonic_button, ice_button]
        interaction.ingredient_button_clicked(ingredient_buttons) # if ingredient is clicked.

        # Available Glasses
        martini_glass_button.draw(WIN)
        lowball_glass_button.draw(WIN)

        interaction.glass_button_clicked(glasses, glass_buttons)
        
        #show drinks created by player
        display_drinks_created(interaction.drinks_created, WIN)

        # has the order been satisfied? if so then:..
        interaction.order_satisfied(customer_queue)

        # print the total on the page
        display_score(interaction.money_made, WIN) 

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