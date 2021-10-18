# -*- coding: utf-8 -*-

import os
import glob
import shutil
from io import BytesIO
from zipfile import ZipFile
from urllib.request import urlopen
from puttier.definitions import *
from puttier.theme import *

class ThemeLoader:
    data_path = os.path.join(os.getcwd(), Project.DATA_DIR)

    @staticmethod
    def reset_destination_dir(dest_dir):
        if not dest_dir:
            raise Exception("Error no valid folder name found")
        not os.path.exists(dest_dir) or shutil.rmtree(dest_dir)
        os.makedirs(dest_dir)

    @staticmethod
    def download_repo(repo, force = False):
        if not repo.name:
            raise Exception("Error no valid folder name found")
        dest_dir = os.path.abspath(os.path.join(ThemeLoader.data_path, repo.name)) + os.sep
        if os.path.exists(dest_dir) and not force:
            # Files already downloaded
            return
        ThemeLoader.reset_destination_dir(dest_dir)
        if repo.is_zip:
            resp = urlopen(repo.url)
            zipfile = ZipFile(BytesIO(resp.read()))
            for file in zipfile.namelist():
                if file.endswith(".reg"):
                    # and (str(repo.search_path) in str(file)):
                    zipfile.extract(file, path=ThemeLoader.data_path)
                    abs_path = os.path.abspath(os.path.join(ThemeLoader.data_path, file))
                    if os.path.isdir(abs_path):
                        print("dir found")
                        continue
                    shutil.move(abs_path, dest_dir)
            if zipfile.namelist():
                unzipped_dir = os.path.abspath(os.path.join(ThemeLoader.data_path, zipfile.namelist()[0]))
                print(unzipped_dir)
                not os.path.exists(unzipped_dir) or shutil.rmtree(unzipped_dir)
        else:
            resp = urlopen(repo.url)
            file_name = repo.url.split('/')[-1]
            dest_file = os.path.join(ThemeLoader.data_path, repo.name, file_name)
            open(dest_file, 'wb').write(resp.read())


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
    def loadFromDirectory():
        """return a dictionary of themes (key = hash of the theme, value = theme)"""
        try:
            search_expr = ThemeLoader.data_path + os.sep + "**" + os.sep + "*.reg"
            files = glob.glob(search_expr, recursive=True)
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

    @staticmethod
    def merge_two_dicts(x, y):
        """Given two dictionaries, merge them into a new dict as a shallow copy."""
        z = x.copy()
        z.update(y)
        return z

    @staticmethod
    def loadThemes(themes_repo, force_download = False):
        """return a dictionary of themes (key = hash of the theme, value = theme)"""
        if not force_download:
            return ThemeLoader.loadFromDirectory()

        theme_dict = {}
        for repo in themes_repo:
            print("Loading themes from repo: {}".format(repo.name))
            ThemeLoader.download_repo(repo, force=force_download)
            theme_dict = ThemeLoader.merge_two_dicts (theme_dict, ThemeLoader.loadFromDirectory())
        return theme_dict

def main():
    ThemeLoader.loadThemes(None, False)

if __name__ == "__main__":
    main()