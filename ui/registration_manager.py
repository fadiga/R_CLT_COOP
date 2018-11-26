#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# vim: ai ts=4 sts=4 et sw=4 nu
# maintainer: Fad


from PyQt4.QtGui import (QVBoxLayout, QGridLayout, QIcon, QTableWidgetItem)

from configuration import Config
from Common.ui.common import (
    LineEdit, FWidget, FPeriodHolder, FPageTitle, Button)
from Common.ui.table import FTableWidget
# from Common.ui.util import (date_to_datetime, date_on_or_end)

from models import Demande, CooperativeCompanie


class ResgistrationManagerWidget(FWidget):

    def __init__(self, parent=0, *args, **kwargs):

        super(ResgistrationManagerWidget, self).__init__(
            parent=parent, *args, **kwargs)

        self.parent = parent

        self.search_field = LineEdit()
        self.search_field.setPlaceholderText("Rechercher une demande")
        # self.search_field.setMaximumWidth(400)
        self.search_field.setMaximumSize(900, 100)
        self.search_field.textChanged.connect(self.finder)

        self.string_list = []
        self.title_field = FPageTitle("Gestion des demandes")

        self.new_demande_btt = Button("Nouvelle demande")
        self.new_demande_btt.setMaximumWidth(400)
        self.new_demande_btt.setIcon(QIcon.fromTheme('save', QIcon(
            u"{}add.png".format(Config.img_media))))
        self.new_demande_btt.clicked.connect(self.goto_demande)
        self.table = DemandeTableWidget(parent=self)

        editbox = QGridLayout()
        editbox.addWidget(self.search_field, 1, 0)
        editbox.setColumnStretch(1, 1)
        editbox.addWidget(self.new_demande_btt, 1, 3)

        vbox = QVBoxLayout()
        vbox.addWidget(self.title_field)
        vbox.addLayout(editbox)
        vbox.addWidget(self.table)
        self.setLayout(vbox)

    def goto_demande(self):
        from ui.registration_view import RegistrationViewWidget
        self.change_main_context(RegistrationViewWidget)

    def finder(self):
        self.table.refresh_()


class DemandeTableWidget(FTableWidget):

    def __init__(self, parent, *args, **kwargs):

        FTableWidget.__init__(self, parent=parent, *args, **kwargs)
        self.parent = parent
        # self.sorter = True
        self.stretch_columns = [0, 1, 2, 3, 4]
        self.align_map = {0: 'l', 1: 'l', 2: 'r', 3: 'r', 4: 'r'}
        self.display_vheaders = False
        self.hheaders = ["Denomination", "date", "Forme", "Etape suivante", ""]
        self.refresh_()

    def refresh_(self):
        self._reset()
        self.set_data_for()
        self.refresh()
        self.hideColumn(len(self.hheaders) - 1)

    def set_data_for(self):
        qs = Demande.select().filter(Demande.status != Demande.ENDPROCCES)
        if not self.parent.search_field.text() == "":
            coopc = CooperativeCompanie.select().where(
                CooperativeCompanie.denomination.contains(self.parent.search_field.text()))
            qs = qs.select().filter(Demande.scoop == coopc).order_by(
                Demande.declaration_date.asc())
        self.data = [(dmd.scoop.denomination, dmd.declaration_date,
                      dmd.scoop.display_forme(), dmd.status, dmd.scoop.id) for dmd in qs]

    def _item_for_data(self, row, column, data, context=None):
        if column == len(self.data[0]) - 2:
            return QTableWidgetItem(QIcon(
                u"{}go-next.png".format(Config.img_cmedia)),
                Demande.STATUS.get(int(self.data[row][-2])))
        return super(DemandeTableWidget, self)._item_for_data(
            row, column, data, context)

    def click_item(self, row, column, *args):
        self.choix = Demande.filter(id=self.data[row][-1]).get()
        if column == 3:
            status = int(self.choix.status)
            if status == self.choix.ADDMEMBER:
                from ui.member_manager import MemberManagerWidget
                self.parent.change_main_context(
                    MemberManagerWidget, dmd=self.choix)
            if status == self.choix.CHECKLIST:
                from ui.check_list_view import CheckListViewWidget
                self.parent.change_main_context(
                    CheckListViewWidget, dmd=self.choix)
            if status == self.choix.IMMATRICULAITON:
                from ui.immatriculation import ImmatriculationSCoopViewWidget
                self.parent.change_main_context(
                    ImmatriculationSCoopViewWidget, dmd=self.choix)
