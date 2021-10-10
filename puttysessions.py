# -*- coding: utf-8 -*-
import winreg
from theme import *

class PuttySession:
    def __init__(self, name, theme):
        self.name = name
        self.theme = theme


class PuttyLoader:
    base_key = r"SOFTWARE\\SimonTatham\\PuTTY\\Sessions"

    @staticmethod
    def getSessionKey(session):
        return "{}\\{}".format(PuttyLoader.base_key,session)

    @staticmethod
    def sessionNames(reg = winreg.ConnectRegistry(None, winreg.HKEY_CURRENT_USER)):
        with winreg.OpenKey(reg, PuttyLoader.base_key, winreg.KEY_READ) as key:
            for i in range(1024):
                try:
                    subkey_name = winreg.EnumKey(key, i)
                    yield subkey_name
                except EnvironmentError:
                    pass

    @staticmethod
    def sessionColors(session_name, reg = winreg.ConnectRegistry(None, winreg.HKEY_CURRENT_USER)):
        keypath = PuttyLoader.getSessionKey(session_name)
        with winreg.OpenKey(reg, keypath, winreg.KEY_READ) as key:
            for i in range(22):
                try:
                    colour_name = "{0}{1}".format("Colour",i)
                    yield winreg.QueryValueEx(key, colour_name)[0]
                except EnvironmentError:
                    pass

    @staticmethod
    def toTheme(session_colors):
        """Convert an array of colors into a theme """
        theme = Theme()
        for color_str in session_colors:
            color_arr = color_str.split(",",3)
            if (len(color_arr) != 3):
                print("Invalid color combination found")
                color = Color(0,0,0)
            else:
                color = Color(color_arr[0],color_arr[1],color_arr[2])
            theme.addColor(color)
        return theme

    @staticmethod
    def sessions():
        """return a generator of PuttySession"""
        for name in PuttyLoader.sessionNames():
            session_colors = (PuttyLoader.sessionColors(name))
            theme = PuttyLoader.toTheme(session_colors)
            yield PuttySession(name, theme)

    @staticmethod
    def themeBySession(session_name):
        session_colors = PuttyLoader.sessionColors(session_name)
        return PuttyLoader.toTheme(session_colors)

class PuttyUpdate:
    @staticmethod
    def updateSession(session_name, theme=Theme, reg = winreg.ConnectRegistry(None, winreg.HKEY_CURRENT_USER)):
        keypath = PuttyLoader.getSessionKey(session_name)
        with winreg.OpenKey(reg, keypath, 0, winreg.KEY_ALL_ACCESS) as key:
            for index,color in enumerate(theme.colors):
                try:
                    colour_name = "{0}{1}".format("Colour",index)
                    # print(winreg.QueryValueEx(key, colour_name)[0])
                    winreg.SetValueEx(key, colour_name, 0, winreg.REG_SZ, str(color.regFormat()))
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