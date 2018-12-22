#!usr/bin/env python
# -*- coding: utf8 -*-
# maintainer: Fad
from __future__ import (
    unicode_literals, absolute_import, division, print_function)

from PyQt4.QtGui import (QComboBox, QVBoxLayout, QGroupBox,
                         QFormLayout, QDialog, QTextEdit)
from models import Office

from Common.ui.util import check_is_empty, is_int
from data_helper import (
    get_offices, office_name, office_region, get_entity_name,
    office_cercle)

from Common.ui.common import (
    FWidget, LineEdit, Button_save, FormLabel, IntLineEdit, FLabel)


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
        self.region_label = FLabel()
        self.cercle_label = FLabel()
        self.phone_field = IntLineEdit()
        self.phone_field.setInputMask('## ## ## ##')
        self.bp = LineEdit()
        self.adress_org = QTextEdit()
        self.email_org = LineEdit()

        for index, value in enumerate(self.office_list):
            self.office_box.addItem("{}".format(office_name(value)), value)

        formbox = QFormLayout()
        formbox.addRow(FormLabel(u"Nom service :"), self.office_box)
        formbox.addRow(FormLabel(u"Région"), self.region_label)
        formbox.addRow(FormLabel(u"Cercle"), self.cercle_label)
        formbox.addRow(FormLabel(u"Tel :"), self.phone_field)
        formbox.addRow(FormLabel(u"B.P :"), self.bp)
        formbox.addRow(FormLabel(u"E-mail :"), self.email_org)
        formbox.addRow(FormLabel(u"Adresse complete :"), self.adress_org)
        butt = Button_save(u"Enregistrer")
        butt.clicked.connect(self.save_edit)
        formbox.addRow("", butt)

        self.organGroupBoxBtt.setLayout(formbox)

    def change_select_office(self):
        select_o = self.office_box.itemData(self.office_box.currentIndex())
        self.r_select = office_region(select_o)
        self.c_select = office_cercle(select_o)
        self.region_label.setText(get_entity_name(self.r_select))
        self.cercle_label.setText(get_entity_name(self.c_select))

    def is_valide(self):
        if check_is_empty(self.phone_field):
            return False
        return True

    def save_edit(self):
        ''' add operation '''

        if not self.is_valide():
            return

        office = Office()
        office.slug = self.office_box.itemData(self.office_box.currentIndex())
        office.slug_region = self.r_select
        office.slug_cercle = self.c_select
        office.phone = is_int(self.phone_field.text())
        office.email_org = str(self.email_org.text())
        office.bp = str(self.bp.text())
        office.adress_org = str(self.adress_org.toPlainText())
        office.save()
        self.accept()
