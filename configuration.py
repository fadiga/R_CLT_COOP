#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# vim: ai ts=4 sts=4 et sw=4 nu
# maintainer: Fad
from __future__ import (unicode_literals, absolute_import, division,
                        print_function)
import os
from Common.cstatic import CConstants


class Config(CConstants):
    """ docstring for Config """
    DATEFORMAT = u'%d-%m-%Y'

    def __init__(self):
        CConstants.__init__(self)

    from Common.models import Settings
    from models import (CheckList, CooperativeCompanie, Immatriculation,
                        Demande, CooperativeMember, Office)

    LSE = False
    DEBUG = False
    PEEWEE_V = 224
    ORG_LOGO = None

    ROOT_DIR = os.path.dirname(os.path.abspath('__file__'))

    AUTOR = u"IBS Mali"

    # -------- Application -----------#
    NAME_MAIN = "main.py"
    APP_NAME = "R_coop_desktop"
    APP_VERSION = 1
    APP_DATE = u"10/2018"
    ARMOIRE = "img_prod"

    des_image_record = os.path.join(ROOT_DIR, ARMOIRE)
    templates = os.path.join(ROOT_DIR, "templates")
    img_media = os.path.join(os.path.join(ROOT_DIR, "static"), "img/")
    APP_LOGO = os.path.join(img_media, "logo.png")
    APP_LOGO_ICO = os.path.join(img_media, "logo.ico")
    # BASE_URL = "http://192.168.6.6:9009"

    try:
        BASE_URL = Settings().get(Settings.id == 1).url
    except:
        BASE_URL = "https://dnds.ml"

    SERV = True
    EXCLUDE_MENU_ADMIN = []
    list_models = [Immatriculation, CooperativeMember, CooperativeCompanie,
                   Demande, CheckList, Office]
