from cocktail import GinAndTonic, VesperMartini
import random


class Order():

    def __init__(self):
        self.possible_drinks = (GinAndTonic(), VesperMartini()) # all possible drinks.
        self.order = self._create_drinks_order()
        self.order_for_display = self._order_for_display()


    def _order_for_display(self): # how the order will be written onscreen
        if self.order:
            opening_text = ""
            drinks_dict = self._simplify_order()
            length_dict = len(drinks_dict)-1
            i = 0
            for key, value in drinks_dict.items():
                if length_dict == 0:
                    drink_text = f" {str(value)} {key}"
                    opening_text += drink_text                 
                elif i == length_dict:
                    drink_text = f" and {str(value)} {key}"
                    opening_text += drink_text
                    i+=1
                else:
                    drink_text = f" {str(value)} {key},"
                    opening_text += drink_text
                    i+=1
            return opening_text #surface.blit(opening_text, (self.x, self.y))

    def _simplify_order(self):
        drinks = {}
        for drink in self.order:
            if drink.drink_name in drinks:
                drinks[drink.drink_name] += 1
            else:
                drinks[drink.drink_name] = 1
        return drinks

    
    def _create_drinks_order(self): # creates the drinks order
        drinks_order = []
        number_of_drinks = round(random.uniform(1,5))
        for i in range(number_of_drinks):
            drinks_order.append(self._pick_random_drink())
        return drinks_order


    def _pick_random_drink(self): # picks a random drink from the list of possible drinks
        i = round(random.uniform(0,len(self.possible_drinks)-1))
        return self.possible_drinks[i]
