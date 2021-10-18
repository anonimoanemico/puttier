# -*- coding: utf-8 -*-
from functools import cmp_to_key
from puttier.themeloader import *
from puttier.puttysessions import *


class Themerepo:

    def __init__(self, name, url, is_zip, search_path, credits_url):
        self.name = name
        self.url = url
        self.is_zip = is_zip
        self.search_path = search_path
        self.credits_url = credits_url
