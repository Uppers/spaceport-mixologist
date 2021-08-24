
from cocktail import GinAndTonic, VesperMartini
from order import Order
import pygame 
import cv2
import os
from glass import Glass
from queue import Queue 
from button import Button, TextButton 
from ingredient import Gin, Ice, Tonic, Vermouth, Vodka





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
    #text = Text("hello", 10,10)

    # Add more of the same. This allows you to click an ingredient once.
    add_ingredient = {
        "Gin":True,
        "Vodka":True,
        "Vermouth":True,
        "Tonic":True,
        "Ice":True,
    }


    # instantiate glasses 
    martini_glass = Glass("Martini Glass")
    lowball_glass = Glass("Lowball Glass")

    # buttons for empty glasses
    martini_glass_button = Button(300,300, martini_glass.image)
    lowball_glass_button = Button(350, 300, lowball_glass.image)

    # ensuring you can only click a glass once
    glass_clickable = {
        "Martini Glass": True,
        "Lowball Glass": True,
    }

    # customer drinks order
    customer_order = []
    
    # drink currently being created
    drink_created = []

    # drinks created in this order
    drinks_created = []

    # queue number of the customer
    customer_queue_number = None

    # how much money the barman has made
    money_made = 0

    def create_customer_drinks_order(drinks_order):
        order = []
        for drink in drinks_order:
            drink_ingredients = []
            for ingredient in drink.drink_ingredients:
                drink_ingredients.append(ingredient.name)
            order.append(drink_ingredients)
        return order

    def is_in_orderlist(drink_ingredients, customer_order): # checks if drink created is in customer order
        for order in customer_order:
            if sorted(order) == sorted(drink_ingredients):
                return True

    def count_instances_in_list(instance, two_d_list):
        # where instance is a list and two_d_list is a list of lists. 
        number_of_instances = 0 
        for item in two_d_list:
            if sorted(instance) == sorted(item):
                number_of_instances+=1
        return number_of_instances

    def is_not_surplus(drink_ingredients, drinks_created, drinks_order): 
        # checks if enough of that drink has already been made
        # counts how many of that drink_ingredients in drinks_order
        # counts how many of that drink_ingredients in drinks created
        # if count_drinks_order > count_drinks_created for that drink_ingredients then True (no surplus)
        count_drinks_created = count_instances_in_list(drink_ingredients, drinks_created)
        count_drinks_order = count_instances_in_list(drink_ingredients, drinks_order)
        if count_drinks_order> count_drinks_created:
            return True
        else:
            False


    def is_valid(drink_ingredients, drinks_created, drinks_order): 
        #checks if drink should be added to drinks_created
        if is_in_orderlist(drink_ingredients, drinks_order) and is_not_surplus(drink_ingredients, drinks_created, drinks_order):
            return True 
        else:
            False

    def cocktail_ingredients_list(cocktail_object):
        ingredients = []
        cocktail_ingredients_obj = cocktail_object.drink_ingredients
        for ingredient_obj in cocktail_ingredients_obj:
            ingredient_name = ingredient_obj.name
            ingredients.append(ingredient_name)
        return sorted(ingredients)

    # used to find the correct image for the made cocktails  
    gin_and_tonic_ingredients = cocktail_ingredients_list(GinAndTonic())
    vesper_martini_ingredients = cocktail_ingredients_list(VesperMartini())
    cocktail_ingredients_map = {
        "Gin and Tonic": gin_and_tonic_ingredients,
        "Vesper Martini": vesper_martini_ingredients,
    }
    cocktail_name_map = {
        "Gin and Tonic": GinAndTonic(),
        "Vesper Martini": VesperMartini(),
    }
    
    def convert_ingredients_to_image(list_of_ingredients):
        for key, value in cocktail_ingredients_map.items():
            if sorted(value) == sorted(list_of_ingredients):
                image = cocktail_name_map[key].get_image()
                return image

    def convert_made_coctails_to_images(list_of_cocktail_ingredients):
        images = []
        for list_of_ingredients in list_of_cocktail_ingredients:
            images.append(convert_ingredients_to_image(list_of_ingredients))
        return images

    # used to check the customer has recieved their order
    # compares the cocktails made by the barista 
    def is_same_2d_lists(twodlist1, twodlist2):
        if twodlist1 is not None and twodlist2 is not None and len(twodlist1)>0 and len(twodlist2)>0:
            if len(twodlist1) == len(twodlist2):
                twodlist1 = sort_2d_list(twodlist1)
                twodlist2 = sort_2d_list(twodlist2)
                if twodlist1 == twodlist2:
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False

    
    def sort_2d_list(twodlist):
        twodlist = twodlist.sort()
        sortedtwodlist = []
        if twodlist is not None:
            for list in twodlist:
                sortedtwodlist.append(list.sort())
            return sortedtwodlist




    # define a variable to control the main loop
    running = True 

    #main loop
    while running:
        WIN.fill((255,255,255))
        WIN.blit(background_image,(0,0))
        
        # Customer Interaction 
        customer_queue.update_customer_list()
        for i in range(0, len(customer_queue.customer_list)):
            current_customer = customer_queue.customer_list[i]
            if current_customer:
                current_customer.update_customer_status()
                current_customer.draw(WIN)
                if current_customer.switch:
                    text = TextButton(10,10, current_customer.order_for_display)
                    text.draw(WIN)
                    if current_customer.clicked:
                        customer_order = create_customer_drinks_order(current_customer.order)
                        customer_queue_number = i
                    if text.clicked:
                        print("clicked")

        # Available Drinks 
        gin = Gin()
        gin_button = Button(10,300, gin.image)
        gin_button.draw(WIN)
        vodka = Vodka()
        vodka_button = Button(60,300, vodka.image)
        vodka_button.draw(WIN)
        vermouth = Vermouth()
        vermouth_button = Button(110,300, vermouth.image)
        vermouth_button.draw(WIN)
        tonic = Tonic()
        tonic_button = Button(160,300, tonic.image)
        tonic_button.draw(WIN)
        ice = Ice()
        ice_button = Button(210,300, ice.image)
        ice_button.draw(WIN)

        # drinks are clicked
        if gin_button.switch and add_ingredient["Gin"]:
            drink_created.append(gin.name) # add gin.
            add_ingredient["Gin"] = False # drink can only be selected once (see event loop for more details).
            # either glass can now be selected
            glass_clickable["Lowball Glass"] = True
            glass_clickable["Martini Glass"] = True
        if vodka_button.switch and add_ingredient["Vodka"]:
            drink_created.append(vodka.name) # add vodka
            add_ingredient["Vodka"] = False
            glass_clickable["Lowball Glass"] = True
            glass_clickable["Martini Glass"] = True
        if vermouth_button.switch and add_ingredient["Vermouth"]:
            drink_created.append(vermouth.name) # add vermouth
            add_ingredient["Vermouth"] = False
            glass_clickable["Lowball Glass"] = True
            glass_clickable["Martini Glass"] = True
        if tonic_button.switch and add_ingredient["Tonic"]:
            drink_created.append(tonic.name) # add tonic
            add_ingredient["Tonic"] = False
            glass_clickable["Lowball Glass"] = True
            glass_clickable["Martini Glass"] = True
        if ice_button.switch and add_ingredient["Ice"]:
            drink_created.append(ice.name) # add ice
            add_ingredient["Ice"] = False
            glass_clickable["Lowball Glass"] = True
            glass_clickable["Martini Glass"] = True

        # Available Glasses
        martini_glass_button.draw(WIN)
        lowball_glass_button.draw(WIN)

        
        # empty glasses can be selected. 
        if martini_glass_button.switch and glass_clickable["Martini Glass"] and glass_clickable["Lowball Glass"]:
            if is_valid(drink_created, drinks_created, customer_order): # check the drink is something the customer ordered.
                drinks_created.append(drink_created) # add it to the customer's tray
                drink_created=[] # make way for the creation of a new drink
                print(f"drink created: {drink_created}")
                print(f"drinks created: {drinks_created}")
                print(f"customer order: {customer_order}")
            else:
                print(f"this is not valid: {drink_created}")
                drink_created = []
            martini_glass.selected = True
            glass_clickable["Martini Glass"] = False
            martini_glass_button.switch = False
        elif martini_glass_button.switch and glass_clickable["Martini Glass"] and glass_clickable["Lowball Glass"]==False:
            if is_valid(drink_created, drinks_created, customer_order):
                drinks_created.append(drink_created)
                drink_created = []
            else:
                drink_created = []
            martini_glass.selected = True
            lowball_glass.selected = False
            glass_clickable["Martini Glass"] = False
            glass_clickable["Lowball Glass"] = True
            martini_glass_button.switch = False
        elif lowball_glass_button.switch and glass_clickable["Lowball Glass"] and glass_clickable["Martini Glass"]:
            if is_valid(drink_created, drinks_created, customer_order):
                drinks_created.append(drink_created)
                drink_created = []
            else:
                drink_created = []
            lowball_glass.selected = True
            glass_clickable["Lowball Glass"] = False
            lowball_glass_button.switch = False
        elif lowball_glass_button.switch and glass_clickable["Lowball Glass"] and glass_clickable["Martini Glass"]==False:
            if is_valid(drink_created, drinks_created, customer_order):
                drinks_created.append(drink_created)
                drink_created = []
            else:
                drink_created = []
            lowball_glass.selected = True
            martini_glass.selected = False
            glass_clickable["Lowball Glass"] = False
            glass_clickable["Martini Glass"] = True
            lowball_glass_button.switch = False
        
    
 
        #show drinks created by player
        list_of_drinks_images = convert_made_coctails_to_images(drinks_created)
        x_axis = 390
        for image in list_of_drinks_images:
            x_axis += 50
            drink_button = Button(x_axis,300, image)
            drink_button.draw(WIN)



        # has the order been satisfied?
        if is_same_2d_lists(drinks_created, customer_order):
            print("customer served")
            customer_served = customer_queue.customer_list.pop(customer_queue_number) # take the serviced customer out of the queue.
            customer_reciept = customer_served.order # a list of drinks ordered
            #cost = 0
            for drink in customer_reciept:
                money_made += drink.price # get the price of each drink and add it to the total
            #print(cost)
            print(customer_queue.customer_list)
            customer_queue.customer_list.insert(customer_queue_number, None) # or the _fill_empty_list_space() queue function will throw an index not found error
            drinks_created = [] 
            customer_order = []

                #WIN.blit(pygame.image.load(customer_queue.customer_list[i].face), customer_coordinates[i])

        # print the total on the page 
        total_amount_spent = TextButton(650,270, str(money_made))
        total_amount_spent.draw(WIN)


        # event handling, gets all event from the event queue
        for event in pygame.event.get():
            # only do something if the event is of type QUIT
            if event.type == pygame.QUIT:
                #change the value to False, to exit the main loop
                running = False
            if event.type == pygame.MOUSEBUTTONUP:
                for ingredient in add_ingredient:
                    if add_ingredient[ingredient] == False:
                        add_ingredient[ingredient] = True

        
        pygame.display.update()
        # fps
        clock.tick(30)
        
    pygame.quit()

# run the main function only if this module is executed as the main script 
# if you import this as a module then nothing is executed.
if __name__=="__main__":
    main()