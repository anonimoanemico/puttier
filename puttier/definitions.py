# -*- coding: utf-8 -*-

import os
from pathlib import Path


class Project:

    ROOT_DIR = Path(os.path.abspath(__file__)).parent
    DATA_DIR = os.path.join(Path.home(), ".puttier-data")
    THEMES_INI_PATH = os.path.join(ROOT_DIR, "cfg", "themes.ini")

class DescribeProject:
    @staticmethod
    def describe():
        print("ROOT_DIR={}".format(Project.ROOT_DIR))
        print("DATA_DIR={}".format(Project.DATA_DIR))
        print("THEMES_INI_PATH={}".format(Project.THEMES_INI_PATH))


DescribeProject.describe()
