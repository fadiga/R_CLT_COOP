#!/usr/bin/env python
# -*- coding: utf-8 -*-
# maintainer: Fad

from __future__ import (unicode_literals, absolute_import, division,
                        print_function)
import datetime

# from PyQt4.QtCore import QDate
from PyQt4.QtGui import (QVBoxLayout, QLineEdit, QComboBox,
                         QFormLayout, QGroupBox)

from constants import *
from Common.ui.util import check_is_empty
from Common.ui.common import (FWidget, Button_save, IntLineEdit, FLabel)
from models import Immatriculation
from data_helper import get_qualities
from ui.registration_manager import ResgistrationManagerWidget

today = datetime.date.today()


class ImmatriculationSCoopViewWidget(FWidget):

    def __init__(self, parent, dmd=None, *args, **kwargs):
        super(ImmatriculationSCoopViewWidget, self).__init__(
            parent=parent, *args, **kwargs)

        self.parent = parent
        self.parentWidget().set_window_title("FORMULAIRE D’IMMATRICULATION")
        self.dmd = dmd
        self.scoop = self.dmd.scoop
        self.name_declarant_field = QLineEdit()
        self.name_declarant_field.setPlaceholderText("M. / Mme")
        self.name_declarant_field.setMaximumWidth(600)

        self.procuration_field = QLineEdit()
        self.procuration_field.setPlaceholderText(
            "Réf.de la Procuration le cas échéant")
        self.procuration_field.setMaximumWidth(600)
        self.quality_box = QComboBox()
        self.quality_box.setMaximumWidth(600)
        self.quality_box.currentIndexChanged.connect(self.change_select)
        self.qualities_list = get_qualities()
        for index, value in enumerate(self.qualities_list):
            self.quality_box.addItem(
                "{}".format(self.qualities_list.get(value).upper()), value)

        self.type_box = QComboBox()
        self.type_box.setMaximumWidth(600)
        self.type_lists = Immatriculation.TYPES
        for index, value in enumerate(self.type_lists):
            print(value)
            self.type_box.addItem("{}".format(value[1], index))
        self.tel_declarant_field = IntLineEdit()
        self.tel_declarant_field.setInputMask('## ## ## ##')
        self.tel_declarant_field.setMaximumWidth(600)
        self.btn = Button_save("Sauvegarder")
        self.btn.setMaximumWidth(600)
        self.btn.clicked.connect(self.save)

        declarant_formbox = QFormLayout()
        declarant_formbox.addRow(FLabel("<strong>Type de d'immatriculation *: </strong>"), self.type_box)
        declarant_formbox.addRow(FLabel("<strong>Nom et prénom du declarant *: </strong>"), self.name_declarant_field)
        declarant_formbox.addRow(FLabel("<strong>En qualité de *: </strong>"), self.quality_box)
        declarant_formbox.addRow(FLabel("<strong>Procuration *: </strong>"), self.procuration_field)
        declarant_formbox.addRow(FLabel("<strong>Numéro tel. du declarant *: </strong>"), self.tel_declarant_field)
        declarant_formbox.addRow(FLabel(""), self.btn)
        self.declarantGroupBox = QGroupBox("Info. du déclarant de la {} *".format(self.scoop.denomination))
        self.declarantGroupBox.setStyleSheet(CSS_CENTER)
        self.declarantGroupBox.setLayout(declarant_formbox)
        vbox = QVBoxLayout()
        # vbox.addWidget(self.infoGroupBox)
        vbox.addWidget(self.declarantGroupBox)
        # vbox.addLayout(editbox)
        self.setLayout(vbox)

    def change_select(self):
        self.qlt_select = self.quality_box.itemData(
            self.quality_box.currentIndex())

        self.procuration_field.setEnabled(False)
        if self.qlt_select == Immatriculation.TP:
            self.procuration_field.setEnabled(True)
            # if check_is_empty(self.procuration_field):
            #     return False

    def is_not_valide(self):
        # print(check_is_empty(self.name_declarant_field))
        if self.quality_box.itemData(self.quality_box.currentIndex()) == Immatriculation.TP:
            if check_is_empty(self.procuration_field) or check_is_empty(self.tel_declarant_field):
                return True
        return check_is_empty(self.name_declarant_field) or check_is_empty(self.tel_declarant_field)

    def save(self):
        if self.is_not_valide():
            return False

        imma = Immatriculation()
        imma.scoop = self.scoop
        imma.typ_imm = self.type_lists[self.type_box.currentIndex()][0]
        imma.name_declarant = self.name_declarant_field.text()
        imma.quality = self.quality_box.itemData(self.quality_box.currentIndex())
        imma.procuration = self.procuration_field.text()
        imma.tel_declarant = self.tel_declarant_field.text()
        imma.save_ident()
        self.dmd.status = self.dmd.ENDPROCCES
        self.dmd.save_()
        self.parent.change_context(ResgistrationManagerWidget)
