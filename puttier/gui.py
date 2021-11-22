# -*- coding: utf-8 -*-

import tkinter as tk
import tkinter.font as tkFont
from tkinter import ttk
from tkinter import font
from puttier.configurator import *
import threading
import puttier.definitions as appconfig
from puttier.vstermtheme import VsTermTheme


class App:

    def __init__(self):
        self.root = tk.Tk()
        self.themes_db = dict()
        self.sessions_db = dict()
        #setting title
        self.root.title("Puttier")
        #setting window size
        max_width = 800
        width = max_width
        height = 630
        screenwidth = self.root.winfo_screenwidth()
        screenheight = self.root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height,
                                    (screenwidth - width) / 2, (screenheight - height) / 2)
        self.root.geometry(alignstr)
        self.root.resizable(width=True, height=True)

        pMain = tk.PanedWindow(self.root, orient=tk.VERTICAL)
        pMain.pack(side=tk.BOTTOM, expand=tk.Y, fill=tk.BOTH, pady=0, padx=0)

        self.f_status = tk.PanedWindow(
            pMain, orient=tk.HORIZONTAL, bd=1, relief=tk.SUNKEN, height=10)
        self.f_status.pack(side=tk.BOTTOM, expand=tk.N,
                           fill=tk.X, pady=0, padx=0)

        self.setStatusBar(self.f_status)

        top_panel = tk.PanedWindow(pMain, orient=tk.HORIZONTAL)
        top_panel.pack(side=tk.TOP, expand=tk.Y, fill=tk.BOTH, pady=0, padx=0)

        labelFrame0 = tk.LabelFrame(top_panel, text="Sessions", padx=0, pady=0)
        self.setSessionsListBox(labelFrame0)

        self.lbl_frame_themes = tk.LabelFrame(
            top_panel, text="Themes", padx=0, pady=0)
        self.setThemesListBox(self.lbl_frame_themes)

        self.lbl_frame_themes.pack(side=tk.LEFT, fill=tk.BOTH, expand=tk.Y)

        pBottom = tk.PanedWindow(pMain, orient=tk.VERTICAL)
        pBottom.pack(side=tk.BOTTOM, expand=tk.Y, fill=tk.BOTH, pady=0, padx=0)
        pBottomFont = tk.PanedWindow(pBottom, orient=tk.HORIZONTAL)
        pBottomFont.pack(side=tk.TOP, expand=tk.N,
                         fill=tk.BOTH, pady=0, padx=0)

        self.font_families = [f for f in font.families(
        ) if tkFont.Font(family=f).metrics()["fixed"] == 1]
        self.font_families.sort()

        self.setFontSelectionArea(pBottomFont)

        pBottomBottom = tk.PanedWindow(pBottom, orient=tk.HORIZONTAL)
        pBottomBottom.pack(side=tk.TOP, expand=tk.Y,
                           fill=tk.BOTH, pady=0, padx=0)

        pBottomTerminal = tk.PanedWindow(
            pBottomBottom, orient=tk.VERTICAL, height=230)
        self.setTextArea(pBottomTerminal)
        pBottomTerminal.pack(side=tk.TOP, expand=tk.Y,
                             fill=tk.BOTH, pady=0, padx=0)

        pBottomButtons = tk.PanedWindow(pBottomBottom, orient=tk.HORIZONTAL)

        self.setBottomButtons(pBottomButtons)
        pBottomButtons.pack(side=tk.BOTTOM, expand=tk.Y,
                            fill=tk.BOTH, pady=0, padx=0)

        self.root.mainloop()

    def setSessionsListBox(self, label_frame):
        self.session_listbox = tk.Listbox(label_frame)
        self.session_listbox["borderwidth"] = "1px"
        font_type = tkFont.Font(family='Verdana', size=8)
        self.session_listbox["font"] = font_type
        self.session_listbox["fg"] = "#333333"
        self.session_listbox["selectmode"] = "single"
        scrollbar_GListBox_0 = tk.Scrollbar(label_frame)
        self.session_listbox.config(
            yscrollcommand=scrollbar_GListBox_0.set, exportselection=False)
        scrollbar_GListBox_0.pack(side=tk.RIGHT, fill=tk.BOTH)
        self.session_listbox.pack(side=tk.RIGHT, fill=tk.BOTH, expand=tk.Y)
        label_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=tk.Y)
        self.session_listbox.bind("<<ListboxSelect>>", self.onSessionSelect)

    def setThemesListBox(self, label_frame):
        self.inner_theme_frame = tk.LabelFrame(
            label_frame, padx=0, pady=0, borderwidth=0, highlightthickness=0)
        self.inner_theme_frame.grid(row=0, column=0, sticky="nesw")
        label_frame.rowconfigure(0, weight=30)
        label_frame.rowconfigure(1, weight=2)
        label_frame.columnconfigure(0, weight=1)

        self.theme_listbox = tk.Listbox(self.inner_theme_frame)
        self.theme_listbox["borderwidth"] = "1px"
        ft = tkFont.Font(family='Verdana', size=8)
        self.theme_listbox["font"] = ft
        self.theme_listbox["fg"] = "#333333"
        self.theme_listbox["selectmode"] = "single"
        self.theme_listbox.bind("<<ListboxSelect>>", self.onThemeSelect)
        self.theme_listbox.bind("<Down>", self.onEntryUpDown)
        self.theme_listbox.bind("<Up>", self.onEntryUpDown)
        self.theme_listbox.place(x=0, y=0)
        scrollbar_theme_listbox = tk.Scrollbar(self.inner_theme_frame)
        self.theme_listbox.config(
            yscrollcommand=scrollbar_theme_listbox.set, exportselection=False)
        scrollbar_theme_listbox.pack(side=tk.RIGHT, fill=tk.BOTH)
        self.theme_listbox.pack(side=tk.RIGHT, fill=tk.BOTH, expand="yes")

    def setFontSelectionArea(self, panel):
        self.fontCombo = ttk.Combobox(panel, height=20, state="readonly",
                                      values=self.font_families)
        label = ttk.Label(panel, text="Font Family:")
        label.pack(side=tk.LEFT, fill=tk.BOTH, pady=0, padx=0)
        default_font_family = "Consolas"
        if default_font_family in self.font_families:
            self.fontCombo.current(
                self.font_families.index(default_font_family))
        self.fontCombo.pack(side=tk.LEFT, fill=tk.BOTH, pady=0, padx=0)
        self.fontCombo.bind("<<ComboboxSelected>>", self.onSelectFontFamily)

        label = ttk.Label(panel, text="Font Size:")
        label.pack(side=tk.LEFT, fill=tk.BOTH, pady=0, padx=0)
        self.fontSizeCombo = ttk.Combobox(panel, height=20, state="readonly",
                                          values=list(range(4, 28)))
        self.fontSizeCombo.current(1)
        self.fontSizeCombo.pack(side=tk.LEFT, fill=tk.BOTH, pady=0, padx=0)
        self.fontSizeCombo.bind("<<ComboboxSelected>>", self.onSelectFontSize)

    def updateVsCodeExport(self):
        self.btn_copy_vs_json["state"] = tk.NORMAL

    def setStatusBar(self, panel):
        self.statusMsg = tk.StringVar()
        self.setStatusMessage("Ready")
        self.statusBar = tk.Label(
            panel, textvariable=self.statusMsg, anchor=tk.W)
        self.statusBar.pack(side=tk.LEFT, fill=tk.X)

    def setProgressBar(self, panel):
        self.progress_bar = ttk.Progressbar(
            panel, orient=tk.HORIZONTAL, mode='indeterminate', value=0)
        self.progress_bar.pack(side=tk.RIGHT, fill=tk.X)

    def setStatusMessage(self, message):
        self.statusMsg.set(message)

    def setTextArea(self, panel):
        self.text_area = tk.Text(panel, height=160, width=120)
        ft = tkFont.Font(family='Consolas', size=8)
        self.text_area["font"] = ft
        panel.pack_propagate(0)
        self.text_area.pack_propagate(0)
        self.text_area.insert(tk.INSERT,
                              """ user@machine  ~/project/target  ls --color=auto -al
total 1944
drwxr-xr-x 13 user user    4096 Oct  9 22:36 .
drwxr-xr-x  4 root root    4096 Dec 13  2016 ..
-rw-------  1 user user   24880 Oct  2 08:44 .bash_history
-rw-r--r--  1 user user    3567 Dec  5  2018 .bashrc
lrwxrwxrwx  1 user user      12 Oct  9 22:35 broken_link -> removed_path
drwx------  5 user user    4096 Dec 14  2016 .cache
drwxr-xr-x  5 user user    4096 Feb 15  2018 ftp
lrwxrwxrwx  1 user user       3 Oct  9 22:36 ftp_link -> ftp
drwxr-xr-x  6 user user    4096 Feb 17  2021 project
drwxrwxrwx  3 user user    4096 Dec 14  2016 public
-rw-r--r--  1 user user  174080 Sep  2  2013 ssocr-2.14.1.tar
-rwxr-xr-x  1 user user      40 Apr 27 20:32 stop_ucounter_svc.sh
""")
        self.text_area.insert(tk.END, "\n")
        scrollbar_text_area = tk.Scrollbar(panel)
        self.text_area.config(
            yscrollcommand=scrollbar_text_area.set, exportselection=False)
        scrollbar_text_area.pack(side=tk.RIGHT, fill=tk.BOTH)
        self.text_area.pack(side=tk.LEFT, expand=tk.N, fill=tk.Y)
        self.text_area.config(state=tk.DISABLED)

    def setBottomButtons(self, panel):
        self.btn_load = tk.Button(panel)
        self.btn_load["bg"] = "#efefef"
        ft = tkFont.Font(family='Verdana', size=8)
        self.btn_load["font"] = ft
        self.btn_load["fg"] = "#000000"
        self.btn_load["text"] = "Load"
        self.btn_load.place(x=0, y=0, width=100, height=25)
        self.btn_load["command"] = self.btnLoadCommand

        btn_update = tk.Button(panel)
        btn_update["bg"] = "#efefef"
        ft = tkFont.Font(family='Verdana', size=8)
        btn_update["font"] = ft
        btn_update["fg"] = "#000000"
        btn_update["text"] = "Update"
        btn_update.place(x=110, y=0, width=120, height=25)
        btn_update["command"] = self.btnUpdateCommand

        self.btn_download = tk.Button(panel)
        self.btn_download["bg"] = "#efefef"
        ft = tkFont.Font(family='Verdana', size=8)
        self.btn_download["font"] = ft
        self.btn_download["fg"] = "#000000"
        self.btn_download["text"] = "Download Themes"
        self.btn_download.place(x=240, y=0, width=130, height=25)
        self.btn_download["command"] = self.btnDownloadCommand
        self.btn_download["state"] = tk.DISABLED

        self.btn_copy_vs_json = tk.Button(panel)
        self.btn_copy_vs_json["bg"] = "#efefef"
        ft = tkFont.Font(family='Verdana', size=8)
        self.btn_copy_vs_json["font"] = ft
        self.btn_copy_vs_json["fg"] = "#000000"
        self.btn_copy_vs_json["text"] = "Copy VSCode Json"
        self.btn_copy_vs_json.place(x=380, y=0, width=130, height=25)
        self.btn_copy_vs_json["command"] = self.btnCopyCommand
        self.btn_copy_vs_json["state"] = tk.DISABLED

    def loadSessions(self):
        self.sessions_db = Configurator.loadSessions(themes_db=self.themes_db)
        self.session_listbox.delete(0, tk.END)
        index = 0
        for session, theme_name in self.sessions_db.items():
            session_name = session.name.replace("%20", " ")
            self.session_listbox.insert(
                index, "{} ({})".format(session_name, theme_name))
            index = index + 1
        self.session_listbox.pack(side=tk.RIGHT, fill=tk.BOTH, expand="yes")

    def lockThemes(self):
        self.theme_listbox.configure(state=tk.DISABLED)

    def unlockThemes(self):
        self.theme_listbox.configure(state=tk.NORMAL)

    def loadThemes(self, themes_db=None):
        if not themes_db:
            self.themes_db = Configurator.loadThemes()
        else:
            self.themes_db = themes_db
        self.theme_listbox.delete(0, tk.END)
        index = 0
        for hash, theme in self.themes_db.items():
            self.theme_listbox.insert(index, theme.name)
            index = index + 1
        self.theme_listbox.pack(side=tk.RIGHT, fill=tk.BOTH, expand="yes")
        self.setStatusMessage("Loaded {} themes".format(len(self.themes_db)))

    def btnLoadCommand(self):
        self.loadThemes()
        self.loadSessions()
        self.btn_download["state"] = tk.ACTIVE

    def getSelectedSession(self):
        selected_session_idx = None if not self.session_listbox.curselection(
        ) else self.session_listbox.curselection()[0]
        session_instance = None
        if selected_session_idx is not None and self.sessions_db:
            session_instance = (list(self.sessions_db.keys())[
                                selected_session_idx])
        return session_instance

    def getSelectedTheme(self):
        theme_instance = None
        selected_theme_idx = None if not self.theme_listbox.curselection(
        ) else self.theme_listbox.curselection()[0]
        if selected_theme_idx is not None:
            theme_instance = (list(self.themes_db.values())
                              [selected_theme_idx])
        return theme_instance

    def btnUpdateCommand(self):
        selected_session_idx = None if not self.session_listbox.curselection(
        ) else self.session_listbox.curselection()[0]
        session_instance = self.getSelectedSession()
        session_name = session_instance.name if session_instance else None
        theme_instance = self.getSelectedTheme()
        font_family = self.fontCombo.get()
        font_size = self.fontSizeCombo.get()
        if (session_name and theme_instance):
            PuttyUpdate.updateSession(
                session_name, theme_instance, font_family, font_size)
            self.loadSessions()
            # reselect previously selected session
            self.session_listbox.select_set(selected_session_idx)
            self.session_listbox.see(selected_session_idx)
            self.setStatusMessage("Theme {} saved for session {}" .format(
                theme_instance.name, session_name))
        elif not session_name:
            self.setStatusMessage("No Session selected")
        else:
            self.setStatusMessage("No Theme selected")

    def forceUpdateThemesAndSessionsAfterFinish(self, themes_db):
        self.loadThemes(themes_db)
        self.loadSessions()
        self.unlockThemes()
        self.stopDownload()

    def forceUpdateThemesAndSessionsStart(self):
        self.startDownload()
        themes_db = Configurator.loadThemes(force_download=True)
        self.forceUpdateThemesAndSessionsAfterFinish(themes_db)

    def startDownload(self):
        self.setStatusMessage("Downloading themes defined in Theme.ini")
        self.setProgressBar(self.f_status)
        self.progress_bar.start()

    def stopDownload(self):
        self.progress_bar.stop()
        self.progress_bar.pack_forget()
        self.setStatusMessage("Download finished")

    def forceUpdateThemesAndSessions(self):
        self.lockThemes()
        td = threading.Thread(target=self.forceUpdateThemesAndSessionsStart)
        td.daemon = True
        td.start()

    def btnDownloadCommand(self):
        self.btn_download.after(1000, self.forceUpdateThemesAndSessions())

    def btnCopyCommand(self):
        theme_instance = self.getSelectedTheme()
        if theme_instance is None:
            self.setStatusMessage("No theme selected")
            return
        vstheme = VsTermTheme(theme_instance)
        font_family = self.fontCombo.get()
        font_size = self.fontSizeCombo.get()
        json = vstheme.export(font_family, font_size)
        self.root.clipboard_clear()
        self.root.clipboard_append(json)
        self.setStatusMessage(
            "Json of theme {} is now in the clipboard".format(theme_instance.name))

    def onEntryUpDown(self, event):
        selection = event.widget.curselection()[0]
        if event.keysym == 'Up':
            selection += -1
        if event.keysym == 'Down':
            selection += 1
        if 0 <= selection < event.widget.size():
            event.widget.selection_clear(0, tk.END)
            event.widget.select_set(selection)
            event.widget.event_generate('<<ListboxSelect>>')

    def onSessionSelect(self, evt):
        session_instance = self.getSelectedSession()
        if not session_instance:
            return

        if session_instance and session_instance.font and session_instance.font_size:
            self.fontCombo.current(
                self.font_families.index(session_instance.font))
            curr_font_size = int(session_instance.font_size)
            if curr_font_size < 28 and curr_font_size > 4:
                self.fontSizeCombo.current(str(curr_font_size - 4))

        session_hash = session_instance.theme.toHash()
        self.theme_listbox.selection_clear(0, 'end')
        theme_index = 0
        if session_hash in self.themes_db:
            theme_index = (list(self.themes_db.keys())).index(session_hash)
        self.theme_listbox.select_set(theme_index)
        self.theme_listbox.see(theme_index)
        self.theme_listbox.event_generate('<<ListboxSelect>>')

    def onThemeSelect(self, evt):
        theme_instance = self.getSelectedTheme()
        session_instance = self.getSelectedSession()
        ft = tkFont.Font(family=self.fontCombo.get(),
                         size=self.fontSizeCombo.get())
        self.text_area["font"] = ft

        if theme_instance is None:
            return
        self.text_area["bg"] = theme_instance.getColorHex(
            Theme.DEFAULT_BACKGROUND)
        self.text_area["fg"] = theme_instance.getColorHex(
            Theme.DEFAULT_FOREGROUND)
        self.text_area.tag_add("user", "1.0", "1.14")
        self.text_area.tag_add("band", "1.14", "1.33")
        self.text_area.tag_add(">", "1.33", "1.34")
        self.text_area.tag_add("di", "3.45", "3.46")
        self.text_area.tag_add("di", "4.45", "4.47")
        self.text_area.tag_add("or", "7.45", "7.56")
        self.text_area.tag_add("or", "7.60", "7.76")
        self.text_area.tag_add("di", "8.45", "8.51")
        self.text_area.tag_add("di", "9.45", "9.48")
        self.text_area.tag_add("ln", "10.45", "10.54")
        self.text_area.tag_add("di", "10.57", "10.67")
        self.text_area.tag_add("di", "11.45", "11.52")
        self.text_area.tag_add("dp", "12.45", "12.51")
        self.text_area.tag_add("ar", "13.45", "13.61")
        self.text_area.tag_add("ex", "14.45", "14.65")
        self.text_area.tag_config("user", foreground=theme_instance.getColorHex(
            Theme.ANSI_WHITE), background=theme_instance.getColorHex(Theme.ANSI_BLACK))
        self.text_area.tag_config("band", foreground=theme_instance.getColorHex(
            Theme.ANSI_BLACK), background=theme_instance.getColorHex(Theme.ANSI_BLUE))
        self.text_area.tag_config(
            ">", foreground=theme_instance.getColorHex(Theme.ANSI_BLUE))
        self.text_area.tag_config(
            "di", foreground=theme_instance.getColorHex(Theme.ANSI_BLUE_BOLD))
        self.text_area.tag_config("or", foreground=theme_instance.getColorHex(
            Theme.ANSI_RED_BOLD), background=theme_instance.getColorHex(Theme.ANSI_BLACK))
        self.text_area.tag_config(
            "ln", foreground=theme_instance.getColorHex(Theme.ANSI_CYAN_BOLD))
        self.text_area.tag_config("dp", foreground=theme_instance.getColorHex(
            Theme.ANSI_BLUE), background=theme_instance.getColorHex(Theme.ANSI_GREEN))
        self.text_area.tag_config(
            "ar", foreground=theme_instance.getColorHex(Theme.ANSI_RED_BOLD))
        self.text_area.tag_config(
            "ex", foreground=theme_instance.getColorHex(Theme.ANSI_GREEN_BOLD))
        self.updateVsCodeExport()

    def onSelectFontFamily(self, evt):
        self.onThemeSelect(evt)

    def onSelectFontSize(self, evt):
        self.onThemeSelect(evt)


def main():
    theApp = App()


if __name__ == "__main__":
    main()
