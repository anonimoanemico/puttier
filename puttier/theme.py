# -*- coding: utf-8 -*-

import pickle


class Color:
    def __init__(self, red, green, blue):
        self.red = int(red)
        self.green = int(green)
        self.blue = int(blue)

    def toHash(self):
        return hash((self.red, self.green, self.blue))

    def regFormat(self):
        return "{},{},{}".format(self.red, self.green, self.blue)

    def toTuple(self):
        return (self.red, self.green, self.blue)

    @staticmethod
    def mix(color1, color2):
        red = int((color1.red+color2.red)/2)
        green = int((color1.green+color2.green)/2)
        blue = int((color1.blue+color2.blue)/2)
        return Color(red, green, blue)


class Theme(object):
    DEFAULT_FOREGROUND = 0
    DEFAULT_BOLD_FOREGROUND = 1
    DEFAULT_BACKGROUND = 2
    DEFAULT_BOLD_BACKGROUND = 3
    CURSOR_TEXT = 4
    CURSOR_COLOR = 5
    ANSI_BLACK = 6
    ANSI_BLACK_BOLD = 7
    ANSI_RED = 8
    ANSI_RED_BOLD = 9
    ANSI_GREEN = 10
    ANSI_GREEN_BOLD = 11
    ANSI_YELLOW = 12
    ANSI_YELLOW_BOLD = 13
    ANSI_BLUE = 14
    ANSI_BLUE_BOLD = 15
    ANSI_MAGENTA = 16
    ANSI_MAGENTA_BOLD = 17
    ANSI_CYAN = 18
    ANSI_CYAN_BOLD = 19
    ANSI_WHITE = 20
    ANSI_WHITE_BOLD = 21

    def __init__(self, name=None):
        self.colors = []
        self.name = name

    def addColorValues(self, red=0, green=0, blue=0):
        self.colors.append(Color(red, green, blue))
        return self

    def addColor(self, color=Color):
        self.colors.append(color)
        return self

    def describe(self):
        for c in self.colors:
            print("{} {} {}".format(c.red, c.green, c.blue))

    def describeHex(self):
        for c in self.colors:
            print("0x{:02x}{:02x}{:02x}".format(c.red, c.green, c.blue))

    def toHash(self):
        p = pickle.dumps(self.colors, -1)
        return hash(p)

    def getColorHexByIndex(self, index):
        if len(self.colors) != 22 or index > 21 or index < 0:
            return None
        color_hex_str = "".join('{:02x}'.format(a)
                                for a in self.colors[index].toTuple())
        return "#{}".format(color_hex_str)

    def getColorHex(self, color_index):
        if len(self.colors) != 22:
            return None
        color_hex_str = self.getColorHexByIndex(color_index)
        return color_hex_str

    @staticmethod
    def default():
        theme = Theme("Default")
        theme.addColorValues(187, 187, 187)
        theme.addColorValues(255, 255, 255)
        theme.addColorValues(0, 0, 0)
        theme.addColorValues(85, 85, 85)
        theme.addColorValues(0, 0, 0)
        theme.addColorValues(0, 255, 0)
        theme.addColorValues(0, 0, 0)
        theme.addColorValues(85, 85, 85)
        theme.addColorValues(187, 0, 0)
        theme.addColorValues(255, 85, 85)
        theme.addColorValues(0, 187, 0)
        theme.addColorValues(85, 255, 85)
        theme.addColorValues(187, 187, 0)
        theme.addColorValues(255, 255, 85)
        theme.addColorValues(0, 0, 187)
        theme.addColorValues(85, 85, 255)
        theme.addColorValues(187, 0, 187)
        theme.addColorValues(255, 85, 255)
        theme.addColorValues(0, 187, 187)
        theme.addColorValues(85, 255, 255)
        theme.addColorValues(187, 187, 187)
        theme.addColorValues(255, 255, 255)
        return theme
