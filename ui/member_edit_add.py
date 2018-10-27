#!/usr/bin/env python
# -*- coding: utf-8 -*-
# maintainer: Fad

from PyQt4.QtCore import QDate
from PyQt4.QtGui import (QVBoxLayout, QDialog,
                         QTextEdit, QFormLayout, QComboBox)

from Common.ui.util import check_is_empty, field_error
from Common.ui.common import (
    FWidget, Button, FormLabel, LineEdit, IntLineEdit, FormatDate)
import peewee
from models import CooperativeMember

from configuration import Config


class EditOrAddMemberDialog(QDialog, FWidget):

    def __init__(self, table_p, parent, scoop=None, member=None, *args, **kwargs):
        FWidget.__init__(self, parent, *args, **kwargs)

        self.table_p = table_p
        self.member = member
        self.scoop = scoop
        self.parent = parent
        full_name = ""
        sex = ""
        ddn = QDate.currentDate()
        addres = ""
        nationality = ""
        phone = ""
        poste = ""
        if self.member:
            self.new = False
            full_name = self.member.full_name
            sex = self.member.sex
            ddn = self.member.ddn
            addres = self.member.addres
            nationality = self.member.nationality
            phone = str(self.member.phone)
            sex = self.member.sex
            self.title = u"Modification de {}".format(self.member)
            self.succes_msg = u"{} a été bien mise à jour".format(
                self.member)
        else:
            self.new = True
            self.succes_msg = u"Client a été bien enregistré"
            self.title = u"Création d'un nouvel client"
            self.member = CooperativeMember()
        self.setWindowTitle(self.title)

        vbox = QVBoxLayout()
        # vbox.addWidget(FPageTitle(u"Utilisateur: %s " % self.member.name))

        self.full_name_field = LineEdit(full_name)
        # self.sex_field = LineEdit(self.member.sex)
        self.sex_list = CooperativeMember.SEX
        # Combobox widget
        self.sex_box = QComboBox()
        for index, value in enumerate(self.sex_list):
            self.sex_box.addItem(
                "{}".format(self.sex_list[value]))
            if self.member.sex == value:
                self.sex_box.setCurrentIndex(index)

        self.ddn_field = FormatDate(ddn)
        self.addres_field = LineEdit(addres)
        self.nationality_field = LineEdit(nationality)
        self.phone_field = IntLineEdit(phone)
        # self.phone_field.setInputMask("D9.99.99.99")
        # self.poste_box = LineEdit(self.member.poste)
        self.poste_list = CooperativeMember.POSTE
        # Combobox widget
        self.poste_box = QComboBox()
        for index, value in enumerate(self.poste_list):
            self.poste_box.addItem(
                "{}".format(self.poste_list[value]))
            if self.member.poste == value:
                self.poste_box.setCurrentIndex(index)

        formbox = QFormLayout()
        formbox.addRow(FormLabel(u"Nom complet : *"), self.full_name_field)
        formbox.addRow(FormLabel(u"Sexe :"), self.sex_box)
        formbox.addRow(FormLabel(u"Date de naissance :"), self.ddn_field)
        formbox.addRow(FormLabel(u"Adresse :"), self.addres_field)
        formbox.addRow(FormLabel(u"Nationalité :"), self.nationality_field)
        formbox.addRow(FormLabel(u"Téléphone :"), self.phone_field)
        formbox.addRow(FormLabel(u"Poste occupé :"), self.poste_box)

        butt = Button(u"Enregistrer")
        butt.clicked.connect(self.save_edit)
        formbox.addRow("", butt)

        vbox.addLayout(formbox)
        self.setLayout(vbox)

    def save_edit(self):
        ''' add operation '''
        # print("Save")
        self.member.scoop = self.scoop
        # self.member.scoop = self.scoop_field.text()
        self.member.full_name = self.full_name_field.text()
        self.member.sex = str(self.sex_box.currentText())
        self.member.ddn = self.ddn_field.text()
        self.member.addres = self.addres_field.text()
        self.member.nationality = self.nationality_field.text()
        phone = self.phone_field.text()
        if phone != "":
            self.member.phone = int(phone)
        self.member.poste = str(self.poste_box.currentText())
        # field_error
        if check_is_empty(self.full_name_field):
            return
        if check_is_empty(self.addres_field):
            return
        if check_is_empty(self.nationality_field):
            return

        member = self.member

        try:
            member.save()
            self.close()
            self.table_p.refresh_()
            self.parent.Notify(u"Le Compte %s a été mise à jour" %
                               member.full_name, "success")
        except peewee.IntegrityError:
            field_error(
                self.full_name_field, "Ce nom existe dans la basse de donnée.")
