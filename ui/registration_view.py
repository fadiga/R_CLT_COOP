#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# vim: ai ts=4 sts=4 et sw=4 nu
# maintainer: Fad
from __future__ import (
    unicode_literals, absolute_import, division, print_function)

from PyQt4.QtCore import QDate
from PyQt4.QtGui import (
    QVBoxLayout, QGridLayout, QFormLayout, QFrame, QComboBox, QGroupBox)

from constants import *

from Common.ui.common import (ExtendedComboBox, FWidget, FormatDate, LineEdit,
                              Button_save, FLabel, FRLabel, IntLineEdit)
from Common.ui.util import device_amount, check_is_empty, is_int, field_error
from models import (Demande, CooperativeCompanie, Office, CheckList)
from data_helper import (entity_children, get_formes, get_spinneret_activites,
                         get_activities)
from ui.registration_manager import ResgistrationManagerWidget


class RegistrationViewWidget(FWidget):

    """ Shows the home page  """

    def __init__(self, parent=0, *args, **kwargs):
        super(RegistrationViewWidget, self).__init__(
            parent=parent, *args, **kwargs)
        self.parent = parent

        self.parentWidget().set_window_title("FORMULAIRE D’IMMATRICULATION")
        self.title = FLabel("<h3>FORMULAIRE D’IMMATRICULATION</h3>")
        self.office = Office.select().where(Office.id == 1).get()
        self.created_date_field = FormatDate(QDate.currentDate())
        self.created_date_field.setMaximumWidth(130)
        # self.created_date_field.setInputMask('##/##/####')
        self.rue_field = IntLineEdit()
        self.porte_field = IntLineEdit()
        self.tel_field = IntLineEdit()
        self.tel_field.setInputMask('## ## ## ##')
        self.tel2_field = IntLineEdit()
        self.tel2_field.setInputMask('## ## ## ##')
        self.bp_field = IntLineEdit()
        self.email_field = LineEdit()
        self.denomination_field = LineEdit()
        self.commercial_name_field = LineEdit()
        self.declaration_date_field = FormatDate(QDate.currentDate())
        self.declaration_date_field.setMaximumWidth(130)
        self.amount_capital_social_initial = FLabel()
        self.amount_part_social_field = IntLineEdit()
        self.apports_numeraire_field = IntLineEdit()
        self.apports_numeraire_field.textChanged.connect(self.cal_total)
        self.apports_nature_field = IntLineEdit()
        self.apports_nature_field.textChanged.connect(self.cal_total)
        self.apports_industrie_field = IntLineEdit()
        self.apports_industrie_field.textChanged.connect(self.cal_total)

        self.duree_statutaire_field = IntLineEdit()
        self.duree_statutaire_field.setMaximumWidth(80)
        self.spinneret_box = QComboBox()
        self.spinneret_box.setMaximumWidth(800)

        self.activites_box = QComboBox()
        self.activites_box.setMaximumWidth(800)
        self.activites_box.currentIndexChanged.connect(self.sp_change_select)
        self.activities_list = get_activities()
        for index, value in enumerate(self.activities_list):
            self.activites_box.addItem(
                "{}".format(self.activities_list.get(value).upper()), value)
            # if self.store and self.store.name == op.name:
            #     self.box_store.setCurrentIndex(index)

        self.formes_box = QComboBox()
        self.formes_box.setMaximumWidth(800)
        self.formes_list = get_formes()
        for index, value in enumerate(self.formes_list):
            self.formes_box.addItem(
                "{}".format(self.formes_list.get(value).upper()), value)

        self.commune_list = entity_children(self.office.slug_cercle).items()
        self.commune_box = ExtendedComboBox()
        for index, value in enumerate(self.commune_list):
            self.commune_box.addItem(
                "{}".format(value[1].upper()), value[0])
        # self.commune_box.addItems(self.commune_list)
        self.commune_box.setToolTip("commune")
        self.commune_box.currentIndexChanged.connect(self.c_change_select)

        # self.vfq_list = self.get_vfq_list()
        self.vfq_box = ExtendedComboBox()
        self.vfq_list = self.get_vfq_list()
        for index, value in enumerate(self.vfq_list):
            self.vfq_box.addItem(
                "{}".format(self.vfq_list.get(value).upper()), value)
        self.vfq_box.setToolTip("vfq")

        formbox = QFormLayout()
        formbox.addRow(FLabel(DATE_DEMANTE), self.declaration_date_field)
        formbox.addRow(FLabel("1. " + DENOMINATION_S_SC), self.denomination_field)
        formbox.addRow(FLabel("2. " + NOM_COMMERCIAL), self.commercial_name_field)
        formbox.addRow(FLabel("3. " + DATE_CREATION_SC), self.created_date_field)
        formbox.addRow(FLabel("4. " + ACTIVITES_E), self.activites_box)
        formbox.addRow(FLabel("5. " + FILIERE), self.spinneret_box)
        formbox.addRow(FLabel("6. " + FORME_SC), self.formes_box)
        # Capital Social Initial
        capital_formbox = QFormLayout()
        capital_formbox.addRow(FLabel("7.1. " + MONTANT_PART_S), self.amount_part_social_field)
        capital_formbox.addRow(FLabel("7.2. " + MONTANT_APPORTS_NUM), self.apports_numeraire_field)
        capital_formbox.addRow(FLabel("7.3. " + MONTANT_APPORTS_NAT), self.apports_nature_field)
        capital_formbox.addRow(FLabel("7.4. " + MONTANT_APPORTS_INDU), self.apports_industrie_field)
        self.capitalSGroupBox = QGroupBox("7. " + MONTANT_CAPITAL_SI)
        self.capitalSGroupBox.setLayout(capital_formbox)
        self.capitalSGroupBox.setStyleSheet(CSS)
        # self.capitalSGroupBox.setMaximumWidth(1300)
        # Adresse du siège social

        self.vline = QFrame()
        self.vline.setFrameShape(QFrame.VLine)
        self.vline.setFrameShadow(QFrame.Sunken)

        self.addresGroupBox = QGroupBox("8. " + ADRESSE_SS)
        self.addresGroupBox.setStyleSheet(CSS)
        addres_gribox = QGridLayout()
        addres_gribox.addWidget(FRLabel(CERCLE), 0, 0)
        addres_gribox.addWidget(FLabel(self.office.cercle_name()), 0, 1)
        addres_gribox.addWidget(FRLabel(COMMUNE), 1, 0)
        addres_gribox.addWidget(self.commune_box, 1, 1)
        # addres_gribox.addWidget(self.vline, 0, 3, 2, 5)
        addres_gribox.addWidget(FRLabel(VFQ), 2, 0)
        addres_gribox.addWidget(self.vfq_box, 2, 1)
        addres_gribox.addWidget(FRLabel(RUE), 0, 2)
        addres_gribox.addWidget(self.rue_field, 0, 3)
        addres_gribox.addWidget(FRLabel(PORTE), 1, 2)
        addres_gribox.addWidget(self.porte_field, 1, 3)
        addres_gribox.addWidget(FRLabel(BP), 0, 4)
        addres_gribox.addWidget(self.bp_field, 0, 5)
        addres_gribox.addWidget(FRLabel(EMAIL), 1, 4)
        addres_gribox.addWidget(self.email_field, 1, 5)
        addres_gribox.addWidget(FRLabel(TEL), 2, 2)
        addres_gribox.addWidget(self.tel_field, 2, 3)
        addres_gribox.addWidget(FRLabel(TEL2), 2, 4)
        addres_gribox.addWidget(self.tel2_field, 2, 5)
        # addres_gribox.setColumnStretch(6, 5)
        self.addresGroupBox.setLayout(addres_gribox)
        # self.addresGroupBox.setMaximumWidth(1300)
        # Durée statutaire de la société coopérative
        duree_fbox = QFormLayout()
        duree_fbox.addRow(FLabel("9. " + DUREE_STATUTAIRE_SC), self.duree_statutaire_field)
        butt = Button_save(SAVE)
        butt.clicked.connect(self.save_and_goto_manager)
        butt_and_continous = Button_save(SAVE_AND_CONTINNUES)
        butt_and_continous.clicked.connect(self.save_and_goto_add_member)

        butt_and_continous.setMaximumWidth(300)
        duree_fbox.addRow(FLabel(""), FLabel(""))
        duree_fbox.addRow(butt, butt_and_continous)

        vbox = QVBoxLayout()
        vbox.addLayout(formbox)
        vbox.addWidget(self.capitalSGroupBox)
        vbox.addWidget(self.addresGroupBox)
        vbox.addLayout(duree_fbox)
        self.setLayout(vbox)

    def get_vfq_list(self):
        # c_dic = {}
        co_select = self.commune_box.itemData(
            self.commune_box.currentIndex())
        return entity_children(co_select)

    def c_change_select(self):
        self.vfq_box.clear()
        self.vfq_list = self.get_vfq_list()
        for index, value in enumerate(self.vfq_list):
            self.vfq_box.addItem("{}".format(self.vfq_list.get(
                value).upper()), value)

    def get_spinneret_list(self):
        # c_dic = {}
        r_select = self.activites_box.itemData(
            self.activites_box.currentIndex())
        return get_spinneret_activites(r_select)

    def sp_change_select(self):
        self.spinneret_box.clear()
        self.spinneret_list = self.get_spinneret_list()

        for index, value in enumerate(self.spinneret_list):
            self.spinneret_box.addItem("{}".format(
                self.spinneret_list.get(value).upper()), value)

    def is_valide(self):
        if check_is_empty(self.denomination_field):
            return False

        if CooperativeCompanie.select().where(CooperativeCompanie.denomination==self.denomination_field.text()).exists():
            field_error(self.denomination_field, "Cette dénomination existe déjà dans la base de données !")
            return False
        if check_is_empty(self.commercial_name_field):
            return False
        if check_is_empty(self.created_date_field):
            return False
        if check_is_empty(self.denomination_field):
            return False
        if check_is_empty(self.apports_numeraire_field):
            return False
        if check_is_empty(self.apports_nature_field):
            return False
        if check_is_empty(self.apports_industrie_field):
            return False
        # if check_is_empty(self.rue_field):
        #     return False
        # if check_is_empty(self.porte_field):
        #     return False
        # print(len(self.tel_field.text()))
        if len(self.tel_field.text()) != 11:
            field_error(self.tel_field, "Numéro requis")
            return False
        # if check_is_empty(self.bp_field):
        #     return False
        # if check_is_empty(self.email_field):
        #     return False
        if check_is_empty(self.duree_statutaire_field):
            return False
        # print(int(self.duree_statutaire_field.text()))
        if int(self.duree_statutaire_field.text()) > 99:
            field_error(self.duree_statutaire_field, "La durée statutaire ne peut être supérieure à 99 ans")
            return False
        return True

    def save(self):
        if not self.is_valide():
            return
        self.scoop = CooperativeCompanie()
        self.scoop.office = self.office
        self.scoop.created_date = str(self.created_date_field.text())
        self.scoop.denomination = str(self.denomination_field.text())
        self.scoop.commercial_name = str(self.commercial_name_field.text())
        self.scoop.activity = self.activites_box.itemData(
            self.activites_box.currentIndex())
        self.scoop.spinneret = self.spinneret_box.itemData(
            self.spinneret_box.currentIndex())
        self.scoop.forme = self.formes_box.itemData(
            self.formes_box.currentIndex())
        self.scoop.amount_part_social = is_int(
            self.amount_part_social_field.text())
        self.scoop.apports_numeraire = is_int(
            self.apports_numeraire_field.text())
        self.scoop.apports_nature = is_int(self.apports_nature_field.text())
        self.scoop.apports_industrie = is_int(
            self.apports_industrie_field.text())
        self.scoop.region = self.office.slug_region
        self.scoop.cercle = self.office.slug_cercle
        self.scoop.commune = self.commune_box.itemData(
            self.commune_box.currentIndex())
        self.scoop.vfq = self.vfq_box.itemData(self.vfq_box.currentIndex())
        self.scoop.rue = is_int(self.rue_field.text())
        self.scoop.porte = is_int(self.porte_field.text())
        self.scoop.tel = is_int(self.tel_field.text())
        self.scoop.tel2 = is_int(self.tel2_field.text())
        self.scoop.bp = is_int(self.bp_field.text())
        self.scoop.email = self.email_field.text()
        self.scoop.duree_statutaire = is_int(
            self.duree_statutaire_field.text())
        self.scoop.save_()
        check_list = CheckList()
        check_list.save_()
        self.dmd = Demande()
        self.dmd.check_list = check_list
        self.dmd.declaration_date = str(self.declaration_date_field.text())
        self.dmd.scoop = self.scoop
        self.dmd.status = self.dmd.ADDMEMBER
        self.dmd.save_()
        return True

    def save_and_goto_add_member(self):
        if self.save():
            from ui.member_manager import MemberManagerWidget
            self.parent.change_context(MemberManagerWidget, dmd=self.dmd)

    def save_and_goto_manager(self):
        if self.save():
            self.parent.change_context(ResgistrationManagerWidget)

    def cal_total(self):
        total = is_int(
            self.apports_numeraire_field.text() or 0) + is_int(
            self.apports_nature_field.text() or 0) + is_int(
            self.apports_industrie_field.text() or 0)
        self.capitalSGroupBox.setTitle("7. {} :  {}".format(MONTANT_CAPITAL_SI, device_amount(total)))
