#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# vim: ai ts=4 sts=4 et sw=4 nu
# maintainer: Fad
from __future__ import (
    unicode_literals, absolute_import, division, print_function)

# from datetime import datetime

from PyQt4.QtCore import QDate, Qt
from PyQt4.QtGui import (
    QCheckBox, QVBoxLayout, QGridLayout, QFormLayout, QFrame, QComboBox, QGroupBox, QScrollArea)

from Common.ui.common import (
    FWidget, FormatDate, FPageTitle, FRLabel, Fhelper, FHeader, ErrorLabel,
    LineEdit, Button_save, FLabel, IntLineEdit)

from models import CheckList
from configuration import Config

from ui.registration_manager import ResgistrationManagerWidget


class CheckListViewWidget(FWidget):

    """ Shows the home page  """

    def __init__(self, parent=0, dmd=None, *args, **kwargs):
        super(CheckListViewWidget, self).__init__(
            parent=parent, *args, **kwargs)
        self.parent = parent
        self.dmd = dmd
        self.parentWidget().set_window_title("Check-list")

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
        # if self.organization.is_login:
        #     self.checked.setCheckState(Qt.Checked)
        self.hline = QFrame()
        self.hline.setFrameShape(QFrame.HLine)
        self.hline.setFrameShadow(QFrame.Sunken)
        col = 0
        self.piecesGroupBox = QGroupBox("")
        # self.piecesGroupBox.setStyleSheet("color: gray; background:#fff")
        pieces_v_gribox = QGridLayout()
        css = "font-size:26px;border: 3px solid #000;background: black;color: white;"
        pieces_v_gribox.addWidget(FHeader(
            "I. Pièces à vérifier (au dépôt)", css), col, 0, 1, 6)
        col += 1
        self.qualite_declarant_check = QCheckBox("(4)")
        pieces_v_gribox.addWidget(FRLabel(
            "Qualité du déclarant (Président, mandataire ou auxiliaire de Justice) "), col, 0)
        pieces_v_gribox.addWidget(self.qualite_declarant_check, col, 1)
        # col += 1
        self.status_check = QCheckBox("(4)")
        pieces_v_gribox.addWidget(FRLabel("Statuts "), col, 2)
        pieces_v_gribox.addWidget(self.status_check, col, 3)
        pieces_check = QCheckBox("(4)")
        pieces_v_gribox.addWidget(
            FRLabel("Règlement Intérieur "), col, 4)
        pieces_v_gribox.addWidget(pieces_check, col, 5)
        col += 1
        self.autorisation_pre_immt_check = QCheckBox("")
        pieces_v_gribox.addWidget(FRLabel(
            "Autorisations préalables pour les activités réglementées "), col, 0)
        pieces_v_gribox.addWidget(self.autorisation_pre_immt_check, col, 1)
        self.demande_immt_check = QCheckBox("(2)")
        pieces_v_gribox.addWidget(
            FRLabel("Demande d’Immatriculation "), col, 2)
        pieces_v_gribox.addWidget(self.demande_immt_check, col, 3)
        self.pv_check = QCheckBox("(4)")
        pieces_v_gribox.addWidget(FRLabel("PV "), col, 4)
        pieces_v_gribox.addWidget(self.pv_check, col, 5)
        col = 0
        pieces_gribox = QGridLayout()
        chronologique_check = QCheckBox(
            "SCOOPS Art 235 et 236 COOP-CA Art 320, 321, 322 et 323")
        pieces_gribox.addWidget(FRLabel(
            "Vérifier l’existence du registre des membres tenu par ordre chronologique "), col, 0)
        pieces_gribox.addWidget(chronologique_check, col, 1)
        col += 1
        compte_check = QCheckBox("Art 213")
        pieces_gribox.addWidget(FRLabel(
            "Vérifier l’existence d’un compte bancaire / Institution de Micro Finance"), col, 0)
        pieces_gribox.addWidget(compte_check, col, 1)
        col += 1
        self.dispositions_check = QCheckBox("Art 300 et 326")
        pieces_gribox.addWidget(FRLabel(
            "Vérifier le respect des dispositions sur le non cumul des mandats"), col, 0)
        pieces_gribox.addWidget(self.dispositions_check, col, 1)
        col += 1
        self.pv_delib_ca_check = QCheckBox(
            "Art : 235, (d’ordre général) et COOP-CA 320")
        pieces_gribox.addWidget(FRLabel(
            "Vérifier l’existence du registre des procès- verbaux de délibération du CA <br/> des COOP-CA coté et paraphé par le tribunal civil compétent"), col, 0)
        pieces_gribox.addWidget(self.pv_delib_ca_check, col, 1)
        col = 0
        # pieces_gribox.setColumnStretch(6, 5)
        mentions_gribox = QGridLayout()
        mentions_gribox.addWidget(FHeader(
            " II. Mentions à vérifier dans les Statuts et le Règlement Intérieur", css), col, 0, 1, 4)
        col += 1
        css = "color:blue;font-size:26px;border: 1px solid #000;background: black;color: white;"
        mentions_gribox.addWidget(FHeader("Mentions", css=css), col, 0)
        mentions_gribox.addWidget(
            FHeader("N° Art des Statuts", css=css), col, 1)
        mentions_gribox.addWidget(FHeader("N° Art du R.I", css=css), col, 2)
        mentions_gribox.addWidget(
            FHeader("Référence OHADA", css=css), col, 3)
        col += 1
        self.forme_scoop_status_field = IntLineEdit()
        self.forme_scoop_ri_field = IntLineEdit()
        self.add_element(mentions_gribox, col, "01. La forme de la société coopérative",
                         self.forme_scoop_status_field, self.forme_scoop_ri_field,
                         "Art 204 ,215 et 216 Pour la SCOOPS / Art 267 et de 271 à 290 Pour la COOP-CA")
        col += 1
        self.denomination_status_field = IntLineEdit()
        self.denomination_ri_field = IntLineEdit()
        self.add_element(mentions_gribox, col, "02. Sa dénomination suivie, le cas échéant, de son sigle",
                         self.denomination_status_field, self.denomination_ri_field,
                         "Art 19 et Art 205 Pour la SCOOPS<br/> Art 19 et 205 Pour COOP-CA")
        col += 1
        self.nature_domaine_status_field = IntLineEdit()
        self.nature_domaine_ri_field = IntLineEdit()
        self.add_element(mentions_gribox, col, "03. La nature et le domaine de son activité et qui forment son objet social",
                         self.nature_domaine_status_field, self.nature_domaine_ri_field,
                         "Art 5, Art 20 et 21 Pour toutes les formes<br/> de Sociétés Coopératives")
        col += 1
        self.duree_status_field = IntLineEdit()
        self.duree_ri_field = IntLineEdit()
        self.add_element(mentions_gribox, col, "04. Son siège et sa durée",
                         self.duree_status_field, self.duree_ri_field,
                         "Pour le Siège : Art 22 ,23 et 24 et Pour<br/> la Durée : Art 25, 26, 27et 28")
        col += 1
        self.duree_status_field = IntLineEdit()
        self.duree_ri_field = IntLineEdit()
        self.add_element(mentions_gribox, col, "04. Son siège et sa durée",
                         self.duree_status_field, self.duree_ri_field,
                         "Pour le Siège : Art 22 ,23 et 24 et Pour<br/> la Durée : Art 25, 26, 27et 28")
        col += 1
        self.status_field = IntLineEdit()
        self.ri_field = IntLineEdit()
        self.add_element(mentions_gribox, col, "Le lien commun qui réunit les membres,",
                         self.status_field, self.ri_field, "Art 8")
        col += 1
        self.status_field = IntLineEdit()
        self.ri_field = IntLineEdit()
        self.add_element(mentions_gribox, col, "06 Les noms, prénoms et adresse résidentielle de chaque initiateur",
                         self.status_field, self.ri_field, "Art 87")
        col += 1
        self.status_field = IntLineEdit()
        self.ri_field = IntLineEdit()
        self.add_element(mentions_gribox, col, "07 Le nombre précis ou les nombres minimal et maximal de ses <br/> administrateurs ou membres du comité de gestion",
                         self.status_field, self.ri_field, "Art 204 et Art 223 Pour la SCOOPS : <br/> (Effectif : 5 Pers au mini : CG=3 au plus si adh de 5 à 99 et CG = 5 si adh de 100 et +.")
        col += 1
        self.status_field = IntLineEdit()
        self.ri_field = IntLineEdit()
        self.add_element(mentions_gribox, col, "Le nombre précis ou les nombres minimal et maximal de ses <br/> administrateurs ou membres du Conseil d’Administration;",
                         self.status_field, self.ri_field, "Art 207 et Art 223 Pour la COOP-CA: (Effectif : 15 Pers au mini : CA=3 au moins et 12 au plus.")
        col += 1
        self.status_field = IntLineEdit()
        self.ri_field = IntLineEdit()
        self.add_element(mentions_gribox, col, "Les dispositions portant limitation des pouvoirs des <br/> administrateurs ou membres du comité de gestion",
                         self.status_field, self.ri_field, "Art 224 à Art 230 Pour la SCOOPS")
        col += 1
        self.status_field = IntLineEdit()
        self.ri_field = IntLineEdit()
        self.add_element(mentions_gribox, col, "Les dispositions portant limitation des pouvoirs des <br/> administrateurs ou membres du Conseil d’Administration",
                         self.status_field, self.ri_field, "Art 296 à Art 307 Pour la COOP-CA et autres pouvoirs de l’Art 314 à l’Art 333")
        col += 1
        self.status_field = IntLineEdit()
        self.ri_field = IntLineEdit()
        self.add_element(mentions_gribox, col, "08 Le nombre précis ou les nombres minimal et maximal <br/> des membres de la Commission de Surveillance",
                         self.status_field, self.ri_field, "Art 258 Pour la SCOOPS (de 3 à 5 Pers)")
        col += 1
        self.status_field = IntLineEdit()
        self.ri_field = IntLineEdit()
        self.add_element(mentions_gribox, col, "Le nombre précis ou les nombres minimal et maximal des <br/> membres du Conseil de Surveillance",
                         self.status_field, self.ri_field, "Art 335 Pour la COOP-CA (de 3 à 5 Pers)")
        col += 1
        self.status_field = IntLineEdit()
        self.ri_field = IntLineEdit()
        self.add_element(mentions_gribox, col, "Les dispositions relatives à l’exercice efficace des missions de ces organes",
                         self.status_field, self.ri_field, "Art 263 Pour la SCOOPS /Art 341 Pour la COOP-CA")
        col += 1
        self.status_field = IntLineEdit()
        self.ri_field = IntLineEdit()
        self.add_element(mentions_gribox, col, "09 La durée du mandat des membres du comité de gestion, du conseil d’administration, <br/> du comité de surveillance et du conseil de surveillance",
                         self.status_field, self.ri_field, "Art 224 (Réf aux statuts) Pour la SCOOPS /Art 295 Pour la COOP-CA (Réf aux statuts)")
        col += 1
        self.status_field = IntLineEdit()
        self.ri_field = IntLineEdit()
        self.add_element(mentions_gribox, col, "10 Toute limite relative au pourcentage maximal de parts <br/> sociales que peut détenir un seul membre Pour la SCOOPS",
                         self.status_field, self.ri_field, "Art 210 Réf aux statuts et ne peut excéder 5 fois <br/> le montant des parts sociales souscrites) Pour la COOP-CA Art 371")
        col += 1
        self.status_field = IntLineEdit()
        self.ri_field = IntLineEdit()
        self.add_element(mentions_gribox, col, "11 Une déclaration précisant que la société coopérative est organisée et exploitée <br/> et exerce ses activités selon les principes coopératifs et le rappel de ces principes", self.status_field, self.ri_field, "Art 6")
        col += 1
        self.status_field = IntLineEdit()
        self.ri_field = IntLineEdit()
        self.add_element(mentions_gribox, col, "12 L’identité des apporteurs en numéraires avec pour chacun d’eux le montant des <br/> apports, le nombre et la valeur des parts sociales remis en contrepartie de chaque apport",
                         self.status_field, self.ri_field, "Art 30, 31, 32, 33,35, 36,")
        col += 1
        self.status_field = IntLineEdit()
        self.ri_field = IntLineEdit()
        self.add_element(mentions_gribox, col, "13 L’identité des apporteurs en nature",
                         self.status_field, self.ri_field, "Point 12 de l’Art 18")
        col += 1
        self.status_field = IntLineEdit()
        self.ri_field = IntLineEdit()
        self.add_element(mentions_gribox, col, "La nature et l’évaluation de l’apport effectué par chacun d’eux, <br/> le nombre et la valeur des parts sociales remises en contrepartie de chaque apport, <br/> Le régime des biens ou valeurs apportés lorsque leur valeur excède celle des apports exigés ;",
                         self.status_field, self.ri_field, "Point 13 de l’Art 18")
        col += 1
        self.status_field = IntLineEdit()
        self.ri_field = IntLineEdit()
        self.add_element(mentions_gribox, col, "Le montant du capital social, les limitations minimales et maximales y afférentes",
                         self.status_field, self.ri_field, "Art 53, 57 et 58 en général. Art 207 Pour la SCOOPS et 269 Pour la COOP-CA")
        col += 1
        self.status_field = IntLineEdit()
        self.ri_field = IntLineEdit()
        self.add_element(mentions_gribox, col, "La valeur nominale des diverses catégories de parts, les <br/> conditions précises de leur émission ou souscription ;",
                         self.status_field, self.ri_field, "Art 44 et 45 en général. Pour la COOP-CA Art 376 et 377")
        col += 1
        self.status_field = IntLineEdit()
        self.ri_field = IntLineEdit()
        self.add_element(mentions_gribox, col, "Les stipulations relatives à la répartition du résultat <br/> et notamment, des excédents et des réserves ;",
                         self.status_field, self.ri_field, "Art 46 alinéa en général. Pour SCOOPS alinéa 2 de l’Art 209 Pour la COOP-CA Art 363 alinéa 4")
        col += 1
        self.status_field = IntLineEdit()
        self.ri_field = IntLineEdit()
        self.add_element(mentions_gribox, col, "16. Les modalités de fonctionnement de la société coopérative ;",
                         self.status_field, self.ri_field, "Art 95 à 121 en général .Pour SCOOPS art 217 à 263 Pour la COOP-CA Art 291 à 368")
        col += 1
        self.status_field = IntLineEdit()
        self.ri_field = IntLineEdit()
        self.add_element(mentions_gribox, col, "17. La signature des initiateurs ou l’apposition de leur empreinte digitale",
                         self.status_field, self.ri_field, "Point 17 de l’Art 18")
        col += 1
        self.status_field = IntLineEdit()
        self.ri_field = IntLineEdit()
        self.add_element(mentions_gribox, col, "18. L’étendue des transactions avec les usagers non coopérateurs, <br/>tout en ayant en vue la sauvegarde de l’autonomie de la société coopérative ;",
                         self.status_field, self.ri_field, "Art 4 al. 2")
        col += 1
        mentions_gribox.addWidget(FHeader(
            "Les mentions facultatives", "background: #41cd52;font-size:20px;color:#fff"), col, 0, 1, 4)
        col += 1
        self.status_field = IntLineEdit()
        self.ri_field = IntLineEdit()
        self.add_element(mentions_gribox, col, "1. a) Le taux de rendement maximal qui peut être appliqué aux prêts et aux épargnes des membres",
                         self.status_field, self.ri_field, "Art 18. 1bis alinéa 1")
        col += 1
        self.status_field = IntLineEdit()
        self.ri_field = IntLineEdit()
        self.add_element(mentions_gribox, col, "1. b) Le taux de rémunération maximale qui peut être appliqué aux parts de membres ;",
                         self.status_field, self.ri_field, "Art 239 ; 240 alinéa4 et 231(Art 18. 1bis alinéa 1)")
        col += 1
        self.status_field = IntLineEdit()
        self.ri_field = IntLineEdit()
        self.add_element(mentions_gribox, col, "2. Toute limite imposée aux activités commerciales de la société coopérative.",
                         self.status_field, self.ri_field, "COOP–CA Art 313,SCOOPS Art 258 et 259")
        col += 1
        mentions_gribox.addWidget(FHeader(
            "Règlement Intérieur, outre les mentions obligatoires des statuts, le règlement intérieur contient les prescriptions suivantes :", "background: #41cd52;font-size:20px;color:#fff"), col, 0, 1, 4)
        col += 1
        self.status_field = IntLineEdit()
        self.ri_field = IntLineEdit()
        self.add_element(mentions_gribox, col, "1. Les conditions de paiement d’indemnités aux membres du <br/>conseil d’administration ou du comité de gestion, du conseil ou du comité <br/>de surveillance, définies dans le respect des dispositions des articles 225 et 305 ;",
                         self.status_field, self.ri_field, "Scoops : Art 225; Scoop-CA : Art 305")
        col += 1
        self.status_field = IntLineEdit()
        self.ri_field = IntLineEdit()
        self.add_element(mentions_gribox, col, "2. La souscription de parts sociales supplémentaires et leur nombre par coopérateur ;",
                         self.status_field, self.ri_field, "Pour la SCOOPS Art 210 Réf aux statuts et ne peut excéder <br/>5 fois le montant des parts sociales souscrites) Pour la COOP-CA Art 371")
        col += 1
        self.status_field = IntLineEdit()
        self.ri_field = IntLineEdit()
        self.add_element(mentions_gribox, col, "3. Les critères et conditions de suspension des coopérateurs;",
                         self.status_field, self.ri_field, "Statut (initiateurs)")
        col += 1
        self.status_field = IntLineEdit()
        self.ri_field = IntLineEdit()
        self.add_element(mentions_gribox, col, "4. La possibilité d’attribution d’un droit de vote plural dans le cas des <br/>unions, des fédérations et des confédérations ;",
                         self.status_field, self.ri_field, "Art 138)")
        col += 1
        self.status_field = IntLineEdit()
        self.ri_field = IntLineEdit()
        self.add_element(mentions_gribox, col, "5. Toutes autres prescriptions jugées nécessaires pour la réalisation de l’objet <br/>de la société coopérative et conformes aux principes <br/>coopératifs et aux dispositions impératives du présent Acte uniforme.",
                         self.status_field, self.ri_field, "Art 138)")
        vbox = QVBoxLayout()
        vbox.addLayout(pieces_v_gribox)
        vbox.addLayout(pieces_gribox)
        vbox.addLayout(mentions_gribox)
        self.piecesGroupBox.setLayout(vbox)
        # Durée statutaire de la société coopérative
        duree_fbox = QFormLayout()
        butt_continous = Button_save(u"continuer")
        butt_continous.clicked.connect(self.goto_immatriculation)
        duree_fbox.addRow("", butt_continous)

        scroll = QScrollArea(self)
        scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        scroll.setWidgetResizable(True)
        # scroll.setFixedHeight(200)
        vbox = QVBoxLayout()
        vbox.addWidget(FPageTitle(
            "<h2>Check-list de Contrôle de dossiers des sociétés coopératives avant l’immatriculation et l’enregistrement par le SLDS-ES</h2>"))
        vbox.addWidget(FHeader(
            "<h4> Société Coopérative : {} </h4>".format(self.dmd.scoop)))
        scroll.setWidget(self.piecesGroupBox)
        vbox.addWidget(scroll)
        vbox.addLayout(duree_fbox)
        self.setLayout(vbox)

    def to_int_or_none(self, value):
        if isinstance(value, int):
            return value
        else:
            None

    def save(self):
        print(self.forme_scoop_status_field.text())
        self.check_l = CheckList()
        self.check_l.forme_scoop_status = self.to_int_or_none(
            self.forme_scoop_status_field.text())
        self.check_l.forme_scoop_ri = self.to_int_or_none(
            self.forme_scoop_ri_field.text())
        self.check_l.denomination_status = self.to_int_or_none(
            self.denomination_status_field.text())
        self.check_l.denomination_ri = self.to_int_or_none(
            self.denomination_ri_field.text())
        self.check_l.nature_domaine_status = self.to_int_or_none(
            self.nature_domaine_status_field.text())
        self.check_l.nature_domaine_ri = self.to_int_or_none(
            self.nature_domaine_ri_field.text())
        self.check_l.duree_status = self.to_int_or_none(
            self.duree_status_field.text())
        self.check_l.duree_ri = self.to_int_or_none(self.duree_ri_field.text())
        print(self.check_l)

    def add_element(self, objet_, col, text, field1, field2, helper=None):
        field1.textChanged.connect(self.save)
        field2.textChanged.connect(self.save)
        objet_.addWidget(FHeader(text), col, 0)
        objet_.addWidget(field1, col, 1)
        objet_.addWidget(field2, col, 2)
        if helper:
            objet_.addWidget(
                FHeader(helper, css="font-size: 15px;"), col, 3)

    def goto_immatriculation(self):
        # self.save()
        from ui.immatriculation import ImmatriculationWidget
        self.parent.change_context(ImmatriculationWidget, scoop=self.scoop)
