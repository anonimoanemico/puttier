# -*- coding: utf-8 -*-

import os
from pathlib import Path

class Project:

    ROOT_DIR = Path(os.path.abspath(__file__)).parent.parent
    THEMES_INI_PATH = os.path.join(ROOT_DIR, "themes.ini")
    DATA_DIR = os.path.join(ROOT_DIR, "data")
