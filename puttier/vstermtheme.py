# -*- coding: utf-8 -*-

from puttier.theme import Theme, Color


class VsTermTheme(Theme):
    fontSizeOffset = 5

    def __init__(self, superclass):
        super().__init__(superclass.name)
        self.colors = superclass.colors

    def toJson(self, fontName=None, fontSize=None):
        json = """"workbench.colorCustomizations": {\n"""
        labels = {key: value for (key, value)
                  in VsTermTheme.labels.items() if value}
        for num, label in labels.items():
            c = self.colors[num]
            json = json + \
                "   \"{}\": \"#{:02x}{:02x}{:02x}\",\n".format(
                    label, c.red, c.green, c.blue)

        selection = Color.mix(
            self.colors[Theme.DEFAULT_BACKGROUND], self.colors[Theme.CURSOR_COLOR])
        json = json + "   \"terminal.selectionBackground\": \"#{:02x}{:02x}{:02x}\"\n".format(
            selection.red, selection.green, selection.blue)
        json = json + "}"
        if fontName:
            json = json + ",\n"
            json = json + \
                "\"terminal.integrated.fontFamily\": \"{}\"".format(fontName)
        if fontSize:
            json = json + ",\n"
            json = json + "\"terminal.integrated.fontSize\": {}\n".format(
                int(fontSize)+VsTermTheme.fontSizeOffset)
        return json

    def export(self, fontName, fontSize):
        return self.toJson(fontName, fontSize)

    def describe(self):
        print(self.toJson())

    labels = dict()
    labels[Theme.DEFAULT_FOREGROUND] = "terminal.foreground"
    labels[Theme.DEFAULT_BACKGROUND] = "terminal.background"
    labels[Theme.CURSOR_COLOR] = "terminalCursor.foreground"
    labels[Theme.ANSI_BLACK] = "terminal.ansiBlack"
    labels[Theme.ANSI_BLACK_BOLD] = "terminal.ansiBrightBlack"
    labels[Theme.ANSI_RED] = "terminal.ansiRed"
    labels[Theme.ANSI_RED_BOLD] = "terminal.ansiBrightRed"
    labels[Theme.ANSI_GREEN] = "terminal.ansiGreen"
    labels[Theme.ANSI_GREEN_BOLD] = "terminal.ansiBrightGreen"
    labels[Theme.ANSI_YELLOW] = "terminal.ansiYellow"
    labels[Theme.ANSI_YELLOW_BOLD] = "terminal.ansiBrightYellow"
    labels[Theme.ANSI_BLUE] = "terminal.ansiBlue"
    labels[Theme.ANSI_BLUE_BOLD] = "terminal.ansiBrightBlue"
    labels[Theme.ANSI_MAGENTA] = "terminal.ansiMagenta"
    labels[Theme.ANSI_MAGENTA_BOLD] = "terminal.ansiBrightMagenta"
    labels[Theme.ANSI_CYAN] = "terminal.ansiCyan"
    labels[Theme.ANSI_CYAN_BOLD] = "terminal.ansiBrightCyan"
    labels[Theme.ANSI_WHITE] = "terminal.ansiWhite"
    labels[Theme.ANSI_WHITE_BOLD] = "terminal.ansiBrightWhite"
    labels[Theme.CURSOR_COLOR] = None
    labels[Theme.DEFAULT_BOLD_BACKGROUND] = None
    labels[Theme.CURSOR_TEXT] = None
    # Missing!
    # labels[Theme.??????????] = "terminal.selectionBackground"
