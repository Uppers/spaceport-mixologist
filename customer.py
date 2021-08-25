from datetime import datetime
from button import Button
from order import Order
import pygame
import os

class Customer(Button, Order):
    """This is the model for a customer"""

    def __init__(self, name, x, y, queue_patience, scale = 1):
        self.name = name
        self.scale = scale
        self.x = x
        self.y = y
        self.queue_patience = queue_patience
        self.percent_patience_remaining = 1
        self._customer_status = "happy"
        self._time_at_init = datetime.now()
        self.face = os.path.join("Assets",f"{self.name}",f"{self._customer_status}.png")
        Button.__init__(self, x, y, image= pygame.image.load(self.face).convert_alpha(), scale=scale)
        Order.__init__(self)



    def _time_elapsed(self):
        time_now = datetime.now()
        time_delta = time_now-self._time_at_init
        return time_delta.total_seconds()

    def update_customer_status(self):
        has_status_changed = False
        self.percent_patience_remaining = 1-(self._time_elapsed()/self.queue_patience)
        if self.percent_patience_remaining >= 2/3: # checks if customer should be happy
            if self._customer_status != "happy": # if customer is not happy then this will need to be changed
                self._customer_status =  "happy" # change to happy
                has_status_changed = True # so we can update the face image because there has been a change
        elif self.percent_patience_remaining >= 1/3: # checks if a customer should be waiting
            if self._customer_status != "waiting": # if customer is not waiting then this should be changed
                self._customer_status =  "waiting" # change to waiting
                has_status_changed = True # so we can update the face image because there has been a change
        else: # you get the idea if you've read the above comments
            if self._customer_status != "cross": 
                self._customer_status =  "cross"
                has_status_changed = True
        if has_status_changed: # checks for change in status
            self._face() # changes the image.


    def _face(self):
        self.face = os.path.join("Assets",f"{self.name}",f"{self._customer_status}.png")
        super().__init__(self.x, self.y, image= pygame.image.load(self.face).convert_alpha(), scale = self.scale)


    
    def _drinks_order(self):
        return "drinks"

