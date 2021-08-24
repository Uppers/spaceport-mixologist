import pygame 


class Text():
    WHITE = (255,255,255)
    BLACK = (0,0,0)

    def __init__(self, text, x, y):
        self.text = text 
        self.font_name = "freesansbold.ttf"
        self.font_size = 20
        self.font = pygame.font.Font(self.font_name, self.font_size) # set font 
        self.text_render = self.font.render(self.text,True, self.BLACK, self.WHITE) # render the text in a black colour with a white background
        self.text_rect = self.text_render.get_rect()
        self.x = x
        self.y = y

    def draw(self, surface):
        surface.blit(self.text_render, (self.x, self.y))
 




