import pygame
from Game.button import Button, TextButton

class Display():

    def display_drinks_created(self, list_of_drinks_images, screen):
        x_axis = 390
        for image in list_of_drinks_images:
            x_axis += 50
            drink_button = Button(x_axis,300, image)
            drink_button.draw(screen)

    def display_score(self, money_made, screen): # displays amount of money the player has made on screen
        total_amount_spent = TextButton(650,270, str(money_made),font_size=20, background_colour=pygame.Color("Gold"))
        total_amount_spent.draw(screen)

    # makes the buttons for the ingredients such as ice, vodka etc.
    def draw_ingredient_button(self, drink_obj, x, y, screen):
        button = Button(x,y, drink_obj.image)
        button.draw(screen)
        return {"name": drink_obj.name, "button": button}

    def display_customer_order_as_text_button(self, current_customer, screen):
        # (when customer is toggled) the customer order is displayed
        text = TextButton(340,360, current_customer.order_for_display)
        text.draw(screen)

    def display_customer(self, current_customer, screen):
        # displays the customers on screen
        current_customer.update_customer_status()
        current_customer.draw(screen)

        