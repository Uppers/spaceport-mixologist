import os
import pygame
from Game.ingredient import Gin, Vodka, Vermouth, Ice, Tonic

class Cocktail():

    def __init__(self):
        self.drink_name = None
        self.drink_ingredients = ((None,None))
        self.shaken_not_stirred = False
        self.price = 0
        self.glass = ""

    def get_image_location(self):
        return os.path.join("Assets", "cocktails",f"{self.drink_name}.png")


    def get_image(self):
        return pygame.image.load(self.get_image_location())
        

class GinAndTonic(Cocktail):

    def __init__(self):
        self.drink_name = "Gin and Tonic"
        #self.drink_ingredients = ((Gin(),2), (Ice(), 1), (Tonic(), 1))
        self.drink_ingredients = (Gin(), Ice(), Tonic())
        self.shaken_not_stirred = False
        self.price = 60
        self.glass = "Lowball Glass"
        


class VesperMartini(Cocktail):

    def __init__(self):
        self.drink_name = "Vesper Martini"
        #self.drink_ingredients = ((Gin(), 3), (Vodka(), 1), (Vermouth(), 0.5), (Ice(), 1))
        self.drink_ingredients =(Gin(), Vodka(), Vermouth(), Ice())
        self.shaken_not_stirred = True
        self.price = 90
        self.glass = "Martini Glass"



