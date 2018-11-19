#!/usr/bin/env python
# -*- coding: utf-8 -*-
# maintainer: fad

from __future__ import (unicode_literals, absolute_import, division,
                        print_function)


# from PyQt5.QtWidgets import QAction
# from PyQt5.QtGui import (QIcon, QPixmap)
# from PyQt5.QtCore import pyqtSignal

from PyQt4.QtGui import (QMessageBox, QIcon, QAction, QPixmap)
from PyQt4.QtCore import SIGNAL

from configuration import Config
from Common.ui.common import FWidget
from Common.ui.cmenubar import FMenuBar
from ui.dashboard import DashbordViewWidget
from ui.registration_view import RegistrationViewWidget
from ui.registration_manager import ResgistrationManagerWidget
from ui.cooperative_society_view import CooperativeSocietyViewWidget


class MenuBar(FMenuBar, FWidget):

    def __init__(self, parent=None, admin=False, *args, **kwargs):
        FMenuBar.__init__(self, parent=parent, *args, **kwargs)

        self.setWindowIcon(QIcon(QPixmap("{}".format(Config.APP_LOGO))))
        self.parent = parent

        menu = [
            {"name": u"Table de Bord", "icon": 'dashboard', "admin":
             False, "shortcut": "Ctrl+T", "goto": DashbordViewWidget},
            {"name": u"Ajout demande", "icon": 'demande', "admin":
             False, "shortcut": "Alt+D", "goto": RegistrationViewWidget},
            {"name": u"Gestion demande", "icon": 'gestion_dmd', "admin":
             False, "shortcut": "Ctrl+D", "goto": ResgistrationManagerWidget},
            {"name": u"Cooperatives", "icon": 'scoop', "admin":
             False, "shortcut": "Ctrl+C", "goto": CooperativeSocietyViewWidget},
        ]

        # Menu aller à
        goto_ = self.addMenu(u"&Aller a")

        for m in menu:
            el_menu = QAction(
                QIcon("{}{}.png".format(Config.img_media, m.get('icon'))), m.get('name'), self)
            el_menu.setShortcut(m.get("shortcut"))
            self.connect(
                el_menu, SIGNAL("triggered()"), lambda m=m: self.goto(m.get('goto')))
            goto_.addSeparator()
            goto_.addAction(el_menu)

        settings = QAction(u"Serveur", self)
        settings.setShortcut("Ctrl+S")
        self.connect(settings, SIGNAL("triggered()"),
                     self.goto_settings)

        settings_m = self.addMenu(u"Configurations")
        settings_m.addAction(settings)

        # Menu Aide
        help_ = self.addMenu(u"Aide")
        help_.addAction(QIcon("{}help.png".format(Config.img_cmedia)),
                        "Aide", self.goto_help)
        help_.addAction(QIcon("{}info.png".format(Config.img_cmedia)),
                        u"À propos", self.goto_about)

    def goto(self, goto):
        self.change_main_context(goto)

    def goto_settings(self):
        from ui.settingsView import SettingsDialog
        self.change_main_context(SettingsDialog)

    # Aide
    def goto_help(self):
        pass
        # from ui.help import HTMLEditor
        # self.open_dialog(HTMLEditor, modal=True)
