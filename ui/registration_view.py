#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# vim: ai ts=4 sts=4 et sw=4 nu
# maintainer: Fad
from __future__ import (
    unicode_literals, absolute_import, division, print_function)

# from datetime import datetime

from PyQt4.QtCore import QDate
from PyQt4.QtGui import (
    QVBoxLayout, QGridLayout, QFormLayout, QFrame, QComboBox, QGroupBox)

from Common.ui.common import (FWidget, FormatDate,
                              LineEdit, Button_save, FLabel, IntLineEdit)
# from Common.ui.table import FTableWidget
from Common.ui.util import (device_amount, is_int)

from models import Demande, CooperativeCompanie
from configuration import Config

from ui.registration_manager import ResgistrationManagerWidget


class RegistrationViewWidget(FWidget):

    """ Shows the home page  """

    def __init__(self, parent=0, *args, **kwargs):
        super(RegistrationViewWidget, self).__init__(
            parent=parent, *args, **kwargs)
        self.parent = parent
        self.parentWidget().set_window_title("FORMULAIRE D’IMMATRICULATION")

        self.title = FLabel("<h3>FORMULAIRE D’IMMATRICULATION</h3>")
        # editbox = QGridLayout()
        # self.parent.setVerticalScrollBar(True)
        # registration_w = QVBoxLayout()
        # self.registration_w = RegistrationWidget(parent=self)
        # registration_w.addLayout(editbox)
        # registration_w.addWidget(self.registration_w)

        self.created_year_field = IntLineEdit()
        self.duree_statutaire_field = IntLineEdit()
        self.vfq_field = LineEdit()
        self.commune_field = LineEdit()
        self.quartier_field = LineEdit()
        self.rue_field = IntLineEdit()
        self.porte_field = IntLineEdit()
        self.tel_field = IntLineEdit()
        self.bp_field = LineEdit()
        self.email_field = LineEdit()
        self.denomination_field = LineEdit()
        self.commercial_name_field = LineEdit()
        self.declaration_date_field = FormatDate(QDate.currentDate())
        self.declaration_date_field.setMaximumWidth(200)
        self.activites_box = LineEdit()
        self.total_amount = FLabel()
        self.apports_amount_field = IntLineEdit()
        self.apports_nature_field = IntLineEdit()
        self.apports_industrie_field = IntLineEdit()
        self.apports_industrie_field = IntLineEdit()

        self.activities_list = Config.CATEGORY
        self.activites_box = QComboBox()
        self.activites_box.setMaximumWidth(200)
        for index, value in enumerate(self.activities_list):
            self.activites_box.addItem(
                "{} {}".format(self.activities_list[value], value))
            # if self.organization.devise == value:
            #     self.activites_box.setCurrentIndex(index)

        # for index in range(0, len(self.liste_store)):
        #     op = self.liste_store[index]
        #     self.box_mag.addItem(op.name, op.id)

        #     if self.store and self.store.name == op.name:
        #         self.box_mag.setCurrentIndex(index)

        self.form_list = Config.CATEGORY
        self.formes_box = QComboBox()
        self.formes_box.setMaximumWidth(200)
        for index, value in enumerate(self.form_list):
            self.formes_box.addItem(
                "{} {}".format(self.form_list[value], value))
            # if self.organization.devise == value:
            #     self.formes_box.setCurrentIndex(index)
        formbox = QFormLayout()
        formbox.addRow(FLabel(
            u"Date de creation :"), self.declaration_date_field)
        formbox.addRow(FLabel(
            u"1. Dénomination Sociale de la société coopérative :"), self.denomination_field)
        formbox.addRow(
            FLabel(u"2. Nom Commercial / Sigle / Enseigne :"), self.commercial_name_field)
        formbox.addRow(FLabel(
            u"3. Année de création de la société coopérative :"), self.created_year_field)
        formbox.addRow(
            FLabel(u"4. Activités exercées :"), self.activites_box)
        formbox.addRow(
            FLabel(u"5. Forme de la société coopérative :"), self.formes_box)
        # Capital Social Initial
        self.capitalSGroupBox = QGroupBox("6. Capital Social Initial")
        capital_formbox = QFormLayout()
        capital_formbox.addRow(FLabel("Montant total :"), self.total_amount)
        capital_formbox.addRow(
            FLabel("6.1 Montant apports en numéraire :"), self.apports_amount_field)
        capital_formbox.addRow(
            FLabel("6.2 Montant apports en nature :"), self.apports_nature_field)
        capital_formbox.addRow(
            FLabel("6.3 Montant apports en industrie :"), self.apports_industrie_field)
        self.capitalSGroupBox.setLayout(capital_formbox)
        self.apports_industrie_field.textChanged.connect(self.cal_total)
        # Adresse du siège social

        self.vline = QFrame()
        self.vline.setFrameShape(QFrame.VLine)
        self.vline.setFrameShadow(QFrame.Sunken)

        self.addresGroupBox = QGroupBox("7. Adresse du siège social")
        addres_gribox = QGridLayout()
        addres_gribox.addWidget(FLabel("Village/Fraction :"), 0, 0)
        addres_gribox.addWidget(self.vfq_field, 0, 1)
        addres_gribox.addWidget(FLabel("Commune :"), 1, 0)
        addres_gribox.addWidget(self.commune_field, 1, 1)
        # addres_gribox.addWidget(self.vline, 0, 3, 2, 5)
        addres_gribox.addWidget(FLabel("Quartier :"), 2, 0)
        addres_gribox.addWidget(self.quartier_field, 2, 1)
        addres_gribox.addWidget(FLabel("Rue"), 0, 2)
        addres_gribox.addWidget(self.rue_field, 0, 3)
        addres_gribox.addWidget(FLabel("Porte (n°)"), 1, 2)
        addres_gribox.addWidget(self.porte_field, 1, 3)
        addres_gribox.addWidget(FLabel("Tel"), 2, 2)
        addres_gribox.addWidget(self.tel_field, 2, 3)
        addres_gribox.addWidget(FLabel("BP"), 0, 4)
        addres_gribox.addWidget(self.bp_field, 0, 5)
        addres_gribox.addWidget(FLabel("E-mail"), 1, 4)
        addres_gribox.addWidget(self.email_field, 1, 5)
        addres_gribox.setColumnStretch(6, 5)
        self.addresGroupBox.setLayout(addres_gribox)
        # Durée statutaire de la société coopérative
        duree_fbox = QFormLayout()
        duree_fbox.addRow(
            FLabel(u"8. Durée statutaire de la société coopérative:"), self.duree_statutaire_field)

        butt = Button_save(u"Enregistrer")
        butt.clicked.connect(self.save_and_goto_manager)
        butt_and_continous = Button_save(u"Enregistrer et continuer")
        butt_and_continous.clicked.connect(self.save_and_goto_add_member)
        duree_fbox.addRow(butt, butt_and_continous)

        vbox = QVBoxLayout()
        vbox.addLayout(formbox)
        vbox.addWidget(self.capitalSGroupBox)
        vbox.addWidget(self.addresGroupBox)
        vbox.addLayout(duree_fbox)
        self.setLayout(vbox)

    def save(self):
        self.scoop = CooperativeCompanie()
        self.scoop.denomination = str(self.denomination_field.text())
        self.scoop.commercial_name = str(self.commercial_name_field.text())
        # self.scoop.created_year = self.created_year_field.text()
        # self.scoop.vfq = str(self.vfq_field.text())
        print("DJFJ ", self.vfq_field.text())
        # self.scoop.commune = str(self.commune_field.text())
        # self.scoop.quartier = self.quartier_field.text()
        # self.scoop.rue = is_int(self.rue_field.text())
        # self.scoop.porte = is_int(self.porte_field.text())
        # self.scoop.bp = str(self.bp_field.text())
        # self.scoop.tel = is_int(self.tel_field.text())
        # self.scoop.email = str(self.email_field.text())
        # self.scoop.activite = self.activities_list[self.activites_box.currentIndex()]
        # self.scoop.forme = self.form_list[self.forme_box.currentIndex()]
        # self.scoop.apports_amount = is_int(self.apports_amount_field.text())
        # self.scoop.apports_nature = is_int(self.apports_nature_field.text())
        # self.scoop.apports_industrie = is_int(self.apports_industrie_field.text())
        self.scoop.save()
        self.dmd = Demande()
        self.dmd.declaration_date = str(self.declaration_date_field.text())
        self.dmd.scoop = self.scoop
        self.dmd.save()

    def save_and_goto_add_member(self):
        self.save()
        from ui.member_manager import MemberManagerWidget
        self.parent.change_context(MemberManagerWidget, scoop=self.scoop)

    def save_and_goto_manager(self):
        self.save()
        self.parent.change_context(ResgistrationManagerWidget)

    def cal_total(self):
        total = int(self.apports_amount_field.text()) + \
            int(self.apports_nature_field.text()) + \
            int(self.apports_industrie_field.text())
        self.total_amount.setText(device_amount(total))
