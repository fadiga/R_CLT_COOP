#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: ai ts=4 sts=4 et sw=4 nu
# maintainer: Fadiga

from __future__ import (
    unicode_literals, absolute_import, division, print_function)

import os
import sys

sys.path.append(os.path.abspath('../'))

from PyQt4.QtGui import QApplication

from Common.ui.window import FWindow
from Common.cmain import cmain
from Common.ui.qss import theme

from migrations import make_migrate
from ui.mainwindow import MainWindow

app = QApplication(sys.argv)


def main():
    window = MainWindow()
    window.setStyleSheet(theme)
    setattr(FWindow, 'window', window)
    # window.show()
    window.showMaximized()
    sys.exit(app.exec_())

if __name__ == '__main__':
    if cmain():
        make_migrate()
        from models import Settings
        if Settings().select().count() == 0:
            from PyQt4.QtGui import QDialog
            from ui.settingsView import NewOrEditSettingsViewWidget
            if not NewOrEditSettingsViewWidget().exec_() == QDialog.Accepted:
                sys.exit(0)
        main()
