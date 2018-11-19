#!/usr/bin/env python
# -*- coding: utf-8 -*-
# maintainer: Fad

from datetime import datetime
from PyQt4.QtCore import QDate
from PyQt4.QtGui import (QVBoxLayout, QDialog, QDateEdit,
                         QFormLayout, QComboBox)

from Common.ui.util import check_is_empty, field_error
from Common.ui.common import (
    FWidget, Button, FormLabel, LineEdit, IntLineEdit, FormatDate)
import peewee
from models import CooperativeCompanie

# from configuration import Config


class CooperativeSocietyDialog(QDialog, FWidget):

    def __init__(self, parent, scoop=None, *args, **kwargs):
        FWidget.__init__(self, parent, *args, **kwargs)

        self.scoop = scoop

        vbox = QVBoxLayout()
        self.setLayout(vbox)
