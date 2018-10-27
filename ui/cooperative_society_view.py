#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# vim: ai ts=4 sts=4 et sw=4 nu
# maintainer: Fad
from __future__ import (
    unicode_literals, absolute_import, division, print_function)

from datetime import datetime
from PyQt4.QtGui import (QVBoxLayout, QIcon, QTableWidgetItem)

from Common.tabpane import tabbox
from Common.ui.common import FWidget, FPageTitle, FBoxTitle, LineEdit
from Common.ui.table import FTableWidget
from Common.ui.util import (show_date, formatted_number,
                            date_on_or_end)

# from models import Invoice, Reports
from configuration import Config


class CooperativeSocietyViewWidget(FWidget):

    """ Shows the home page  """

    def __init__(self, parent=0, *args, **kwargs):
        super(CooperativeSocietyViewWidget, self).__init__(
            parent=parent, *args, **kwargs)

        self.parentWidget().set_window_title("FORMULAIRE DE DEMANDE D’IMMATRICULATION")
