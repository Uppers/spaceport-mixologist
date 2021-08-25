import queue
import random
from customer import Customer

class Queue():

    def __init__(self, queue_space_coordinates):
        self.coordinates = queue_space_coordinates
        self.customer_list = [None for x in range(len(queue_space_coordinates))] # creates a queue with the same amount of spaces as coordinates
        self._possible_names = ("gary", "terry", "jane", "emma",)
        self.expired_customers = []

    # this will create a customer object with randomised parameters (within boundaries).
    def create_customer(self, space):
        name = self._possible_names[round(random.uniform(0,len(self._possible_names)-1))]
        x = self.coordinates[space][0]
        y = self.coordinates[space][1]
        patience_in_seconds = round(random.uniform(40,120))
        return Customer(name, x, y, patience_in_seconds)

    # this should be called in the game loop and will constantly keep the customers up to date.
    def update_customer_list(self):
        self._fill_empty_list_space()
        self._retire_expired_customer()

    # this looks to see if a given space is empty, if it is empty then there is a 1/90 chance that a
    # new customer will be inserted - the game loop updates 30 times per second.
    def _fill_space_if_empty(self, space):
        if self.customer_list[space] is None:
            lucky_number = 45
            random_number = round(random.uniform(0,90))
            if lucky_number == random_number:
                del self.customer_list[space]
                self.customer_list.insert(space, self.create_customer(space))

    # this will fill any empty spaces in the customer list.
    def _fill_empty_list_space(self):
        if all(v is None for v in self.customer_list):
            position = round(random.uniform(0,2)) # gives random integer between 0 and 2 inclusive
            del self.customer_list[position]
            self.customer_list.insert(position, self.create_customer(position))
        elif self.customer_list[0] is None:
            self._fill_space_if_empty(0)
        elif self.customer_list[1] is None:
            self._fill_space_if_empty(1)
        elif self.customer_list[2] is None:
            self._fill_space_if_empty(2)

    # this looks to see if any of the customers have lost their patience and need to leave the queue.
    def _retire_expired_customer(self):
        for i in range(0,len(self.customer_list)):
            if self.customer_list[i] is not None:
                if self.customer_list[i].percent_patience_remaining <= 0:
                    self.expired_customers.append(self.customer_list[i])
                    self.customer_list.remove(self.customer_list[i])
                    self.customer_list.insert(i, None)





