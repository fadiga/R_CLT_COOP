#!/usr/bin/env python
# -*- coding: utf-8 -*-
# maintainer: Fad
from __future__ import (
    unicode_literals, absolute_import, division, print_function)

# from datetime import datetime
from PyQt4.QtGui import (QVBoxLayout, QTableWidgetItem, QIcon,
                         QGroupBox, QFormLayout, QGridLayout)

from Common.tabpane import tabbox
from Common.ui.common import (
    FWidget, FLabel, LineEdit, FPageTitle, Button)
from Common.ui.table import FTableWidget

from ui.member_edit_add import EditOrAddMemberDialog
from models import CooperativeMember
from configuration import Config


class CoopSocietyManager(FWidget):

    def __init__(self, parent, scoop=None, *args, **kwargs):
        super(CoopSocietyManager, self).__init__(
            parent=parent, *args, **kwargs)
        self.title = FPageTitle(
            "Gestion de coopérative {}-<strong>{}</strong>".format(scoop, scoop.immatricule))
        vbox = QVBoxLayout()
        self.scoop = scoop
        self.dmd = self.scoop.demande()
        self.setWindowTitle(self.scoop.denomination)

        info_general = QVBoxLayout()
        self.info_general = InfoManageWidget(parent=self)
        info_general.addWidget(self.info_general)

        member_table = QVBoxLayout()
        self.member_table = MemberManagerWidget(parent=self)
        # member_table.addLayout(gridbox)
        member_table.addWidget(self.member_table)

        tab_widget = tabbox((info_general, u"Info. générale"),
                            (member_table, u"Membres"))

        vbox.addWidget(self.title)
        vbox.addWidget(tab_widget)
        self.setLayout(vbox)


class InfoManageWidget(FWidget):

    def __init__(self, parent, *args, **kwargs):
        super(FWidget, self).__init__(parent=parent, *args, **kwargs)

        self.parent = parent
        formbox = QFormLayout()
        formbox.addRow(FLabel(
            u"<strong>Date de la demande :</strong> {}".format(self.parent.dmd.declaration_date)))
        formbox.addRow(FLabel(
            u"<strong>1. Dénomination Sociale de la société coopérative :</strong> {}".format(self.parent.scoop.denomination)))
        formbox.addRow(FLabel(
            u"<strong>2. Nom Commercial / Sigle / Enseigne :</strong> {}".format(self.parent.scoop.commercial_name)))
        formbox.addRow(FLabel(
            u"<strong>3. Année de création de la société coopérative :</strong> {}".format(self.parent.scoop.created_year)))
        formbox.addRow(FLabel(
            u"<strong>4. Activités exercées :</strong> {}".format(self.parent.scoop.activity)))
        formbox.addRow(FLabel(
            u"<strong>4. Filière :</strong> {}".format(self.parent.scoop.spinneret)))
        formbox.addRow(FLabel(
            u"<strong>5. Forme de la société coopérative :</strong> {}".format(self.parent.scoop.forme)))
        # Capital Social Initial
        capital_formbox = QFormLayout()
        capital_formbox.addRow(
            FLabel("<strong> Montant total : </strong> {}".format(self.parent.scoop.apports_numeraire + self.parent.scoop.apports_nature + self.parent.scoop.apports_industrie)))
        capital_formbox.addRow(FLabel(
            "<strong> 6.1 Montant apports en numéraire : </strong> {}".format(self.parent.scoop.apports_numeraire)))
        capital_formbox.addRow(FLabel(
            "<strong> 6.2 Montant apports en nature : </strong> {}".format(self.parent.scoop.apports_nature)))
        capital_formbox.addRow(FLabel(
            "<strong> 6.3 Montant apports en industrie : </strong> {}".format(self.parent.scoop.apports_industrie)))
        self.capitalSGroupBox = QGroupBox("6. Capital Social Initial")
        self.capitalSGroupBox.setLayout(capital_formbox)
        # self.capitalSGroupBox.setMaximumWidth(1200)
        # Adresse du siège social
        addres_gribox = QGridLayout()
        addres_gribox.addWidget(
            FLabel("<strong>Région : </strong>{}".format(self.parent.scoop.display_region())), 0, 0)
        addres_gribox.addWidget(
            FLabel("<strong>Cercle : </strong>{}".format(self.parent.scoop.display_cercle())), 1, 0)
        # addres_gribox.addWidget(self.vline, 0, 3, 2, 5)
        addres_gribox.addWidget(FLabel(
            "<strong>Village/Fraction/Quartier : </strong>{}".format(self.parent.scoop.display_commune())), 1, 1)
        addres_gribox.addWidget(
            FLabel("<strong>Rue : </strong>{}".format(self.parent.scoop.rue)), 2, 0)
        addres_gribox.addWidget(
            FLabel("<strong>Porte (n°) </strong>{}".format(self.parent.scoop.porte)), 2, 1)
        addres_gribox.addWidget(
            FLabel("<strong>Tel : </strong>{}".format(self.parent.scoop.tel)), 3, 0)
        addres_gribox.addWidget(
            FLabel("<strong>BP : </strong>{}".format(self.parent.scoop.bp)), 3, 1)
        addres_gribox.addWidget(
            FLabel("<strong>E-mail : </strong>{}".format(self.parent.scoop.email)), 3, 2)

        duree_fbox = QFormLayout()
        duree_fbox.addRow(FLabel(
            u"<strong>8. Durée statutaire de la société coopérative: </strong>{}".format(self.parent.scoop.duree_statutaire)))

        self.addresGroupBox = QGroupBox("7. Adresse du siège social")
        self.addresGroupBox.setLayout(addres_gribox)
        vbox = QVBoxLayout()
        vbox.addLayout(formbox)
        vbox.addWidget(self.capitalSGroupBox)
        vbox.addWidget(self.addresGroupBox)
        vbox.addLayout(duree_fbox)
        self.setLayout(vbox)


