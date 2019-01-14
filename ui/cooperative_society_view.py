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
from Common.ui.util import (uopen_file)
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
        self.search_field.setMinimumSize(600, 80)
        self.search_field.textChanged.connect(self.finder)

        self.btt_xlsx_export = BttExportXLSX("")
        self.btt_xlsx_export.clicked.connect(self.export_xlsx)
        self.btt_xlsx_export.setMaximumWidth(40)
        self.btt_xlsx_export.setEnabled(False)
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


class MemberTableWidget(FTableWidget):

    def __init__(self, parent, * args, **kwargs):

        FTableWidget.__init__(self, parent=parent, *args, **kwargs)
        self.setStyleSheet(
            "QHeaderView::section { background-color:green; color:#fff;text-transform: uppercase;font:bold}")
        self.parent = parent
        self.sorter = True
        self.stretch_columns = [0, 1, 2, 3, 4, 5]
        self.align_map = {0: 'l', 1: 'l', 2: 'r', 3: 'r', 4: 'r'}
        # self.display_vheaders = False
        self.hheaders = [
            "Immatricule", "Dénomination Sociale de la société coopérative",
            "Nom Commercial / Sigle / Enseigne",
            "Activités exercées", "Filière", "Forme de la société coopérative", "Editer", "Voir", ""]
        self.refresh_()

    def refresh_(self):
        self._reset()
        self.set_data_for()
        self.refresh()
        self.hideColumn(len(self.hheaders) - 1)

    def set_data_for(self):
        self.qs = CooperativeCompanie.select().filter(
            CooperativeCompanie.created == True)
        self.qs = self.qs.select().where(
            CooperativeCompanie.denomination.contains(
                self.parent.search_field.text())).order_by(
            CooperativeCompanie.start_date.asc())
        self.data = [(coopc.immatricule, coopc.denomination, coopc.commercial_name,
                      coopc.display_activity(), coopc.display_spinneret(),
                      coopc.display_forme(), "", coopc.id) for coopc in self.qs]

        if len(self.data) != 0:
            self.parent.btt_xlsx_export.setEnabled(True)

    def _item_for_data(self, row, column, data, context=None):
        # if column == 0:
        #     return QTableWidgetItem(QIcon(
        # u"{}find.png".format(Config.img_cmedia)),
        # "{}".format(self.data[0][0]))
        if column == len(self.data[0]) - 2:
            return QTableWidgetItem(QIcon(
                u"{}edit.png".format(Config.img_cmedia)), "")
        if column == len(self.data[0]) - 1:
            return QTableWidgetItem(QIcon(
                u"{}find.png".format(Config.img_cmedia)), "")
        return super(MemberTableWidget, self)._item_for_data(row, column,
                                                             data, context)

    def click_item(self, row, column, *args):
        self.choix = CooperativeCompanie.filter(id=self.data[row][-1]).get()
        if column == 0:
            from export_immat_pdf import pdf_maker
            pdf_file = pdf_maker(
                "Immatricule", Demande.filter(scoop=self.choix).get())
            uopen_file(pdf_file)
        if column == len(self.data[0]) - 2:
            from ui.coop_society_manager import CoopSocietyManager
            self.parent.change_main_context(
                CoopSocietyManager, scoop=self.choix)
        if column == len(self.data[0]) - 1:
            from ui.cooperative_society_show import CooperativeSocietyDialog
            self.parent.open_dialog(
                CooperativeSocietyDialog, modal=True, scoop=self.choix)

    def dict_data(self):
        data = [(
            scp.immatricule,
            scp.denomination,
            scp.commercial_name,
            scp.created_year,
            scp.display_activity(),
            scp.display_spinneret(),
            scp.display_forme(),
            int(scp.apports_numeraire) + int(scp.apports_nature) +
            int(scp.apports_industrie),
            scp.apports_numeraire,
            scp.apports_nature,
            scp.apports_industrie,
            scp.display_cercle(),
            scp.display_commune(),
            scp.display_vfq(),
            scp.rue,
            scp.porte,
            scp.tel,
            scp.bp,
            scp.email,
            scp.duree_statutaire
        ) for scp in self.qs]
        self.scp = self.qs.where(CooperativeCompanie.id == 1).get()
        title = "SCOOP de {}".format(self.scp.display_cercle())
        hheaders = [
            "Immatricule",
            "Dénomination Sociale de la société coopérative",
            "Nom Commercial / Sigle / Enseigne",
            "Année de création de la société coopérative",
            "Activités exercées",
            "Filière",
            "Forme de la société coopérative",
            "Montant total",
            "Montant apports en numéraire",
            "Montant apports en nature",
            "Montant apports en industrie",
            "Cercle",
            "Commune",
            "Village/Fraction/Quartier",
            "Rue",
            "Porte",
            "Tel",
            "BP",
            "E-mail",
            "Durée statutaire de la société coopérative",
        ]
        return {
            'file_name': title,
            'headers': hheaders,
            'data': data,
            "extend_rows": [],
            'sheet': title,
            'widths': self.stretch_columns,
            'format_money': ["H:H", "I:I", "J:J", ],
            # 'exclude_row': len(self.data) - 1,
            # 'date': self.parent.now,
            'others': [("A5", "C5", "DRDSES : {}".format(self.scp.display_region())),
                       ("A6", "B6", "SLDSES: {}".format(self.scp.display_cercle()))],
        }
