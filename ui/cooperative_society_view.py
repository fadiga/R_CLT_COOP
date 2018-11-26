#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# vim: ai ts=4 sts=4 et sw=4 nu
# maintainer: Fad
from __future__ import (
    unicode_literals, absolute_import, division, print_function)

# from datetime import datetime
from PyQt4.QtGui import (QVBoxLayout, QIcon, QTableWidgetItem, QGridLayout)

# from Common.tabpane import tabbox
from Common.ui.common import FWidget, FPageTitle, BttExportXLSX, LineEdit
from Common.ui.table import FTableWidget
from tools.export_immat_pdf import pdFview
from Common.ui.util import (uopen_file)
from ui.cooperative_socuety_show import CooperativeSocietyDialog
from models import CooperativeCompanie, Demande
from configuration import Config


class CooperativeSocietyViewWidget(FWidget):

    """ Shows the home page  """

    def __init__(self, parent=0, *args, **kwargs):
        super(CooperativeSocietyViewWidget, self).__init__(
            parent=parent, *args, **kwargs)

        self.parentWidget().set_window_title("SCOOP")

        self.parent = parent
        self.search_field = LineEdit()
        self.search_field.setPlaceholderText("Rechercher une coopérative")
        self.search_field.setMaximumSize(900, 80)
        self.search_field.textChanged.connect(self.finder)

        self.btt_xlsx_export = BttExportXLSX("")
        self.btt_xlsx_export.clicked.connect(self.export_xlsx)
        self.btt_xlsx_export.setMaximumWidth(40)
        self.string_list = []
        self.title_field = FPageTitle("Gestion des Sociétés coopératives")

        self.table = MemberTableWidget(parent=self)

        editbox = QGridLayout()
        editbox.addWidget(self.search_field, 1, 0)
        editbox.setColumnStretch(1, 1)
        editbox.addWidget(self.btt_xlsx_export, 1, 2)

        vbox = QVBoxLayout()
        vbox.addWidget(self.title_field)
        vbox.addLayout(editbox)
        vbox.addWidget(self.table)
        self.setLayout(vbox)

    def export_xlsx(self):
        from Common.exports_xlsx import export_dynamic_data
        export_dynamic_data(self.table.dict_data())

    def finder(self):
        self.search = self.search_field.text()
        self.table.refresh_()

    def printer_pdf(self):
        pdFreport = pdFview("Immatricule", self.dmd)
        uopen_file(pdFreport)


class MemberTableWidget(FTableWidget):

    def __init__(self, parent, * args, **kwargs):

        FTableWidget.__init__(self, parent=parent, *args, **kwargs)
        self.parent = parent
        # self.sorter = True
        self.stretch_columns = [0, 1, 2, 3, 4]
        self.align_map = {0: 'l', 1: 'l', 2: 'r', 3: 'r', 4: 'r'}
        self.display_vheaders = False
        self.hheaders = [
            "Immatricule", "Dénomination Sociale de la société coopérative",
            "Nom Commercial / Sigle / Enseigne",
            "Activités exercées", "Filière", "Forme de la société coopérative", "", ""]
        self.refresh_()

    def refresh_(self):
        self._reset()
        self.set_data_for()
        self.refresh()
        self.hideColumn(len(self.hheaders) - 1)

    def set_data_for(self):
        qs = CooperativeCompanie.select().filter(CooperativeCompanie.created == True)
        qs = qs.select().where(
            CooperativeCompanie.denomination.contains(self.parent.search_field.text())).order_by(
            CooperativeCompanie.start_date.asc())
        self.data = [(coopc.immatricule, coopc.denomination, coopc.commercial_name,
                      coopc.display_activity(), coopc.display_spinneret(),
                      coopc.forme, coopc.id) for coopc in qs]

    def _item_for_data(self, row, column, data, context=None):
        if column == 0:
            return QTableWidgetItem(QIcon(
                u"{}find.png".format(Config.img_cmedia)), "{}".format(self.data[0][0]))
        if column == len(self.data[0]) - 1:
            return QTableWidgetItem(QIcon(
                u"{}find.png".format(Config.img_cmedia)), "Voir")
        return super(MemberTableWidget, self)._item_for_data(row, column,
                                                             data, context)

    def click_item(self, row, column, *args):
        self.choix = CooperativeCompanie.filter(id=self.data[row][-1]).get()
        if column == 0:
            pdFreport = pdFview(
                "Immatricule", Demande.filter(scoop=self.choix).get())
            uopen_file(pdFreport)
        if column == len(self.data[0]) - 1:
            self.parent.open_dialog(
                CooperativeSocietyDialog, modal=True, scoop=self.choix)

    def dict_data(self):
        title = "Movements"
        return {
            'file_name': title,
            'headers': self.hheaders[:-1],
            'data': self.data,
            "extend_rows": [],
            'sheet': title,
            # 'title': self.title,
            'widths': self.stretch_columns,
            'format_money': ["C:C", "D:D", "E:E", ],
            # 'exclude_row': len(self.data) - 1,
            # 'date': self.parent.now,
            # 'others': [("A7", "C7", "Compte : {}".format(self.provider_clt)),
            #            ("A8", "B8", "Solde au {}: {}".format(
            # self.parent.now, device_amount(self.balance_tt,
            # self.provider_clt.id))), ],
        }