class MemberManagerWidget(FWidget):

    def __init__(self, parent, dmd=None, *args, **kwargs):
        super(FWidget, self).__init__(parent=parent, *args, **kwargs)

        self.parent = parent
        self.dmd = parent.dmd
        self.search_field = LineEdit()
        self.search_field.setPlaceholderText("Rechercher un membre")
        # self.search_field.setMaximumWidth(400)
        self.search_field.setMaximumSize(900, 100)
        self.search_field.textChanged.connect(self.finder)

        self.string_list = []

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
        vbox.addLayout(editbox)
        vbox.addWidget(self.table)
        self.setLayout(vbox)

    def add_member(self):
        self.parent.open_dialog(
            EditOrAddMemberDialog, modal=True, scoop=self.dmd.scoop, table_p=self.table)

    def finder(self):
        self.search = self.search_field.text()
        self.table.refresh_()


class MemberTableWidget(FTableWidget):

    def __init__(self, parent, * args, **kwargs):

        FTableWidget.__init__(self, parent=parent, *args, **kwargs)
        self.setStyleSheet(
            "QHeaderView::section { background-color:green; color:#fff;text-transform: uppercase;font:bold}")
        self.parent = parent
        self.dmd = self.parent.dmd
        self.sorter = True
        self.stretch_columns = [0, 1, 2, 3, 4]
        self.align_map = {0: 'l', 1: 'l', 2: 'r', 3: 'r', 4: 'r'}
        # self.display_vheaders = False
        self.hheaders = [
            "Nom complet", "sexe", "Date naissance", "Téléphone", "poste", "", ""]
        self.refresh_()

    def refresh_(self):
        self._reset()
        self.set_data_for()
        self.refresh()
        self.hideColumn(len(self.hheaders) - 1)

    def set_data_for(self):
        qs = self.dmd.scoop.membres()
        qs = qs.select().where(
            CooperativeMember.full_name.contains(self.parent.search_field.text())).order_by(
            CooperativeMember.add_date.asc())
        self.data = [(
            mmb.full_name, mmb.display_sex(), mmb.ddn, mmb.phone,
            mmb.display_poste(), mmb.id) for mmb in qs]

    def _item_for_data(self, row, column, data, context=None):
        if column == len(self.data[0]) - 1:
            return QTableWidgetItem(QIcon(
                u"{}edit.png".format(Config.img_cmedia)), "Edit")
        return super(MemberTableWidget, self)._item_for_data(row, column,
                                                             data, context)

    def click_item(self, row, column, *args):
        self.choix = CooperativeMember.filter(id=self.data[row][-1]).get()
        if column != 2:
            self.parent.open_dialog(
                EditOrAddMemberDialog, modal=True, scoop=self.dmd.scoop,
                member=self.choix, table_p=self.parent.member_table)
