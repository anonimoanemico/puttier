# -*- coding: utf-8 -*-
import winreg
from puttier.theme import *


class PuttySession:
    def __init__(self, name, theme, font, font_size):
        self.name = name
        self.theme = theme
        self.font = font
        self.font_size = font_size

    @staticmethod
    def compare(session1, session2):
        if session1.name < session2.name:
            return -1
        elif session1.name > session2.name:
            return 1
        else:
            return 0


class PuttyLoader:
    base_key = r"SOFTWARE\\SimonTatham\\PuTTY\\Sessions"

    @staticmethod
    def getSessionKey(session):
        return "{}\\{}".format(PuttyLoader.base_key, session)

    @staticmethod
    def sessionNames(reg=winreg.ConnectRegistry(None, winreg.HKEY_CURRENT_USER)):
        with winreg.OpenKey(reg, PuttyLoader.base_key, winreg.KEY_READ) as key:
            for i in range(1024):
                try:
                    subkey_name = winreg.EnumKey(key, i)
                    yield subkey_name
                except EnvironmentError:
                    pass

    @staticmethod
    def sessionColors(session_name, reg=winreg.ConnectRegistry(None, winreg.HKEY_CURRENT_USER)):
        keypath = PuttyLoader.getSessionKey(session_name)
        with winreg.OpenKey(reg, keypath, winreg.KEY_READ) as key:
            for i in range(22):
                try:
                    colour_name = "{0}{1}".format("Colour", i)
                    yield winreg.QueryValueEx(key, colour_name)[0]
                except EnvironmentError:
                    pass

    @staticmethod
    def sessionFont(session_name, reg=winreg.ConnectRegistry(None, winreg.HKEY_CURRENT_USER)):
        keypath = PuttyLoader.getSessionKey(session_name)
        with winreg.OpenKey(reg, keypath, winreg.KEY_READ) as key:
            try:
                font_name = winreg.QueryValueEx(key, "Font")[0]
                font_size = winreg.QueryValueEx(key, "FontHeight")[0]
                return (font_name, font_size)
            except EnvironmentError:
                return (None, None)

    @staticmethod
    def toTheme(session_colors):
        """Convert an array of colors into a theme """
        theme = Theme()
        for color_str in session_colors:
            color_arr = color_str.split(",", 3)
            if (len(color_arr) != 3):
                print("Invalid color combination found")
                color = Color(0, 0, 0)
            else:
                color = Color(color_arr[0], color_arr[1], color_arr[2])
            theme.addColor(color)
        return theme

    @staticmethod
    def sessions():
        """return a generator of PuttySession"""
        for name in PuttyLoader.sessionNames():
            session_colors = (PuttyLoader.sessionColors(name))
            theme = PuttyLoader.toTheme(session_colors)
            font, font_size = PuttyLoader.sessionFont(name)
            yield PuttySession(name, theme, font, font_size)

    @staticmethod
    def themeBySession(session_name):
        session_colors = PuttyLoader.sessionColors(session_name)
        return PuttyLoader.toTheme(session_colors)


class PuttyUpdate:
    @staticmethod
    def updateSession(session_name, theme=Theme, font_family=None, font_size=None, reg=winreg.ConnectRegistry(None, winreg.HKEY_CURRENT_USER)):
        keypath = PuttyLoader.getSessionKey(session_name)
        with winreg.OpenKey(reg, keypath, 0, winreg.KEY_ALL_ACCESS) as key:
            if font_family:
                winreg.SetValueEx(
                    key, "Font", 0, winreg.REG_SZ, str(font_family))
            if font_size and int(font_size):
                winreg.SetValueEx(key, "FontHeight", 0,
                                  winreg.REG_DWORD, int(font_size))
            for index, color in enumerate(theme.colors):
                try:
                    colour_name = "{0}{1}".format("Colour", index)
                    winreg.SetValueEx(key, colour_name, 0,
                                      winreg.REG_SZ, str(color.regFormat()))
                    winreg.FlushKey(key)
                except EnvironmentError as err:
                    print(err)
                    pass


def main():
    print(list(PuttyLoader.sessionNames()))
    session_colors = (PuttyLoader.sessionColors("raspberrypi2"))
    theme = PuttyLoader.toTheme(session_colors)
    theme.describe()


if __name__ == "__main__":
    main()
