#!/usr/bin/env python
# -*- coding: utf-8 -*-
# maintainer: Fad

from __future__ import (unicode_literals, absolute_import, division,
                        print_function)
import datetime

# from PyQt4.QtCore import QDate
from PyQt4.QtGui import (QVBoxLayout, QGridLayout, QLineEdit, QComboBox)

from Common.ui.util import check_is_empty
from Common.ui.common import (FHeader, FWidget, Button_save)
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
        self.quality_box = QComboBox()
        self.quality_box.setMaximumWidth(600)
        self.quality_box.currentIndexChanged.connect(self.change_select)
        self.qualities_list = get_qualities()
        for index, value in enumerate(self.qualities_list):
            self.quality_box.addItem(
                "{}".format(self.qualities_list.get(value).upper()), value)

        self.procuration_field.setMaximumWidth(600)
        self.procuration_field.setPlaceholderText(
            "Réf.de la Procuration le cas échéant")
        self.btn = Button_save("Sauvegarder")
        self.btn.setMaximumWidth(600)
        self.btn.clicked.connect(self.save)
        editbox = QGridLayout()
        editbox.addWidget(FHeader(
            '''
            Ministère de la Solidarité et de l’Action Humanitaire
                                    ******
            Direction Nationale de la Protection Sociale et de l’Economie Solidaire
                                    ******
            DRDSES de : {}
            SLDSES de : {}'''.format(self.scoop.display_region(), self.scoop.display_cercle())),
            0, 0, 1, 0)
        # editbox.setColumnStretch(1, 0)
        editbox.setRowStretch(7, 1)
        editbox.addWidget(FHeader(
            '''REPUBLIQUE DU MALI
             Un Peuple-Un But-Une Foi
                      ******'''), 0, 2)
        editbox.addWidget(FHeader(
            "<h3 style='text-align:center;'>IMMATRICULATION DE LA SOCIETE COOPERATIVE ({})</h3>"
            .format(self.dmd.scoop.denomination),
            "color:blue;font-size:30px;border: 1px solid white;background: blue;color: white;"), 1, 0, 1, 3)
        # editbox.addWidget(FHeader(
        #     u"<h2>Suivant déclaration N° : {}        <br>du {}</h2>".format(
        #         self.dmd.id, self.dmd.declaration_date)), 2, 0)
        editbox.addWidget(self.name_declarant_field, 2, 0)
        editbox.addWidget(self.quality_box, 3, 0)
        editbox.addWidget(self.procuration_field, 4, 0)
        editbox.addWidget(FHeader(
            """
            <h2><b>Suivant déclaration N° :</b> {num} </h2>  du {date}
            <div>
            <b>Commune :</b> {com} <b>Quartier / Village : </b> {vfq} <br>
            <b>Rue : </b>{rue}  <b>Porte N° : </b>{porte} <br>
            <b>Tel</b> : {tel}  <b>BP</b> : {bp}   <b>Email</b> : {email}</div>
            """.format(num=self.dmd.id, date=self.dmd.declaration_date,
                       com=self.scoop.display_commune(), vfq=self.scoop.display_vfq(),
                       rue=self.scoop.rue, porte=self.scoop.porte,
                       tel=self.scoop.tel, bp=self.scoop.bp, email=self.scoop.email),
            "background:#fff; color:gray; padding:1em"), 2, 1, 4, 2)
        # editbox.addWidget(FHeader("<h2>Immatriculation : N°</h2>"), 8, 0)
        # editbox.addWidget(FHeader(
        #     "<h2> Fait à {} le {}</h2>".format(self.dmd.scoop.cercle, today)), 9, 0)
        editbox.addWidget(self.btn, 5, 0, 1, 1)
        vbox = QVBoxLayout()
        vbox.addLayout(editbox)
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
        print(check_is_empty(self.name_declarant_field))
        if self.quality_box.itemData(self.quality_box.currentIndex()) == Immatriculation.TP:
            if check_is_empty(self.procuration_field):
                return True
        return check_is_empty(self.name_declarant_field)

    def save(self):
        if self.is_not_valide():
            return False

        imma = Immatriculation()
        imma.scoop = self.scoop
        imma.name_declarant = self.name_declarant_field.text()
        imma.quality = self.quality_box.itemData(
            self.quality_box.currentIndex())
        imma.procuration = self.procuration_field.text()
        imma.save_ident()
        self.dmd.status = self.dmd.ENDPROCCES
        self.dmd.save_()

        self.parent.change_context(ResgistrationManagerWidget)
