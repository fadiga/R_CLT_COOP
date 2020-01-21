# !/usr/bin/env python
# -*- coding: utf-8 -*-
# maintainer: fad

from __future__ import (
    unicode_literals, absolute_import, division, print_function)

from PyQt4.QtGui import (QIcon, QToolBar, QFont, QCursor)
from PyQt4.QtCore import Qt, QSize

from configuration import Config
from Common.ui.common import FWidget

from ui.dashboard import DashbordViewWidget
from ui.registration_view import RegistrationViewWidget
from ui.registration_manager import ResgistrationManagerWidget
from ui.cooperative_society_view import CooperativeSocietyViewWidget


class MenuToolBar(QToolBar, FWidget):

    def __init__(self, parent=None, admin=False, *args, **kwargs):
        QToolBar.__init__(self, parent, *args, **kwargs)

        self.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.setIconSize(QSize(30, 30))

        font = QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.setFont(font)
        self.setCursor(QCursor(Qt.PointingHandCursor))
        self.setAcceptDrops(True)
        self.setAutoFillBackground(True)
        # Menu File
        self.setOrientation(Qt.Horizontal)
        self.addAction(
            QIcon(u"{}exit.png".format(Config.img_cmedia)),
            u"Quiter", self.goto_exit)
        menu = [
            {"name": u"Enregister une Demande", "icon": 'add',
             "admin": False, "goto": RegistrationViewWidget},
            {"name": u"Demandes en cours", "icon": 'report',
             "admin": False, "goto": ResgistrationManagerWidget},
            {"name": u"Répertoire Coopératives", "icon": 'cooperatives',
             "admin": False, "goto": CooperativeSocietyViewWidget},
            {"name": u"Tableau de bord", "icon": 'dashboard',
             "admin": False, "goto": DashbordViewWidget},
        ]
        # self.addSeparator()
        for m in menu:
            self.addSeparator()
            self.addAction(QIcon(
                "{}{}.png".format(Config.img_media, m.get('icon'))),
                m.get('name'), lambda m=m: self.goto(m.get('goto')))

    def goto(self, goto):
        self.change_main_context(goto)

    def goto_exit(self):
        self.parent().exit()
