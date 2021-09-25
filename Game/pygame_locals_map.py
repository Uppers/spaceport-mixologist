import pygame
from pygame.locals import *

class UnicodeCharacters():

    def __init__(self):
        self.key_dict = {
            "K_SPACE": " "
            ,"K_EXCLAIM":"!"
            ,"K_QUOTEDBL":'"'
            ,"K_HASH":"#"
            ,"K_DOLLAR":"$"
            ,"K_AMPERSAND":"&"
            ,"K_QUOTE":"'"
            ,"K_LEFTPAREN":"("
            ,"K_RIGHTPAREN":")"
            ,"K_ASTERISK":"*"
            ,"K_PLUS":"+"
            ,"K_COMMA":","
            ,"K_MINUS ":"-"
            ,"K_PERIOD":"."
            ,"K_SLASH":"/"
            ,"K_0":"0"
            ,"K_1":"1"
            ,"K_2":"2"
            ,"K_3":"3"
            ,"K_4":"4"
            ,"K_5":"5"
            ,"K_6":"6"
            ,"K_7":"7"
            ,"K_8":"8"
            ,"K_9":"9"
            ,"K_KP0":"0"
            ,"K_KP1":"1"
            ,"K_KP2":"2"
            ,"K_KP3":"3"
            ,"K_KP4":"4"
            ,"K_KP5":"5"
            ,"K_KP6":"6"
            ,"K_KP7":"7"
            ,"K_KP8":"8"
            ,"K_KP9":"9"
            ,"K_COLON":":"
            ,"K_SEMICOLON":";"
            ,"K_LESS":"<"
            ,"K_EQUALS":"="
            ,"K_GREATER":">"
            ,"K_QUESTION":"?"
            ,"K_AT":"@"
            ,"K_LEFTBRACKET":"["
            ,"K_BACKSLASH":"\\"
            ,"K_RIGHTBRACKET":"]"
            ,"K_CARET":"^"
            ,"K_UNDERSCORE":"_"
            ,"K_BACKQUOTE":"`"
            ,"K_KP_PERIOD":"."
            ,"K_KP_DIVIDE":"/"
            ,"K_KP_MULTIPLY":"*"
            ,"K_KP_MINUS":"-"
            ,"K_KP_PLUS":"+"
            ,"K_KP_EQUALS":"="
            ,"K_EURO":"€"
            ,"K_a":"a"
            ,"K_b":"b"
            ,"K_c":"c"
            ,"K_d":"d"
            ,"K_e":"e"
            ,"K_f":"f"
            ,"K_g":"g"
            ,"K_h":"h"
            ,"K_i":"i"
            ,"K_j":"j"
            ,"K_k":"k"
            ,"K_l":"l"
            ,"K_m":"m"
            ,"K_n":"n"
            ,"K_o":"o"
            ,"K_p":"p"
            ,"K_q":"q"
            ,"K_r":"r"
            ,"K_s":"s"
            ,"K_t":"t"
            ,"K_u":"u"
            ,"K_v":"v"
            ,"K_w":"w"
            ,"K_x":"x"
            ,"K_y":"y"
            ,"K_z":"z"
            ,"K_PERCENT":"%"
        }

    def key_press(self, pressed):
        letter = ""
        if pressed[K_SPACE]:
            letter = self.key_dict["K_SPACE"]
        elif pressed[K_EXCLAIM]:
            letter = self.key_dict["K_EXCLAIM"]
        elif pressed[K_QUOTEDBL]:
            letter = self.key_dict["K_QUOTEDBL"]
        elif pressed[K_HASH]:
            letter = self.key_dict["K_HASH"]
        elif pressed[K_DOLLAR]:
            letter = self.key_dict["K_DOLLAR"]
        elif pressed[K_AMPERSAND]:
            letter = self.key_dict["K_AMPERSAND"]
        elif pressed[K_QUOTE]:
            letter = self.key_dict["K_QUOTE"]
        elif pressed[K_LEFTPAREN]:
            letter = self.key_dict["K_LEFTPAREN"]
        elif pressed[K_RIGHTPAREN]:
            letter = self.key_dict["K_RIGHTPAREN"]
        elif pressed[K_ASTERISK]:
            letter = self.key_dict["K_ASTERISK"]
        elif pressed[K_PLUS]:
            letter = self.key_dict["K_PLUS"]
        elif pressed[K_COMMA]:
            letter = self.key_dict["K_COMMA"]
        elif pressed[K_MINUS]:
            letter = self.key_dict["K_MINUS"]
        elif pressed[K_PERIOD]:
            letter = self.key_dict["K_PERIOD"]
        elif pressed[K_SLASH]:
            letter = self.key_dict["K_SLASH"]
        elif pressed[K_0]:
            letter = self.key_dict["K_0"]
        elif pressed[K_1]:
            letter = self.key_dict["K_1"]
        elif pressed[K_2]:
            letter = self.key_dict["K_2"]
        elif pressed[K_3]:
            letter = self.key_dict["K_3"]
        elif pressed[K_4]:
            letter = self.key_dict["K_4"]
        elif pressed[K_5]:
            letter = self.key_dict["K_5"]
        elif pressed[K_6]:
            letter = self.key_dict["K_6"]
        elif pressed[K_7]:
            letter = self.key_dict["K_7"]
        elif pressed[K_8]:
            letter = self.key_dict["K_8"]
        elif pressed[K_9]:
            letter = self.key_dict["K_9"]
        elif pressed[K_KP0]:
            letter = self.key_dict["K_KP0"]
        elif pressed[K_KP1]:
            letter = self.key_dict["K_KP1"]
        elif pressed[K_KP2]:
            letter = self.key_dict["K_KP2"]
        elif pressed[K_KP3]:
            letter = self.key_dict["K_KP3"]
        elif pressed[K_KP4]:
            letter = self.key_dict["K_KP4"]
        elif pressed[K_KP5]:
            letter = self.key_dict["K_KP5"]
        elif pressed[K_KP6]:
            letter = self.key_dict["K_KP6"]
        elif pressed[K_KP7]:
            letter = self.key_dict["K_KP7"]
        elif pressed[K_KP8]:
            letter = self.key_dict["K_KP8"]
        elif pressed[K_KP9]:
            letter = self.key_dict["K_KP9"]
        elif pressed[K_COLON]:
            letter = self.key_dict["K_COLON"]
        elif pressed[K_SEMICOLON]:
            letter = self.key_dict["K_SEMICOLON"]
        elif pressed[K_LESS]:
            letter = self.key_dict["K_LESS"]
        elif pressed[K_EQUALS]:
            letter = self.key_dict["K_EQUALS"]
        elif pressed[K_GREATER]:
            letter = self.key_dict["K_GREATER"]
        elif pressed[K_QUESTION]:
            letter = self.key_dict["K_QUESTION"]
        elif pressed[K_AT]:
            letter = self.key_dict["K_AT"]
        elif pressed[K_LEFTBRACKET]:
            letter = self.key_dict["K_LEFTBRACKET"]
        elif pressed[K_BACKSLASH]:
            letter = self.key_dict["K_BACKSLASH"]
        elif pressed[K_RIGHTBRACKET]:
            letter = self.key_dict["K_RIGHTBRACKET"]
        elif pressed[K_CARET]:
            letter = self.key_dict["K_CARET"]
        elif pressed[K_UNDERSCORE]:
            letter = self.key_dict["K_UNDERSCORE"]
        elif pressed[K_BACKQUOTE]:
            letter = self.key_dict["K_BACKQUOTE"]
        elif pressed[K_KP_PERIOD]:
            letter = self.key_dict["K_KP_PERIOD"]
        elif pressed[K_KP_DIVIDE]:
            letter = self.key_dict["K_KP_DIVIDE"]
        elif pressed[K_KP_MULTIPLY]:
            letter = self.key_dict["K_KP_MULTIPLY"]
        elif pressed[K_KP_MINUS]:
            letter = self.key_dict["K_KP_MINUS"]
        elif pressed[K_KP_PLUS]:
            letter = self.key_dict["K_KP_PLUS"]
        elif pressed[K_KP_EQUALS]:
            letter = self.key_dict["K_KP_EQUALS"]
        elif pressed[K_EURO]:
            letter = self.key_dict["K_EURO"]
        elif pressed[K_a]:
            letter = self.key_dict["K_a"]
        elif pressed[K_b]:
            letter = self.key_dict["K_b"]
        elif pressed[K_c]:
            letter = self.key_dict["K_b"]
        elif pressed[K_d]:
            letter = self.key_dict["K_d"]
        elif pressed[K_e]:
            letter = self.key_dict["K_e"]
        elif pressed[K_f]:
            letter = self.key_dict["K_f"]
        elif pressed[K_g]:
            letter = self.key_dict["K_g"]
        elif pressed[K_h]:
            letter = self.key_dict["K_h"]
        elif pressed[K_i]:
            letter = self.key_dict["K_i"]
        elif pressed[K_j]:
            letter = self.key_dict["K_j"]
        elif pressed[K_k]:
            letter = self.key_dict["K_k"]
        elif pressed[K_l]:
            letter = self.key_dict["K_l"]
        elif pressed[K_m]:
            letter = self.key_dict["K_m"]
        elif pressed[K_n]:
            letter = self.key_dict["K_n"]
        elif pressed[K_o]:
            letter = self.key_dict["K_o"]
        elif pressed[K_p]:
            letter = self.key_dict["K_p"]
        elif pressed[K_q]:
            letter = self.key_dict["K_q"]
        elif pressed[K_r]:
            letter = self.key_dict["K_r"]
        elif pressed[K_s]:
            letter = self.key_dict["K_s"]
        elif pressed[K_t]:
            letter = self.key_dict["K_t"]
        elif pressed[K_u]:
            letter = self.key_dict["K_u"]
        elif pressed[K_v]:
            letter = self.key_dict["K_v"]
        elif pressed[K_w]:
            letter = self.key_dict["K_w"]
        elif pressed[K_x]:
            letter = self.key_dict["K_x"]
        elif pressed[K_y]:
            letter = self.key_dict["K_y"]
        elif pressed[K_z]:
            letter = self.key_dict["K_z"]
        elif pressed[K_0] and (pressed[K_LSHIFT] or pressed[K_RSHIFT]):
            letter = self.key_dict["K_RIGHTPAREN"]
        elif pressed[K_1] and (pressed[K_LSHIFT] or pressed[K_RSHIFT]):
            letter = self.key_dict["K_EXCLAIM"]
        elif pressed[K_2] and (pressed[K_LSHIFT] or pressed[K_RSHIFT]):
            letter = self.key_dict["K_AT"]
        elif pressed[K_3] and (pressed[K_LSHIFT] or pressed[K_RSHIFT]):
            letter = self.key_dict["K_HASH"]
        elif pressed[K_4] and (pressed[K_LSHIFT] or pressed[K_RSHIFT]):
            letter = self.key_dict["K_DOLLAR"]
        elif pressed[K_5] and (pressed[K_LSHIFT] or pressed[K_RSHIFT]):
            letter = self.key_dict["K_PERCENT"]
        elif pressed[K_6] and (pressed[K_LSHIFT] or pressed[K_RSHIFT]):
            letter = self.key_dict["K_CARET"]
        elif pressed[K_7] and (pressed[K_LSHIFT] or pressed[K_RSHIFT]):
            letter = self.key_dict["K_AMPERSAND"]
        elif pressed[K_8] and (pressed[K_LSHIFT] or pressed[K_RSHIFT]):
            letter = self.key_dict["K_ASTERISK"]
        elif pressed[K_9] and (pressed[K_LSHIFT] or pressed[K_RSHIFT]):
            letter = self.key_dict["K_LEFTPAREN"]
        elif pressed[K_KP0] and (pressed[K_LSHIFT] or pressed[K_RSHIFT]):
            letter = self.key_dict["K_RIGHTPAREN"]
        elif pressed[K_KP1] and (pressed[K_LSHIFT] or pressed[K_RSHIFT]):
            letter = self.key_dict["K_EXCLAIM"]
        elif pressed[K_KP2] and (pressed[K_LSHIFT] or pressed[K_RSHIFT]):
            letter = self.key_dict["K_AT"]
        elif pressed[K_KP3] and (pressed[K_LSHIFT] or pressed[K_RSHIFT]):
            letter = self.key_dict["K_HASH"]
        elif pressed[K_KP4] and (pressed[K_LSHIFT] or pressed[K_RSHIFT]):
            letter = self.key_dict["K_DOLLAR"]
        elif pressed[K_KP5] and (pressed[K_LSHIFT] or pressed[K_RSHIFT]):
            letter = self.key_dict["K_PERCENT"]
        elif pressed[K_KP6] and (pressed[K_LSHIFT] or pressed[K_RSHIFT]):
            letter = self.key_dict["K_CARET"]
        elif pressed[K_KP7] and (pressed[K_LSHIFT] or pressed[K_RSHIFT]):
            letter = self.key_dict["K_AMPERSAND"]
        elif pressed[K_KP8] and (pressed[K_LSHIFT] or pressed[K_RSHIFT]):
            letter = self.key_dict["K_ASTERISK"]
        elif pressed[K_KP9] and (pressed[K_LSHIFT] or pressed[K_RSHIFT]):
            letter = self.key_dict["K_LEFTPAREN"]
        if pressed[K_LSHIFT] or pressed[K_RSHIFT] or pressed[K_CAPSLOCK]:
            letter = letter.upper()
        return letter







