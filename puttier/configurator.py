# -*- coding: utf-8 -*-

import configparser
from collections import OrderedDict
from functools import cmp_to_key
from puttier.definitions import *
from puttier.themerepo import Themerepo
from puttier.themeloader import *
from puttier.puttysessions import *


class Configurator:

    @staticmethod
    def loadThemes(force_download=False):
        themes_repo = Configurator.loadConfiguration()
        themes_db = ThemeLoader.loadThemes(themes_repo, force_download)
        default_theme = Theme.default()
        themes_db[default_theme.toHash()] = default_theme
        return themes_db

    @staticmethod
    def loadSessions(themes_db=None):
        putty_sessions = sorted(
            list(PuttyLoader.sessions()), key=cmp_to_key(PuttySession.compare))
        sessions_dict = OrderedDict()
        for index, s in enumerate(putty_sessions):
            known_theme = None
            th_hash = s.theme.toHash()
            if themes_db:
                if th_hash in themes_db:
                    known_theme = themes_db[th_hash].name
            sessions_dict[s] = known_theme
        return sessions_dict

    @staticmethod
    def loadConfiguration():
        # Themerepo
        themes_repo = list()
        # Load the configuration file
        config = configparser.ConfigParser()
        config.read_file(open(Project.THEMES_INI_PATH))

        for section in config.sections():
            name = section
            url = config.get(section, "url")
            is_zip = True if url.endswith(".zip") else False
            search_path = None if not is_zip else config.get(
                section, "search_path")
            credits_url = config.get(section, "credits")
            themes_repo.append(
                Themerepo(name, url, is_zip, search_path, credits_url))
        return themes_repo
