import os 
import pygame
from pygame.locals import *
import win32clipboard
from Game.pygame_locals_map import UnicodeCharacters  

class Textbox():
    def __init__(self, x, y, width, height, font_size, max_chars, label = None):
        self.font_path = os.path.join("Assets", "fonts","8-BIT WONDER.TTF")
        self.font = pygame.font.Font(self.font_path, font_size) # set font 
        self.player_input = ""
        self.max_chars = max_chars
        self.label = label
        self.input_rect = pygame.Rect(x,y,width,height)
        self.active = False
        self._pressed_on = False #if the player clicks on the textbox
        self.key_down = False
        self._unicode_characters = UnicodeCharacters()
        self.active_colour = pygame.Color("Gold")
        self.passive_colour = pygame.Color("Grey")

    def write_text(self, screen):
        self._selected()
        # the label that tells you what the box is for
        if self.player_input == "" and self.active == False and self.label: 
            text_surface = self.font.render(self.label, True, pygame.Color("Grey"))
        else:
            # this writes text to the textbox
            if self.active:
                ctrlv = self._copy_from_clipboard() # retrieve data that was copied onto windows clipboard 
                if ctrlv:
                    self.player_input += str(ctrlv) # paste data to textbox
                self.player_input = self._erase_text() # if user presses backspace
                self.player_input = self._typed_text()
            text_surface = self.font.render(self.player_input, True, pygame.Color("Gold"))
        screen.blit(text_surface, (self.input_rect.x+5, self.input_rect.y+20))

    def _typed_text(self):
        pressed = pygame.key.get_pressed() # get the key presses 
        text = self.player_input # get the existing text 
        if len(self.player_input)<self.max_chars: # if the text box is not overflowing
            if any(pressed) and self.key_down==False: # if there has been a key press and it is the first one
                text += self._unicode_characters.key_press(pressed) # add the new key press char to existing text
                self.key_down = True # set to true to avaid duplicates
            if not any(pressed) and self.key_down: # if the key is no longer being held down...
                self.key_down = False # reset the flag so that a new key press can be registered.
        return text

    def _erase_text(self):
        if pygame.key.get_pressed()[K_BACKSPACE]:
            return self.player_input[:-1]
        else:
            return self.player_input
             
    def _copy_from_clipboard(self):
        # if user presses ctrl+v this returns the data from the clipboard (Windows OS only)
        pressed = pygame.key.get_pressed()
        if pressed[K_v] and pressed[K_LCTRL]:
            win32clipboard.OpenClipboard()
            data = win32clipboard.GetClipboardData()
            win32clipboard.CloseClipboard()
            #self.player_input = data
            if len(data)<= self.max_chars:
                return data
            else:
                return data[:self.max_chars]
        

    def _selected(self):
        # this checks if a textbox has been clicked on to select.
        pos = pygame.mouse.get_pos()# get mouse position
        if self.active: # if already selected then de-select.
            if self.input_rect.collidepoint(pos): # mouse is over the textbox
                if pygame.mouse.get_pressed()[0] == 1: # mouse clicked
                    self._pressed_on = True
                elif self._pressed_on and pygame.mouse.get_pressed()[0] == 0:
                    self.active = False
                    self._pressed_on = False
            else:
                if pygame.mouse.get_pressed()[0] == 1:
                    self.active = False
                    self._pressed_on = False
        else: # if not already selected then select
            if self.input_rect.collidepoint(pos): # mouse is over the textbox
                if pygame.mouse.get_pressed()[0] == 1: # mouse clicked
                    self._pressed_on = True
                elif self._pressed_on and pygame.mouse.get_pressed()[0] == 0:
                    self.active = True # sets active to true
                    self._pressed_on = False
            else:
                if pygame.mouse.get_pressed()[0] == 1: # mouse clicked
                    self.active = False # sets active to False



    def draw_box(self, screen):
        if self.active:
            pygame.draw.rect(screen, self.active_colour, self.input_rect, 3)
        else:
            pygame.draw.rect(screen, self.passive_colour, self.input_rect, 3)
