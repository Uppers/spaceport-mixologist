import os
import pygame

class Glass():

    def __init__(self, name):
        self.name = name
        self.image_location = os.path.join("Assets", "glasses",f"{self.name}.png")
        self.image = pygame.image.load(self.image_location)
        self.selected = False
