class Interaction():
    """ This is the class for functions and variables relating to user interaction with the game."""

    def __init__(self):
        self.customer_queue_number = None 
        self.customer_order = []
        self.drink_created = []
        self.drinks_created = []
        self.money_made = 0
        self.glass_clickable = {
                            "Martini Glass": True,
                            "Lowball Glass": True,
                            }
        self.add_ingredient = {
                                "Gin":True,
                                "Vodka":True,
                                "Vermouth":True,
                                "Tonic":True,
                                "Ice":True,
                                }


    def place_customer_order(self, current_customer_order, customer_queue_number):
        # the order of the customer (who is currently selected) is saved to a variable.
        self._create_customer_drinks_order(current_customer_order)
        # the position of the customer on the bar is saved 
        self.customer_queue_number = customer_queue_number

    def glass_button_clicked(self, glasses, glass_buttons):
        # this makes sure that glasses can be selected. 
        for glass in glasses:
            if glass_buttons[glass.name].switch and self.glass_clickable[glass.name]: #and self.glass_clickable["Lowball Glass"]==False:
                self._add_drink_to_tray() # create the drink.
                glass.selected = True 
                self.glass_clickable[glass.name] = False # so it cannot be clicked repeatedly by accident.
                for g_lass in glasses:
                    if g_lass != glass:
                        g_lass.selected = False # all other glass types are not selected
                        self.glass_clickable[g_lass.name] = True # other types of glass can be selected in future.
                glass_buttons[glass.name].switch = False # other types of buttons are not selected.

    # if the drink is valid i.e. it is in the order then it gets added to tray
    def _add_drink_to_tray(self): # SHOULD USE self.drink_created , self.drinks_created & self.customer_order 
        if self._is_valid(): # check the drink is something the customer ordered.
            self.drinks_created.append(self.drink_created) # add it to the customer's tray
            self.drink_created=[] # make way for the creation of a new drink
        else:
            self.drink_created = [] # if its not valid then destroy it.

    # turns the ingredients for the drinks ordered by the customer into a list of strings.
    def _create_customer_drinks_order(self, drinks_order):
        order = []
        for drink in drinks_order:
            drink_ingredients = []
            for ingredient in drink.drink_ingredients:
                drink_ingredients.append(ingredient.name)
            order.append(drink_ingredients)
        self.customer_order =  order 

    def _is_valid(self): # SHOULD USE self.drink_created , self.drinks_created & self.customer_order 
        #checks if drink should be added to drinks_created
        if self._is_in_orderlist() and self._is_not_surplus():
            return True 
        else:
            False

    def _is_in_orderlist(self): # checks if drink created is in customer order
        for order in self.customer_order:                        
            if sorted(order) == sorted(self.drink_created):  
                return True
    
    def _is_not_surplus(self): 
        # checks if enough of that drink has already been made
        # counts how many of that drink_ingredients in drinks_order
        # counts how many of that drink_ingredients in drinks created
        # if count_drinks_order > count_drinks_created for that drink_ingredients then True (no surplus)
        count_drinks_created = self._count_instances_in_list(self.drink_created, self.drinks_created)
        count_drinks_order = self._count_instances_in_list(self.drink_created, self.customer_order)
        if count_drinks_order> count_drinks_created:
            return True
        else:
            False

    def _count_instances_in_list(self, instance, two_d_list):
        # where instance is a list and two_d_list is a list of lists. 
        number_of_instances = 0 
        for item in two_d_list:
            if sorted(instance) == sorted(item):
                number_of_instances+=1
        return number_of_instances

    # Identifies what the cocktail is from its ingredients and then provides the images of these cocktails as a list
    def convert_made_coctails_to_images(self, cocktail_ingredients_map, cocktail_name_map, list_of_cocktail_ingredients):
        images = []
        for list_of_ingredients in list_of_cocktail_ingredients:
            images.append(self._convert_ingredients_to_image(cocktail_ingredients_map, cocktail_name_map, list_of_ingredients))
        return images
    
    def _convert_ingredients_to_image(self, cocktail_ingredients_map, cocktail_name_map, list_of_ingredients):
        for key, value in cocktail_ingredients_map.items():
            if sorted(value) == sorted(list_of_ingredients):
                image = cocktail_name_map[key].get_image()
                return image

    def customer_not_served_in_time(self, customer_queue):
        # this bit of code checks for a customer who left because they werent served in time.
        # it then resets all the parameters associated with serving that customer.
        if self.customer_queue_number is not None: 
            if customer_queue.customer_list[self.customer_queue_number] is None:
                # reset everything
                self.customer_order = [] 
                self.drink_created = []
                self.drinks_created = []
                self.glass_clickable = dict.fromkeys(self.glass_clickable, True)

    def ingredient_button_clicked(self, ingredient_buttons):
        for button in ingredient_buttons:
            if button["button"].switch and self.add_ingredient[button["name"]]:
                self.drink_created.append(button["name"])
                self.add_ingredient[button["name"]] = False # drink can only be selected once (see event loop for more details).
                # either glass can now be selected
                self.glass_clickable["Lowball Glass"] = True
                self.glass_clickable["Martini Glass"] = True

    def cocktail_ingredients_list(self, cocktail_object):
        # returns the list of ingredients in a given cocktail. 
        ingredients = []
        cocktail_ingredients_obj = cocktail_object.drink_ingredients
        for ingredient_obj in cocktail_ingredients_obj:
            ingredient_name = ingredient_obj.name
            ingredients.append(ingredient_name)
        return sorted(ingredients)

    def order_satisfied(self, customer_queue):
        # has the order been satisfied? if so then:..
        if self._is_same_2d_lists(self.drinks_created, self.customer_order):
            drinks_served = self._pop_customer(customer_queue) # remove customer from queue and return what drinks were served.
            self.money_made += self._calculate_earnings(drinks_served) # calculate the earnings and add to total.
            self.drinks_created = [] 
            self.customer_order = []

    # used to check the customer has recieved their order
    # compares the cocktails made by the barista 
    def _is_same_2d_lists(self, twodlist1, twodlist2): 
        if twodlist1 is not None and twodlist2 is not None and len(twodlist1)>0 and len(twodlist2)>0:
            if len(twodlist1) == len(twodlist2):
                twodlist1 = self._sort_2d_list(twodlist1)
                twodlist2 = self._sort_2d_list(twodlist2)
                if twodlist1 == twodlist2:
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False


    def _sort_2d_list(self, twodlist):
        twodlist = twodlist.sort()
        sortedtwodlist = []
        if twodlist is not None:
            for list in twodlist:
                sortedtwodlist.append(list.sort())
            return sortedtwodlist

    # takes a customer that has been served from queue and returns the drinks they ordered.
    def _pop_customer(self, customer_queue): 
        customer_served = customer_queue.customer_list.pop(self.customer_queue_number) # take the serviced customer out of the queue.
        drinks_served = customer_served.order # a list of drinks ordered
        customer_queue.customer_list.insert(self.customer_queue_number, None) # or the _fill_empty_list_space() queue function will throw an index not found error
        return drinks_served

    def _calculate_earnings(self, drinks_served):
        revenue = 0
        for drink in drinks_served:
            revenue += drink.price # get the price of each drink and add it to the total
        return revenue
    
    


