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


class Theme:
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

    def toHash(self):
        p = pickle.dumps(self.colors, -1)
        return hash(p)

    @staticmethod
    def default():
        theme = Theme("Default")
        theme.addColorValues(187,187,187)
        theme.addColorValues(255,255,255)
        theme.addColorValues(0,0,0)
        theme.addColorValues(85,85,85)
        theme.addColorValues(0,0,0)
        theme.addColorValues(0,255,0)
        theme.addColorValues(0,0,0)
        theme.addColorValues(85,85,85)
        theme.addColorValues(187,0,0)
        theme.addColorValues(255,85,85)
        theme.addColorValues(0,187,0)
        theme.addColorValues(85,255,85)
        theme.addColorValues(187,187,0)
        theme.addColorValues(255,255,85)
        theme.addColorValues(0,0,187)
        theme.addColorValues(85,85,255)
        theme.addColorValues(187,0,187)
        theme.addColorValues(255,85,255)
        theme.addColorValues(0,187,187)
        theme.addColorValues(85,255,255)
        theme.addColorValues(187,187,187)
        theme.addColorValues(255,255,255)
        return theme