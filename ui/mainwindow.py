#!/usr/bin/env python
# -*- coding: utf-8 -*-
# maintainer: Fad
from __future__ import (unicode_literals, absolute_import, division,
                        print_function)

import os
import sys

sys.path.append(os.path.abspath('../'))
from PyQt4.QtGui import QIcon
from PyQt4.QtCore import Qt

from Common.ui.common import FMainWindow

from configuration import Config

from ui.dashboard import DashbordViewWidget
from ui.menutoolbar import MenuToolBar
from ui.menubar import MenuBar


class MainWindow(FMainWindow):

    def __init__(self):
        FMainWindow.__init__(self)

        self.setWindowIcon(QIcon.fromTheme(
            'logo', QIcon(u"{}".format(Config.APP_LOGO))))

        self.menubar = MenuBar(self)
        self.setMenuBar(self.menubar)
        self.toolbar = MenuToolBar(self)
        self.addToolBar(Qt.LeftToolBarArea, self.toolbar)

        self.change_context(DashbordViewWidget)

    def page_width(self):
        return self.width() - 100

    def exit(self):
        # print("exit")
        self.logout()
        self.close()
