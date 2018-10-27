#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# vim: ai ts=4 sts=4 et sw=4 nu
# maintainer: Fad


# from datetime import datetime

from PyQt4.QtGui import (QVBoxLayout, QGridLayout, QIcon, QTableWidgetItem)

from configuration import Config
from Common.ui.common import (
    LineEdit, FWidget, FPeriodHolder, FPageTitle, Button)
from Common.ui.table import FTableWidget
# from Common.ui.util import (date_to_datetime, date_on_or_end)

from models import CooperativeMember


class MemberManagerWidget(FWidget, FPeriodHolder):

    def __init__(self, parent=0, scoop=None, *args, **kwargs):
        super(MemberManagerWidget, self).__init__(
            parent=parent, *args, **kwargs)
        FPeriodHolder.__init__(self, *args, **kwargs)

        self.parent = parent
        self.scoop = scoop
        self.search_field = LineEdit()
        self.search_field.setPlaceholderText("Rechercher un membre")
        # self.search_field.setMaximumWidth(400)
        self.search_field.setMaximumSize(900, 100)
        self.search_field.textChanged.connect(self.finder)

        self.string_list = []
        self.title_field = FPageTitle(
            "Gestion des membres du {}".format(self.scoop))

        self.new_demande_btt = Button("Nouveau Membre")
        self.new_demande_btt.setMaximumWidth(400)
        self.new_demande_btt.setIcon(QIcon.fromTheme('save', QIcon(
            u"{}add.png".format(Config.img_media))))
        self.new_demande_btt.clicked.connect(self.add_member)

        self.table = MemberTableWidget(parent=self)

        editbox = QGridLayout()
        editbox.addWidget(self.search_field, 1, 0)
        editbox.setColumnStretch(1, 1)
        editbox.addWidget(self.new_demande_btt, 1, 3)

        vbox = QVBoxLayout()
        vbox.addWidget(self.title_field)
        vbox.addLayout(editbox)
        vbox.addWidget(self.table)
        self.setLayout(vbox)

    def add_member(self):
        from ui.member_edit_add import EditOrAddMemberDialog
        self.open_dialog(
            EditOrAddMemberDialog, modal=True, scoop=self.scoop, table_p=self.table)

    def finder(self):
        self.search = self.search_field.lineEdit().text()
        self.table.refresh_()


class MemberTableWidget(FTableWidget):

    def __init__(self, parent, *args, **kwargs):

        FTableWidget.__init__(self, parent=parent, *args, **kwargs)
        self.parent = parent
        # self.sorter = True
        self.stretch_columns = [0, 1, 2, 3, 4]
        self.align_map = {0: 'l', 1: 'l', 2: 'r', 3: 'r', 4: 'r'}
        self.display_vheaders = False
        self.hheaders = ["Nom complet", "sexe", "Téléphone", "poste", ""]
        self.refresh_()

    def refresh_(self):
        self._reset()
        self.set_data_for()
        self.refresh()
        self.hideColumn(len(self.hheaders) - 1)

    def set_data_for(self):
        qs = CooperativeMember.select()
        # if not isinstance(self.parent.compte, str):
        #     qs = qs.where(Payment.provider_clt == self.parent.compte)
        # else:
        #     self.parent.compte = "Tous"
        # qs = qs.select().where(
        #     Payment.status == False, Payment.date <= date_on_or_end(
        #         self.end_date, on=False), Payment.date >= date_on_or_end(
        #         self.on_date)).order_by(Payment.date.asc())
        # self.data = [(pay.denomination, pay.created_date, pay.forme, pay.status, pay.id)
        #              for pay in qs]
        self.data = [(
            mmb.full_name, mmb.sex, mmb.phone, mmb.poste, mmb.id) for mmb in qs]

    def _item_for_data(self, row, column, data, context=None):
        if column == 3:
            return QTableWidgetItem(QIcon(
                u"{}edit.png".format(Config.img_cmedia)), "Edit")
        return super(MemberTableWidget, self)._item_for_data(row, column,
                                                             data, context)

    def click_item(self, row, column, *args):
        self.choix = CooperativeMember.filter(id=self.data[row][-1]).get()
        print(self.choix)
        if column != 2:
            pass
