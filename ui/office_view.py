#!usr/bin/env python
# -*- coding: utf8 -*-
# maintainer: Fad
from __future__ import (
    unicode_literals, absolute_import, division, print_function)

from PyQt4.QtGui import (QComboBox, QVBoxLayout, QGroupBox,
                         QFormLayout, QDialog, QTextEdit)
from models import Office

from Common.ui.util import check_is_empty
from data_helper import (
    entity_children, get_offices, office_name, office_region, get_entity_name)

from Common.ui.common import (
    FWidget, LineEdit, Button_save, FormLabel, IntLineEdit)


class NewOrEditOfficeViewWidget(QDialog, FWidget):

    def __init__(self, pp=None, owner=None, parent=None, *args, **kwargs):
        QDialog.__init__(self, parent, *args, **kwargs)

        self.setWindowTitle(u"Nouvel Organisation")
        self.parent = parent

        vbox = QVBoxLayout()

        self.office_group_box()
        vbox.addWidget(self.organGroupBoxBtt)
        self.setLayout(vbox)

    def office_group_box(self):
        self.organGroupBoxBtt = QGroupBox(
            self.tr("Configuration des localités"))

        self.office_box = QComboBox()
        self.office_box.currentIndexChanged.connect(self.change_select_office)

        # print(get_offices())
        self.office_list = get_offices()
        self.region_box = QComboBox()
        # self.region_box.setMaximumWidth(200)
        self.cercle_box = QComboBox()
        self.region_box.currentIndexChanged.connect(self.change_select)
        self.region_list = {}

        # self.name_office = LineEdit()
        self.phone = IntLineEdit()
        self.bp = LineEdit()
        self.adress_org = QTextEdit()
        self.email_org = LineEdit()

        for index, value in enumerate(self.office_list):
            self.office_box.addItem("{}".format(office_name(value)), value)

        for index, value in enumerate(self.region_list):
            print(value)
            self.region_box.addItem(
                "{}".format(self.region_list.get(value).upper()), value)

        self.cercle_list = self.get_cercle_list()
        for index, value in enumerate(self.cercle_list):
            self.cercle_box.addItem(
                "{}".format(self.cercle_list.get(value).upper()), value)

        formbox = QFormLayout()
        formbox.addRow(FormLabel(u"Nom service :"), self.office_box)
        formbox.addRow(FormLabel(u"Région"), self.region_box)
        formbox.addRow(FormLabel(u"Cercle"), self.cercle_box)
        formbox.addRow(FormLabel(u"Tel :"), self.phone)
        formbox.addRow(FormLabel(u"B.P :"), self.bp)
        formbox.addRow(FormLabel(u"E-mail :"), self.email_org)
        formbox.addRow(FormLabel(u"Adresse complete :"), self.adress_org)
        butt = Button_save(u"Enregistrer")
        butt.clicked.connect(self.save_edit)
        formbox.addRow("", butt)

        self.organGroupBoxBtt.setLayout(formbox)

    def get_region_list(self):
        # c_dic = {}
        r_select = office_region(self.office_box.itemData(
            self.office_box.currentIndex()))
        return {r_select: get_entity_name(r_select)}

    def get_cercle_list(self):
        # c_dic = {}
        r_select = self.region_box.itemData(self.region_box.currentIndex())
        return entity_children(r_select)

    def change_select_office(self):
        self.region_box.clear()
        self.region_list = self.get_region_list()

        for index, value in enumerate(self.region_list):
            self.region_box.addItem(
                "{}".format(self.region_list.get(value).upper()), value)

    def change_select(self):
        self.cercle_box.clear()
        self.cercle_list = self.get_cercle_list()

        for index, value in enumerate(self.cercle_list):
            self.cercle_box.addItem(
                "{}".format(self.cercle_list.get(value).upper()), value)

    def save_edit(self):
        ''' add operation '''

        office = Office()
        office.slug = self.office_box.itemData(self.office_box.currentIndex())
        office.slug_region = self.region_box.itemData(
            self.region_box.currentIndex())
        office.slug_cercle = self.cercle_box.itemData(
            self.cercle_box.currentIndex())

        if check_is_empty(self.phone):
            return

        office.phone = str(self.phone.text())
        office.email_org = str(self.email_org.text())
        office.bp = str(self.bp.text())
        office.adress_org = str(self.adress_org.toPlainText())
        office.save()
        self.accept()
