from ntpath import join
import sys
import os
# -*- coding: utf-8 -*-
import glob
from theme import *
from StringIO import StringIO
from zipfile import ZipFile
from urllib import urlopen
import shutil


class ThemeLoader:
    data_path = os.path.join(os.getcwd(), "data")

    @staticmethod
    def download(repo_name, url = "https://github.com/mbadolato/iTerm2-Color-Schemes/archive/refs/heads/master.zip", force = False):
        if not repo_name:
            raise Exception("Error no valid folder name found")
        dest = os.path.join(ThemeLoader.data_path, repo_name, "putty")
        if os.path.exists(ThemeLoader.data_path) and not force:
            # Files already downloaded
            return
        if not os.path.exists(ThemeLoader.data_path):
            os.makedirs(ThemeLoader.data_path)
        resp = urlopen(url)
        zipfile = ZipFile(StringIO(resp.read()))
        last_file = None
        for file in zipfile.namelist():
            if ("/putty/") in file:
                zipfile.extract(file, path=ThemeLoader.data_path)
                last_file = file
        if last_file:
            source = os.path.join(ThemeLoader.data_path, last_file.rsplit("/",1)[0])
            shutil.rmtree(dest)
            shutil.move(source, dest)
            shutil.rmtree(source.rsplit("/",1)[0])

    @staticmethod
    def findThemeFiles(themes_path):
        if not themes_path or not os.path.exists(themes_path):
            raise Exception("Error: no theme was found")
        search_expr = os.path.join(themes_path, "putty") + os.sep + "*.reg"
        return glob.glob(search_expr)

    @staticmethod
    def readThemeFile(theme_path):
        if not theme_path:
            raise Exception("Error: File containing theme not found or not accessible")
        theme_name = theme_path.split(os.sep)[-1][:-4]
        if not theme_name:
            raise Exception("Error: Unable to parse the filename {}".format(theme_name))
        # colors dict should have 22 colors otherwise the model is invalid
        colors_dict = {}
        with open(theme_path) as f:
            for line in f.readlines():
                if not line.startswith("\"") or "=" not in line:
                    continue
                strings = line.strip().split("=", 2)
                if strings[0][1:7] != "Colour":
                    continue
                colors_index = strings[0][7:-1]
                colors_arr_str = strings[1][1:-1]
                if "," not in colors_arr_str:
                    continue
                color_arr = colors_arr_str.split(",",3)
                colors_dict[int(colors_index)] = Color(color_arr[0],color_arr[1],color_arr[2])

        if len(colors_dict) != 22:
            print("Found invalid theme file {}. Skipping".format(theme_name))
            return None
        theme = Theme(name=theme_name)
        for i in range(22):
            theme.addColor(colors_dict[i])
        return theme

    @staticmethod
    def loadThemes(force = False):
        """return a dictionary of themes (key = hash of the theme, value = theme)"""
        repo_source = "https://github.com/mbadolato/iTerm2-Color-Schemes/archive/refs/heads/master.zip"
        repo_name = repo_source.rsplit("/")[-5] # Using iTerm2-Color-Schemes as repo_name (= destination subdir)
        ThemeLoader.download(repo_name, repo_source, force=force)
        themes_fullpath = os.path.join(ThemeLoader.data_path, repo_name)
        try:
            files = ThemeLoader.findThemeFiles(themes_fullpath)
            theme_dict = {}
            for f in files:
                theme = None
                try:
                    theme = ThemeLoader.readThemeFile(f)
                except:
                    pass
                if theme is None:
                    continue
                th_hash = theme.toHash()
                theme_dict[th_hash] = theme
            print("Loaded {} themes".format(len(theme_dict)))
            return theme_dict
        except Exception as err:
            print(err)
            return {}


def main():
    # list all themes in putty/*.reg
    repo_source = "https://github.com/mbadolato/iTerm2-Color-Schemes/archive/refs/heads/master.zip"
    repo_name = repo_source.rsplit("/")[-5] # Using iTerm2-Color-Schemes as repo_name (= destination subdir)
    ThemeLoader.download(repo_name, repo_source)

if __name__ == "__main__":
    main()