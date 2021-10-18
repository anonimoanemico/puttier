# -*- coding: utf-8 -*-
from collections import OrderedDict
from themeloader import *
from puttysessions import *
from functools import cmp_to_key
import io


class Themerepo:

    def __init__(self, name, url, is_zip, search_path, credits_url):
        self.name = name
        self.url = url
        self.is_zip = is_zip
        self.search_path = search_path
        self.credits_url = credits_url
