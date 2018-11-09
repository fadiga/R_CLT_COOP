#!/usr/bin/env python
# -*- coding: utf-8 -*-
# maintainer: Fad

from PyQt4.QtCore import QDate
from PyQt4.QtGui import (QVBoxLayout, QDialog, QDateEdit,
                         QTextEdit, QFormLayout, QComboBox)

from Common.ui.util import check_is_empty, field_error
from Common.ui.common import (
    FWidget, Button, FormLabel, LineEdit, IntLineEdit)


class ImmatriculationSCoopDialog(QDialog, FWidget):

    def __init__(self, table_p, parent, scoop=None, member=None, *args, **kwargs):
        FWidget.__init__(self, parent, *args, **kwargs)
