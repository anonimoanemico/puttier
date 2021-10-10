import tkinter as tk
import tkinter.font as tkFont
from puttier import *

class App:
    def __init__(self, root):
        self.themes_db = dict()
        self.sessions_db = dict()
        #setting title
        root.title("Puttier")
        #setting window size
        width=800
        height=500
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        main_panel = tk.PanedWindow(root, orient=tk.VERTICAL)
        main_panel.pack(side=tk.TOP, expand=tk.Y, fill=tk.BOTH, pady=0, padx=0)

        top_panel = tk.PanedWindow(main_panel, orient=tk.HORIZONTAL)
        top_panel.pack(side=tk.TOP, expand=tk.Y, fill=tk.BOTH, pady=0, padx=0)

        labelFrame0 = tk.LabelFrame(top_panel, text="Sessions", padx=0, pady=0)

        self.session_listbox=tk.Listbox(labelFrame0)
        self.session_listbox["borderwidth"] = "1px"
        ft = tkFont.Font(family='Verdana',size=8)
        self.session_listbox["font"] = ft
        self.session_listbox["fg"] = "#333333"
        #self.session_listbox["justify"] = "left"
        self.session_listbox.place(x=0,y=0,width=300,height=291)
        self.session_listbox["selectmode"] = "single"
        scrollbar_GListBox_0 = tk.Scrollbar(labelFrame0)
        self.session_listbox.config(yscrollcommand = scrollbar_GListBox_0.set, exportselection=False)
        scrollbar_GListBox_0.pack(side = tk.RIGHT, fill = tk.BOTH)
        self.session_listbox.pack(side = tk.RIGHT, fill = tk.BOTH, expand="yes")
        labelFrame0.pack(side=tk.LEFT, fill = tk.BOTH, expand="yes")
        self.session_listbox.bind("<<ListboxSelect>>", self.onSessionSelect)

        labelFrame1 = tk.LabelFrame(top_panel, text="Themes", padx=0, pady=0)

        self.theme_listbox=tk.Listbox(labelFrame1)
        self.theme_listbox["borderwidth"] = "1px"
        ft = tkFont.Font(family='Verdana',size=8)
        self.theme_listbox["font"] = ft
        self.theme_listbox["fg"] = "#333333"
        #self.theme_listbox["justify"] = "left"
        self.theme_listbox["selectmode"] = "single"
        self.theme_listbox.bind("<<ListboxSelect>>", self.onThemeSelect)
        self.theme_listbox.bind("<Down>", self.OnEntryUpDown)
        self.theme_listbox.bind("<Up>", self.OnEntryUpDown)

        self.theme_listbox.place(x=0,y=0,width=300,height=291)
        scrollbar_GListBox_1 = tk.Scrollbar(labelFrame1)
        self.theme_listbox.config(yscrollcommand = scrollbar_GListBox_1.set, exportselection=False)
        scrollbar_GListBox_1.pack(side = tk.RIGHT, fill = tk.BOTH)
        self.theme_listbox.pack(side = tk.RIGHT, fill = tk.BOTH, expand="yes")
        labelFrame1.pack(side=tk.LEFT, fill = tk.BOTH, expand="yes")

        pBottom = tk.PanedWindow(main_panel, orient=tk.HORIZONTAL)
        pBottomTerminal = tk.PanedWindow(pBottom, orient=tk.VERTICAL)

        self.text_area = tk.Text(pBottomTerminal, height=12)
        ft = tkFont.Font(family='Consolas',size=8)
        self.text_area["font"] = ft
        self.text_area.pack()
        self.text_area.insert(tk.INSERT, 
"""user@machine~> ls --color=auto -al
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
        scrollbar_text_area = tk.Scrollbar(pBottomTerminal)
        self.text_area.config(yscrollcommand = scrollbar_text_area.set, exportselection=False)
        scrollbar_text_area.pack(side = tk.RIGHT, fill = tk.BOTH)
        self.text_area.pack(side=tk.LEFT, expand=tk.Y, fill=tk.BOTH)
        pBottomTerminal.pack(side=tk.TOP, expand=tk.Y, fill=tk.BOTH, pady=0, padx=0)

        pBottomButtons = tk.PanedWindow(pBottom, orient=tk.HORIZONTAL, height=15)
        pBottomButtons.pack(side=tk.TOP, expand=tk.Y, fill=tk.BOTH, pady=0, padx=0)
        GButton_687=tk.Button(pBottomButtons)
        GButton_687["bg"] = "#efefef"
        ft = tkFont.Font(family='Verdana',size=8)
        GButton_687["font"] = ft
        GButton_687["fg"] = "#000000"
        # GButton_687["justify"] = "center"
        GButton_687["text"] = "Load"
        GButton_687.place(x=0,y=0,width=100,height=25)
        GButton_687["command"] = self.GButton_687_command

        GButton_46=tk.Button(pBottomButtons)
        GButton_46["bg"] = "#efefef"
        ft = tkFont.Font(family='Verdana',size=8)
        GButton_46["font"] = ft
        GButton_46["fg"] = "#000000"
        # GButton_46["justify"] = "center"
        GButton_46["text"] = "Update"
        GButton_46.place(x=110,y=0,width=120,height=25)
        GButton_46["command"] = self.GButton_46_command
        pBottomButtons.pack(side=tk.TOP, expand=tk.Y, fill=tk.BOTH, pady=0, padx=0)
        pBottom.pack(side=tk.TOP, expand=tk.Y, fill=tk.BOTH, pady=0, padx=0)


    def loadSessions(self):
        self.sessions_db = Puttier.loadSessions(self.themes_db)
        self.session_listbox.delete(0,tk.END)
        index = 0
        for session, theme_name in self.sessions_db.items():
            self.session_listbox.insert(index, "{} ({})".format(session.name, theme_name))
            index = index + 1
        self.session_listbox.pack(side = tk.RIGHT, fill = tk.BOTH, expand="yes")

    def loadThemes(self):
        self.themes_db = Puttier.loadThemes()
        self.theme_listbox.delete(0,tk.END)
        index = 0
        for hash, theme in self.themes_db.items():
            self.theme_listbox.insert(index, theme.name)
            index = index + 1
        self.theme_listbox.pack(side = tk.RIGHT, fill = tk.BOTH, expand="yes")

    def GButton_687_command(self):
        self.loadThemes()
        self.loadSessions()

    def getSelectedSession(self):
        selected_session_idx = None if not self.session_listbox.curselection() else self.session_listbox.curselection()[0]
        session_instance = None
        if (selected_session_idx is not None and self.sessions_db):
            session_instance = (list(self.sessions_db.keys())[selected_session_idx])
        return session_instance

    def getSelectedTheme(self):
        theme_instance = None
        selected_theme_idx = None if not self.theme_listbox.curselection() else self.theme_listbox.curselection()[0]
        if (selected_theme_idx is not None):
            theme_instance = (list(self.themes_db.values())[selected_theme_idx])
        return theme_instance


    def GButton_46_command(self):
        selected_session_idx = None if not self.session_listbox.curselection() else self.session_listbox.curselection()[0]
        session_instance = self.getSelectedSession()
        session_name = session_instance.name if session_instance else None
        theme_instance = self.getSelectedTheme()
        if (session_name and theme_instance):
            PuttyUpdate.updateSession(session_name, theme_instance)
            self.loadSessions()
            # reselect previously selected session
            self.session_listbox.select_set(selected_session_idx)
            self.session_listbox.see(selected_session_idx)
        elif not session_name:
            print("No Session selected")
        else:
            print("No Theme selected")

    def OnEntryUpDown(self, event):
        selection = event.widget.curselection()[0]
        if event.keysym == 'Up':
            selection += -1
        if event.keysym == 'Down':
            selection += 1
        if 0 <= selection < event.widget.size():
            event.widget.selection_clear(0, tk.END)
            event.widget.select_set(selection)
            event.widget.event_generate('<<ListboxSelect>>');

    def onSessionSelect(self, evt):
        session_instance = self.getSelectedSession()
        if not session_instance:
            return
        session_hash = session_instance.theme.toHash()
        self.theme_listbox.selection_clear(0, 'end')
        theme_index = 0
        if session_hash in self.themes_db:
            theme_index = (list(self.themes_db.keys())).index(session_hash)
        self.theme_listbox.select_set(theme_index)
        self.theme_listbox.see(theme_index)
        self.theme_listbox.event_generate('<<ListboxSelect>>');

    def onThemeSelect(self, evt):
        theme_instance = self.getSelectedTheme()
        self.text_area["bg"] = theme_instance.getColorHex(Theme.DEFAULT_BACKGROUND)
        self.text_area["fg"] = theme_instance.getColorHex(Theme.DEFAULT_FOREGROUND)
        self.text_area.tag_add("user", "1.0", "1.4")
        self.text_area.tag_add("machine", "1.5", "1.13")
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
        self.text_area.tag_config("user", foreground=theme_instance.getColorHex(Theme.ANSI_YELLOW))
        self.text_area.tag_config("machine", foreground=theme_instance.getColorHex(Theme.ANSI_BLUE))
        self.text_area.tag_config("di", foreground=theme_instance.getColorHex(Theme.ANSI_BLUE_BOLD))
        self.text_area.tag_config("or", foreground=theme_instance.getColorHex(Theme.ANSI_RED_BOLD), background=theme_instance.getColorHex(Theme.ANSI_BLACK))
        self.text_area.tag_config("ln", foreground=theme_instance.getColorHex(Theme.ANSI_CYAN_BOLD))
        self.text_area.tag_config("dp", foreground=theme_instance.getColorHex(Theme.ANSI_BLUE), background=theme_instance.getColorHex(Theme.ANSI_GREEN))
        self.text_area.tag_config("ar", foreground=theme_instance.getColorHex(Theme.ANSI_RED_BOLD))
        self.text_area.tag_config("ex", foreground=theme_instance.getColorHex(Theme.ANSI_GREEN_BOLD))

if __name__ == "__main__":
    root = tk.Tk()
    theApp = App(root)
    root.mainloop()
