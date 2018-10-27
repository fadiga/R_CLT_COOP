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


class DashbordViewWidget(FWidget):

    """ Shows the home page  """

    def __init__(self, parent=0, *args, **kwargs):
        super(DashbordViewWidget, self).__init__(
            parent=parent, *args, **kwargs)

        self.parentWidget().set_window_title("TABLEAU DE BORD")

        self.parent = parent
        vbox = QVBoxLayout()
        table_invoice = QVBoxLayout()
        table_alert = QVBoxLayout()
        table_mouvement = QVBoxLayout()

        self.search_field = LineEdit()
        self.search_field.setToolTip("Rechercher un produit")
        self.search_field.setMaximumSize(
            500, self.search_field.maximumSize().height())
        self.search_field.textChanged.connect(self.finder)

        self.title = FPageTitle("TABLEAU DE BORD")

        self.title_alert = FBoxTitle(u"Les alertes ")
        self.table_alert = AlertTableWidget(parent=self)
        # table_alert.addWidget(self.title_alert)
        table_alert.addWidget(self.table_alert)

        # table_invoice.addWidget(self.title_invoice)
        # table_mouvement.addWidget(self.title_mouvement)
        # table_mouvement.addWidget(self.table_mouvement)
        tab_widget = tabbox((table_alert, u"Alerte"))

        vbox.addWidget(self.title)
        vbox.addWidget(tab_widget)
        self.setLayout(vbox)

    def finder(self):
        self.table_invoice.refresh_(str(self.search_field.text()))


class AlertTableWidget(FTableWidget):

    def __init__(self, parent, *args, **kwargs):
        FTableWidget.__init__(self, parent=parent, *args, **kwargs)

        self.hheaders = [u"Magasin", "Produits", u"Quantité restante",
                         u"Date de la dernière operation"]

        self.stretch_columns = [0, 1, 2, 3]
        self.align_map = {0: 'l', 1: 'l', 2: 'l', 3: 'r'}
        self.display_vheaders = False
        self.live_refresh = True
        # self.sorter = True
        self.refresh_()

    def refresh_(self):
        """ """
        self._reset()
        self.set_data_for()
        self.refresh()
        pw = self.width() / 5
        self.setColumnWidth(0, pw)
        self.setColumnWidth(1, pw)
        self.setColumnWidth(2, pw)

    def set_data_for(self):
        # reports = lastes_upper_of(10)
        self.data = []
