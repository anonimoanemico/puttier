# -*- coding: utf-8 -*-

import os
from pathlib import Path

class Project:

    ROOT_DIR = Path(os.path.abspath(__file__)).parent
    DATA_DIR = os.path.join(Path.home(), ".puttier-data")
    THEMES_INI_PATH = os.path.join(ROOT_DIR, "cfg", "themes.ini")
