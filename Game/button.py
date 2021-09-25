import pygame
import os

class Button():
    """
    This makes images into clickable buttons.
    Credit to: https://www.youtube.com/watch?v=G8MYGDf_9ho
    """

    def __init__(self, x, y, image, scale = 1):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width*scale), int(height*scale)))
        self.rect = image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False
        self.switch = False
    
    def draw(self, surface):
        if self.image:
            action = False 
            # get mouse position
            pos = pygame.mouse.get_pos()

            # check mouseover and clicked conditions
            if self.rect.collidepoint(pos):
                #if pygame.MOUSEBUTTONDOWN and self.clicked == False:
                if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False: #do these things if the mouse is clicked on the image button.
                    self.clicked = True 
                    action = True
                    if self.switch:
                        self.switch = False
                    else:
                        self.switch = True


            if pygame.mouse.get_pressed()[0] == 0:
                self.clicked = False 

            # draw button on screen
            surface.blit(self.image, (self.rect.x, self.rect.y))

            return action 

class TextButton(Button):
    """This makes text into clickable buttons"""

    def __init__(self, x, y, text, font_size=10, font_colour = pygame.Color("Black"), background_colour = pygame.Color("White")):
        self.font = os.path.join("Assets", "fonts","8-BIT WONDER.TTF")
        self.font = pygame.font.Font(self.font, font_size) # set font 
        self.text = text
        self.font_colour = font_colour
        self.background_colour = background_colour
        self.image = self.font.render(self.text,True, self.font_colour, background_colour) # render the text in a black colour with a white background
        super().__init__(x,y,self.image)

    def change_colour(self, colour):
        self.image = self.font.render(self.text,True, colour, self.background_colour)