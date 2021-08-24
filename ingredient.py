import os
import pygame 

class Ingredient():

    def __init__(self, ingredient_name, abv):
        self.name = ingredient_name
        self.abv = abv
        self.image_location = os.path.join("Assets", "ingredients",self.name, f"{self.name}.png")
        self.image = pygame.image.load(self.image_location)


class Gin(Ingredient):

    def __init__(self):
        super().__init__("Gin", 40)

class Vodka(Ingredient):

    def __init__(self):
        super().__init__("Vodka", 40)

class Vermouth(Ingredient):

    def __init__(self):
        super().__init__("Vermouth", 18)

class Tonic(Ingredient):

    def __init__(self):
        super().__init__("Tonic", 0)

class Ice(Ingredient):

    def __init__(self):
        super().__init__("Ice", 0)
