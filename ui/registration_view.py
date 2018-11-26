#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# vim: ai ts=4 sts=4 et sw=4 nu
# maintainer: Fad
from __future__ import (
    unicode_literals, absolute_import, division, print_function)

from PyQt4.QtCore import QDate
from PyQt4.QtGui import (
    QVBoxLayout, QGridLayout, QFormLayout, QFrame, QComboBox, QGroupBox)
from Common.ui.common import (ExtendedComboBox, FWidget, FormatDate, LineEdit,
                              Button_save, FLabel, FRLabel, IntLineEdit)
from Common.ui.util import device_amount, check_is_empty, is_int
from models import (Demande, CooperativeCompanie, Settings,
                    CheckList)
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
        self.sttg = Settings.select().where(Settings.id == 1).get()
        self.created_year_field = IntLineEdit()
        self.duree_statutaire_field = IntLineEdit()
        self.rue_field = IntLineEdit()
        self.porte_field = IntLineEdit()
        self.tel_field = IntLineEdit()
        self.bp_field = IntLineEdit()
        self.email_field = LineEdit()
        self.denomination_field = LineEdit()
        self.commercial_name_field = LineEdit()
        self.declaration_date_field = FormatDate(QDate.currentDate())
        self.declaration_date_field.setMaximumWidth(200)
        self.total_amount = FLabel()
        self.apports_numeraire_field = IntLineEdit()
        self.apports_numeraire_field.textChanged.connect(self.cal_total)
        self.apports_nature_field = IntLineEdit()
        self.apports_nature_field.textChanged.connect(self.cal_total)
        self.apports_industrie_field = IntLineEdit()
        self.apports_industrie_field.textChanged.connect(self.cal_total)

        self.spinneret_box = QComboBox()
        # self.spinneret_box.setMaximumWidth(280)

        self.activites_box = QComboBox()
        # self.activites_box.setMaximumWidth(280)
        self.activites_box.currentIndexChanged.connect(self.sp_change_select)
        self.activities_list = get_activities()
        for index, value in enumerate(self.activities_list):
            self.activites_box.addItem(
                "{}".format(self.activities_list.get(value).upper()), value)
            # if self.store and self.store.name == op.name:
            #     self.box_store.setCurrentIndex(index)

        self.formes_box = QComboBox()
        self.formes_box.setMaximumWidth(200)
        self.formes_list = get_formes()
        for index, value in enumerate(self.formes_list):
            self.formes_box.addItem(
                "{}".format(self.formes_list.get(value).upper()), value)
        stt = Settings.select().where(Settings.id == 1).get()

        self.commune_list = entity_children(stt.slug_cercle).items()
        self.commune_box = ExtendedComboBox()
        for index, value in enumerate(self.commune_list):
            self.commune_box.addItem(
                "{}".format(value[1].upper()), value[0])
        # self.commune_box.addItems(self.commune_list)
        self.commune_box.setToolTip("commune")
        self.commune_box.currentIndexChanged.connect(self.c_change_select)

        self.vfq_list = self.get_vfq_list()
        self.vfq_box = ExtendedComboBox()
        self.vfq_list = self.get_vfq_list()
        for index, value in enumerate(self.vfq_list):
            self.vfq_box.addItem(
                "{}".format(self.vfq_list.get(value).upper()), value)
        self.vfq_box.setToolTip("vfq")

        formbox = QFormLayout()
        formbox.addRow(FLabel(
            u"Date de la demande :"), self.declaration_date_field)
        formbox.addRow(FLabel(
            u"1. Dénomination Sociale de la société coopérative :"), self.denomination_field)
        formbox.addRow(FLabel(
            u"2. Nom Commercial / Sigle / Enseigne :"), self.commercial_name_field)
        formbox.addRow(FLabel(
            u"3. Année de création de la société coopérative :"), self.created_year_field)
        formbox.addRow(FLabel(
            u"4. Activités exercées :"), self.activites_box)
        formbox.addRow(FLabel(
            u"4. Filière :"), self.spinneret_box)
        formbox.addRow(FLabel(
            u"5. Forme de la société coopérative :"), self.formes_box)
        # Capital Social Initial
        capital_formbox = QFormLayout()
        capital_formbox.addRow(FLabel("Montant total :"), self.total_amount)
        capital_formbox.addRow(FLabel(
            "6.1 Montant apports en numéraire :"), self.apports_numeraire_field)
        capital_formbox.addRow(FLabel(
            "6.2 Montant apports en nature :"), self.apports_nature_field)
        capital_formbox.addRow(FLabel(
            "6.3 Montant apports en industrie :"), self.apports_industrie_field)
        self.capitalSGroupBox = QGroupBox("6. Capital Social Initial")
        self.capitalSGroupBox.setLayout(capital_formbox)
        self.capitalSGroupBox.setMaximumWidth(1200)
        # Adresse du siège social

        self.vline = QFrame()
        self.vline.setFrameShape(QFrame.VLine)
        self.vline.setFrameShadow(QFrame.Sunken)

        self.addresGroupBox = QGroupBox("7. Adresse du siège social")
        addres_gribox = QGridLayout()
        addres_gribox.addWidget(FRLabel("Cercle :"), 0, 0)
        addres_gribox.addWidget(FLabel(stt.cercle_name()), 0, 1)
        addres_gribox.addWidget(FRLabel("Commune :"), 1, 0)
        addres_gribox.addWidget(self.commune_box, 1, 1)
        # addres_gribox.addWidget(self.vline, 0, 3, 2, 5)
        addres_gribox.addWidget(FRLabel("Village/Fraction/Quartier :"), 2, 0)
        addres_gribox.addWidget(self.vfq_box, 2, 1)
        addres_gribox.addWidget(FRLabel("Rue"), 0, 2)
        addres_gribox.addWidget(self.rue_field, 0, 3)
        addres_gribox.addWidget(FRLabel("Porte (n°)"), 1, 2)
        addres_gribox.addWidget(self.porte_field, 1, 3)
        addres_gribox.addWidget(FRLabel("Tel"), 2, 2)
        addres_gribox.addWidget(self.tel_field, 2, 3)
        addres_gribox.addWidget(FRLabel("BP"), 0, 4)
        addres_gribox.addWidget(self.bp_field, 0, 5)
        addres_gribox.addWidget(FRLabel("E-mail"), 1, 4)
        addres_gribox.addWidget(self.email_field, 1, 5)
        # addres_gribox.setColumnStretch(6, 5)
        self.addresGroupBox.setLayout(addres_gribox)
        self.addresGroupBox.setMaximumWidth(1200)
        # Durée statutaire de la société coopérative
        duree_fbox = QFormLayout()
        duree_fbox.addRow(FLabel(
            u"8. Durée statutaire de la société coopérative:"), self.duree_statutaire_field)
        butt = Button_save(u"Enregistrer")
        butt.clicked.connect(self.save_and_goto_manager)
        butt_and_continous = Button_save(u"Enregistrer et continuer")
        butt_and_continous.clicked.connect(self.save_and_goto_add_member)

        butt_and_continous.setMaximumWidth(300)
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
            self.vfq_box.addItem(
                "{}".format(self.vfq_list.get(value).upper()), value)

    def get_spinneret_list(self):
        # c_dic = {}
        r_select = self.activites_box.itemData(
            self.activites_box.currentIndex())
        return get_spinneret_activites(r_select)

    def sp_change_select(self):
        self.spinneret_box.clear()
        self.spinneret_list = self.get_spinneret_list()

        for index, value in enumerate(self.spinneret_list):
            self.spinneret_box.addItem(
                "{}".format(self.spinneret_list.get(value).upper()), value)

    def is_valide(self):
        if check_is_empty(self.denomination_field):
            return False
        if check_is_empty(self.commercial_name_field):
            return False
        if check_is_empty(self.created_year_field):
            return False
        if check_is_empty(self.denomination_field):
            return False
        if check_is_empty(self.commercial_name_field):
            return False
        if check_is_empty(self.apports_numeraire_field):
            return False
        if check_is_empty(self.apports_nature_field):
            return False
        if check_is_empty(self.apports_industrie_field):
            return False
        if check_is_empty(self.rue_field):
            return False
        if check_is_empty(self.porte_field):
            return False
        if check_is_empty(self.tel_field):
            return False
        if check_is_empty(self.bp_field):
            return False
        if check_is_empty(self.email_field):
            return False
        if check_is_empty(self.duree_statutaire_field):
            return False
        return True

    def save(self):
        if not self.is_valide():
            return
        self.scoop = CooperativeCompanie()
        self.scoop.created_year = is_int(self.created_year_field.text())
        self.scoop.denomination = self.denomination_field.text()
        self.scoop.commercial_name = self.commercial_name_field.text()
        self.scoop.activity = self.activites_box.itemData(
            self.activites_box.currentIndex())
        self.scoop.spinneret = self.spinneret_box.itemData(
            self.spinneret_box.currentIndex())
        self.scoop.forme = self.formes_box.itemData(
            self.formes_box.currentIndex())
        self.scoop.apports_numeraire = is_int(
            self.apports_numeraire_field.text())
        self.scoop.apports_nature = is_int(self.apports_nature_field.text())
        self.scoop.apports_industrie = is_int(
            self.apports_industrie_field.text())
        self.scoop.region = self.sttg.slug_region
        self.scoop.cercle = self.sttg.slug_cercle
        self.scoop.commune = self.commune_box.itemData(
            self.commune_box.currentIndex())
        self.scoop.vfq = self.vfq_box.itemData(self.vfq_box.currentIndex())
        self.scoop.rue = is_int(self.rue_field.text())
        self.scoop.porte = is_int(self.porte_field.text())
        self.scoop.tel = is_int(self.tel_field.text())
        self.scoop.bp = is_int(self.bp_field.text())
        self.scoop.email = self.email_field.text()
        self.scoop.duree_statutaire = is_int(
            self.duree_statutaire_field.text())
        self.scoop.save()
        check_list = CheckList()
        check_list.save()
        self.dmd = Demande()
        self.dmd.check_list = check_list
        self.dmd.declaration_date = str(self.declaration_date_field.text())
        self.dmd.scoop = self.scoop
        self.dmd.status = self.dmd.ADDMEMBER
        self.dmd.save()
        return True

    def save_and_goto_add_member(self):
        if self.save():
            from ui.member_manager import MemberManagerWidget
            self.parent.change_context(MemberManagerWidget, dmd=self.dmd)

    def save_and_goto_manager(self):
        if self.save():
            self.parent.change_context(ResgistrationManagerWidget)

    def cal_total(self):
        total = int(self.apports_numeraire_field.text() or 0) + int(
            self.apports_nature_field.text() or 0) + int(
            self.apports_industrie_field.text() or 0)
        self.total_amount.setText(device_amount(total))
