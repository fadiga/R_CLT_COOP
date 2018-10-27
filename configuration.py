#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# vim: ai ts=4 sts=4 et sw=4 nu
# maintainer: Fad
from __future__ import (unicode_literals, absolute_import, division,
                        print_function)
import os
# from static import Constants
from Common.cstatic import CConstants
# from models import Spinneret, Activity, CooperativeCompanies

ROOT_DIR = os.path.dirname(os.path.abspath('__file__'))


class Config(CConstants):
    """ docstring for Config """
    DATEFORMAT = u'%d-%m-%Y'

    def __init__(self):
        CConstants.__init__(self)

    # ------------------------- Organisation --------------------------#
    LSE = False
    DEBUG = False
    PEEWEE_V = 224
    ORG_LOGO = None

    AUTOR = u"IBS Mali"

    # -------- Application -----------#
    NAME_MAIN = "main.py"
    APP_NAME = "Rep_coop"
    APP_VERSION = 1
    APP_DATE = u"10/2018"
    img_media = os.path.join(os.path.join(ROOT_DIR, "static"), "img/")
    APP_LOGO = os.path.join(img_media, "logo.png")
    APP_LOGO_ICO = os.path.join(img_media, "logo.ico")

    BASE_URL = "http://192.168.6.6:9009/"
    # BASE_URL = "http://fadcorp.ml/"
    SERV = True
    EXCLUDE_MENU_ADMIN = ["del_all"]
    SCOOPS = "a"
    COOP_CA = "b"
    UNION = "bv"
    FEDERATION = "bf"
    CONFEDERATION = "bc"
    CATEGORY = {
        SCOOPS: ("SCOOPS"),
        COOP_CA: ("COOP CA"),
        UNION: ("UNION"),
        FEDERATION: ("Fédération"),
        CONFEDERATION: ("Confédération"),
    }
