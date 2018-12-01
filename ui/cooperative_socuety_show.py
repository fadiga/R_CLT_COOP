#!/usr/bin/env python
# -*- coding: utf-8 -*-
# maintainer: Fad
from __future__ import (
    unicode_literals, absolute_import, division, print_function)

# from datetime import datetime
from PyQt4.QtGui import (QVBoxLayout, QDialog,
                         QGroupBox, QFormLayout, QGridLayout)

from Common.ui.common import (FWidget, FLabel, FHeader)
# from models import CooperativeCompanie

# from configuration import Config


class CooperativeSocietyDialog(QDialog, FWidget):

    def __init__(self, parent, scoop=None, *args, **kwargs):
        FWidget.__init__(self, parent, *args, **kwargs)

        self.scoop = scoop
        self.dmd = self.scoop.demande()
        self.setWindowTitle(self.scoop.denomination)

        formbox = QFormLayout()
        formbox.addRow(FLabel(
            u"<strong>Date de la demande :</strong> {}".format(self.dmd.declaration_date)))
        formbox.addRow(FLabel(
            u"<strong>1. Dénomination Sociale de la société coopérative :</strong> {}".format(self.scoop.denomination)))
        formbox.addRow(FLabel(
            u"<strong>2. Nom Commercial / Sigle / Enseigne :</strong> {}".format(self.scoop.commercial_name)))
        formbox.addRow(FLabel(
            u"<strong>3. Année de création de la société coopérative :</strong> {}".format(self.scoop.created_year)))
        formbox.addRow(FLabel(
            u"<strong>4. Activités exercées :</strong> {}".format(self.scoop.activity)))
        formbox.addRow(FLabel(
            u"<strong>4. Filière :</strong> {}".format(self.scoop.spinneret)))
        formbox.addRow(FLabel(
            u"<strong>5. Forme de la société coopérative :</strong> {}".format(self.scoop.forme)))
        # Capital Social Initial
        capital_formbox = QFormLayout()
        capital_formbox.addRow(
            FLabel("<strong> Montant total : </strong> {}".format(self.scoop.apports_numeraire + self.scoop.apports_nature + self.scoop.apports_industrie)))
        capital_formbox.addRow(FLabel(
            "<strong> 6.1 Montant apports en numéraire : </strong> {}".format(self.scoop.apports_numeraire)))
        capital_formbox.addRow(FLabel(
            "<strong> 6.2 Montant apports en nature : </strong> {}".format(self.scoop.apports_nature)))
        capital_formbox.addRow(FLabel(
            "<strong> 6.3 Montant apports en industrie : </strong> {}".format(self.scoop.apports_industrie)))
        self.capitalSGroupBox = QGroupBox("6. Capital Social Initial")
        self.capitalSGroupBox.setLayout(capital_formbox)
        self.capitalSGroupBox.setMaximumWidth(1200)
        # Adresse du siège social
        addres_gribox = QGridLayout()
        addres_gribox.addWidget(
            FLabel("Région : {}".format(self.scoop.display_region())), 0, 0)
        addres_gribox.addWidget(
            FLabel("Cercle : {}".format(self.scoop.display_cercle())), 1, 0)
        # addres_gribox.addWidget(self.vline, 0, 3, 2, 5)
        addres_gribox.addWidget(FLabel(
            "Village/Fraction/Quartier : {}".format(self.scoop.display_commune())), 1, 1)
        addres_gribox.addWidget(
            FLabel("Rue : {}".format(self.scoop.rue)), 2, 0)
        addres_gribox.addWidget(
            FLabel("Porte (n°) {}".format(self.scoop.porte)), 2, 1)
        addres_gribox.addWidget(
            FLabel("Tel : {}".format(self.scoop.tel)), 3, 0)
        addres_gribox.addWidget(FLabel("BP : {}".format(self.scoop.bp)), 3, 1)
        addres_gribox.addWidget(
            FLabel("E-mail : {}".format(self.scoop.email)), 3, 2)

        duree_fbox = QFormLayout()
        duree_fbox.addRow(FLabel(
            u"8. Durée statutaire de la société coopérative:".format(self.scoop.duree_statutaire)))

        members_fbox = QFormLayout()
        rows = ""
        for i in self.scoop.membres():
            rows += """
                <tr style='background-color: #fff;text-align: left;'>
                    <td > {}</td><td> {}</td><td> {}</td><td> {}</td><td> {}</td><td> {}</td><td> {}</td>
                </tr>
                """.format(
                i.full_name, i.display_sex(), i.ddn, i.addres, i.nationality, i.phone, i.display_poste())

        members_fbox.addRow(FHeader("""
                <table>
                <tr style='background-color:green;color:#fff;text-align:center;padding:15px;margin:20px'>
                <th>Nom</th><th>sexe</th><th>Date de naissance</th><th>Adresse</th><th>Nationalie</th><th>Tel</th><th>Porte</th>
                </tr>
                {}
                </table>
        """.format(rows), ""))
        self.addresGroupBox = QGroupBox("7. Adresse du siège social")
        self.addresGroupBox.setLayout(addres_gribox)
        self.membersGroupBox = QGroupBox("Les membres de la coopérative")
        self.membersGroupBox.setLayout(members_fbox)
        vbox = QVBoxLayout()
        vbox.addWidget(FHeader("", "background-color: green; color:#fff"))
        vbox.addLayout(formbox)
        vbox.addWidget(self.capitalSGroupBox)
        vbox.addWidget(self.addresGroupBox)
        vbox.addLayout(duree_fbox)
        vbox.addWidget(self.membersGroupBox)
        self.setLayout(vbox)
