#!usr/bin/env python
# -*- coding: utf8 -*-
# maintainer: Fad
from __future__ import (
    unicode_literals, absolute_import, division, print_function)

from PyQt4.QtGui import (QComboBox, QVBoxLayout, QGroupBox,
                         QFormLayout, QDialog)
from models import Settings

from data_helper import entity_children, regions

from Common.ui.common import (FWidget, Button_save, FormLabel)


class NewOrEditSettingsViewWidget(QDialog, FWidget):

    def __init__(self, pp=None, owner=None, parent=None, *args, **kwargs):
        QDialog.__init__(self, parent, *args, **kwargs)

        self.setWindowTitle(u"Nouvel Organisation")
        self.parent = parent

        vbox = QVBoxLayout()

        self.organization_group_box()
        vbox.addWidget(self.organGroupBoxBtt)
        self.setLayout(vbox)

    def organization_group_box(self):
        self.organGroupBoxBtt = QGroupBox(
            self.tr("Configuration des localités"))

        self.cercle_box = QComboBox()
        self.cercle_box.setMaximumWidth(200)
        self.region_box = QComboBox()
        self.region_box.setMaximumWidth(200)
        self.region_box.currentIndexChanged.connect(self.change_select)
        self.region_list = regions()
        for index, value in enumerate(self.region_list):
            self.region_box.addItem(
                "{}".format(self.region_list.get(value).upper()), value)

        self.cercle_list = self.get_cercle_list()
        for index, value in enumerate(self.cercle_list):
            self.cercle_box.addItem(
                "{}".format(self.cercle_list.get(value).upper()), value)

        formbox = QFormLayout()
        formbox.addRow(FormLabel(u"Région"), self.region_box)
        formbox.addRow(FormLabel(u"Cercle"), self.cercle_box)
        butt = Button_save(u"Enregistrer")
        butt.clicked.connect(self.save_edit)
        formbox.addRow("", butt)

        self.organGroupBoxBtt.setLayout(formbox)

    def get_cercle_list(self):
        # c_dic = {}
        r_select = self.region_box.itemData(
            self.region_box.currentIndex())
        return entity_children(r_select)

    def change_select(self):
        self.cercle_box.clear()
        self.cercle_list = self.get_cercle_list()

        for index, value in enumerate(self.cercle_list):
            self.cercle_box.addItem(
                "{}".format(self.cercle_list.get(value).upper()), value)

    def save_edit(self):
        ''' add operation '''

        sett = Settings()
        sett.slug_region = self.region_box.itemData(
            self.region_box.currentIndex())
        sett.slug_cercle = self.cercle_box.itemData(
            self.cercle_box.currentIndex())
        sett.save()
        self.accept()
