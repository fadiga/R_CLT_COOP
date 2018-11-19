#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# vim: ai ts=4 sts=4 et sw=4 nu
# maintainer: Fad
from __future__ import (
    unicode_literals, absolute_import, division, print_function)

# from datetime import datetime

from PyQt4.QtCore import Qt
from PyQt4.QtGui import (
    QCheckBox, QVBoxLayout, QGridLayout, QFormLayout, QGroupBox, QScrollArea)

from Common.ui.util import check_is_empty
from Common.ui.common import (
    FWidget, FPageTitle, FRLabel, FHeader, Button_save, FLabel, IntLineEdit)
from models import Demande


class CheckListViewWidget(FWidget):

    """ Shows the home page  """

    def __init__(self, parent=0, dmd=None, *args, **kwargs):
        super(CheckListViewWidget, self).__init__(
            parent=parent, *args, **kwargs)
        self.parent = parent
        self.dmd = dmd
        self.check_list = self.dmd.check_list
        self.parentWidget().set_window_title("Check-list")
        row = 0
        self.piecesGroupBox = QGroupBox("")
        # self.piecesGroupBox.setStyleSheet("color: gray; background:#fff")
        pieces_v_gribox = QGridLayout()
        css = "font-size:26px;border: 3px solid #000;background: black;color: white;"
        pieces_v_gribox.addWidget(FHeader(
            "I. Pièces à vérifier (au dépôt)", css), row, 0, 1, 6)
        row += 1
        self.qualite_declarant_check = self.check_box(QCheckBox())
        self.qualite_declarant_check.setChecked(
            self.check_list.qualite_declarant_check)
        pieces_v_gribox.addWidget(FRLabel(
            "Qualité du déclarant (Président, mandataire ou auxiliaire de Justice) "), row, 0)
        pieces_v_gribox.addWidget(self.qualite_declarant_check, row, 1)
        # row += 1
        self.status_check = self.check_box(QCheckBox("(4)"))
        self.status_check.setChecked(self.check_list.status_check)
        pieces_v_gribox.addWidget(FRLabel("Statuts "), row, 2)
        pieces_v_gribox.addWidget(self.status_check, row, 3)
        self.pieces_check = self.check_box(QCheckBox("(4)"))
        self.pieces_check.setChecked(self.check_list.pieces_check)
        pieces_v_gribox.addWidget(
            FRLabel("Règlement Intérieur "), row, 4)
        pieces_v_gribox.addWidget(self.pieces_check, row, 5)
        row += 1
        self.autorisation_pre_immt_check = self.check_box(QCheckBox())
        self.autorisation_pre_immt_check.setChecked(
            self.check_list.autorisation_pre_immt_check)
        pieces_v_gribox.addWidget(FRLabel(
            "Autorisations préalables pour les activités réglementées "), row, 0)
        pieces_v_gribox.addWidget(self.autorisation_pre_immt_check, row, 1)
        self.demande_immt_check = self.check_box(QCheckBox("(2)"))
        self.demande_immt_check.setChecked(self.check_list.demande_immt_check)
        pieces_v_gribox.addWidget(
            FRLabel("Demande d’Immatriculation "), row, 2)
        pieces_v_gribox.addWidget(self.demande_immt_check, row, 3)
        self.pv_check = self.check_box(QCheckBox("(4)"))
        self.pv_check.setChecked(self.check_list.pv_check)
        pieces_v_gribox.addWidget(FRLabel("PV "), row, 4)
        pieces_v_gribox.addWidget(self.pv_check, row, 5)
        row = 0
        pieces_gribox = QGridLayout()
        self.chronologique_check = self.check_box(QCheckBox())
        self.chronologique_check.setChecked(
            self.check_list.chronologique_check)
        pieces_gribox.addWidget(FLabel(
            "Vérifier l’existence du registre des membres tenu par ordre chronologique "), row, 0)
        pieces_gribox.addWidget(self.chronologique_check, row, 1)
        pieces_gribox.addWidget(FHeader(
            "SCOOPS Art 235 et 236 COOP-CA Art 320, 321, 322 et 323", "font-size:15px"), row, 2)
        row += 1
        self.compte_check = self.check_box(QCheckBox())
        self.compte_check.setChecked(self.check_list.compte_check)
        pieces_gribox.addWidget(FLabel(
            "Vérifier l’existence d’un compte bancaire / Institution de Micro Finance"), row, 0)
        pieces_gribox.addWidget(self.compte_check, row, 1)
        pieces_gribox.addWidget(FHeader(
            "Art 213", "font-size:15px"), row, 2)
        row += 1
        self.dispositions_check = self.check_box(QCheckBox())
        self.dispositions_check.setChecked(self.check_list.dispositions_check)
        pieces_gribox.addWidget(FLabel(
            "Vérifier le respect des dispositions sur le non cumul des mandats"), row, 0)
        pieces_gribox.addWidget(self.dispositions_check, row, 1)
        pieces_gribox.addWidget(FHeader(
            "Art 300 et 326", "font-size:15px"), row, 2)
        row += 1
        self.pv_delib_ca_check = self.check_box(QCheckBox())
        self.pv_delib_ca_check.setChecked(self.check_list.pv_delib_ca_check)
        pieces_gribox.addWidget(FLabel(
            "Vérifier l’existence du registre des procès- verbaux de délibération du CA <br/> des COOP-CA coté et paraphé par le tribunal civil compétent"), row, 0)
        pieces_gribox.addWidget(self.pv_delib_ca_check, row, 1)
        pieces_gribox.addWidget(FHeader(
            "Art : 235, (d’ordre général) et COOP-CA 320", "font-size:15px"), row, 2)
        pieces_gribox.setColumnStretch(row, 2)
        row = 0
        mentions_gribox = QGridLayout()
        mentions_gribox.addWidget(FHeader(
            " II. Mentions à vérifier dans les Statuts et le Règlement Intérieur", css), row, 0, 1, 4)
        row += 1
        css = "color:blue;font-size:26px;border: 1px solid #000;background: black;color: white;"
        mentions_gribox.addWidget(FHeader("Mentions", css=css), row, 0)
        mentions_gribox.addWidget(
            FHeader("N° Art des Statuts", css=css), row, 1)
        mentions_gribox.addWidget(FHeader("N° Art du R.I", css=css), row, 2)
        mentions_gribox.addWidget(
            FHeader("Référence OHADA", css=css), row, 3)
        row += 1
        self.forme_scoop_status_field = IntLineEdit(self.rest_d(
            self.check_list.forme_scoop_status))
        self.forme_scoop_ri_field = IntLineEdit(self.rest_d(
            self.check_list.forme_scoop_ri))
        self.add_element(mentions_gribox, row, "<b>01.</b> La forme de la société coopérative",
                         self.forme_scoop_status_field, self.forme_scoop_ri_field,
                         "Art 204 ,215 et 216 Pour la SCOOPS / Art 267 et de 271 à 290 Pour la COOP-CA")
        row += 1
        self.denomination_status_field = IntLineEdit(self.rest_d(
            self.check_list.denomination_status))
        self.denomination_ri_field = IntLineEdit(self.rest_d(
            self.check_list.denomination_ri))
        self.add_element(mentions_gribox, row, "<b>02.</b> Sa dénomination suivie, le cas échéant, de son sigle",
                         self.denomination_status_field, self.denomination_ri_field,
                         "Art 19 et Art 205 Pour la SCOOPS<br/> Art 19 et 205 Pour COOP-CA")
        row += 1
        self.nature_domaine_status_field = IntLineEdit(self.rest_d(
            self.check_list.nature_domaine_status))
        self.nature_domaine_ri_field = IntLineEdit(self.rest_d(
            self.check_list.nature_domaine_ri))
        self.add_element(mentions_gribox, row, "<b>03.</b> La nature et le domaine de son activité et qui forment son objet social",
                         self.nature_domaine_status_field, self.nature_domaine_ri_field,
                         "Art 5, Art 20 et 21 Pour toutes les formes<br/> de Sociétés Coopératives")
        row += 1
        self.duree_status_field = IntLineEdit(self.rest_d(
            self.check_list.duree_status))
        self.duree_ri_field = IntLineEdit(self.rest_d(
            self.check_list.duree_ri))
        self.add_element(mentions_gribox, row, "<b>04.</b> Son siège et sa durée",
                         self.duree_status_field, self.duree_ri_field,
                         "Pour le Siège : Art 22 ,23 et 24 et Pour<br/> la Durée : Art 25, 26, 27et 28")
        row += 1
        self.lien_commun_status_field = IntLineEdit(self.rest_d(
            self.check_list.lien_commun_status))
        self.lien_commun_ri_field = IntLineEdit(self.rest_d(
            self.check_list.lien_commun_ri))
        self.add_element(mentions_gribox, row, "<b>05.</b> Le lien commun qui réunit les membres,",
                         self.lien_commun_status_field, self.lien_commun_ri_field, "Art 8")
        row += 1
        self.coord_initiateur_status_field = IntLineEdit(self.rest_d(
            self.check_list.coord_initiateur_status))
        self.coord_initiateur_ri_field = IntLineEdit(self.rest_d(
            self.check_list.coord_initiateur_ri))
        self.add_element(mentions_gribox, row, "<b>06.</b> Les noms, prénoms et adresse résidentielle de chaque initiateur",
                         self.coord_initiateur_status_field, self.coord_initiateur_ri_field, "Art 87")
        row += 1
        self.max_min_admin_cg_status_field = IntLineEdit(self.rest_d(
            self.check_list.max_min_admin_cg_status))
        self.max_min_admin_cg_ri_field = IntLineEdit(self.rest_d(
            self.check_list.max_min_admin_cg_ri))
        self.add_element(mentions_gribox, row, "<b>07. a.</b> Le nombre précis ou les nombres minimal et maximal de ses administrateurs <br/>  	ou membres du comité de gestion</p>",
                         self.max_min_admin_cg_status_field, self.max_min_admin_cg_ri_field, "Art 204 et Art 223 Pour la SCOOPS : <br/> (Effectif : 5 Pers au mini : CG=3 au plus si adh de 5 à 99 et CG = 5 si adh de 100 et +.")
        row += 1
        self.max_min_admin_ca_status_field = IntLineEdit(self.rest_d(
            self.check_list.max_min_admin_ca_status))
        self.max_min_admin_ca_ri_field = IntLineEdit(self.rest_d(
            self.check_list.max_min_admin_ca_ri))
        self.add_element(mentions_gribox, row, "<b>07. b.</b> Le nombre précis ou les nombres minimal et maximal de ses <br/> administrateurs ou membres du Conseil d’Administration;",
                         self.max_min_admin_ca_status_field, self.max_min_admin_ca_ri_field, "Art 207 et Art 223 Pour la COOP-CA: (Effectif : 15 Pers au mini : CA=3 au moins et 12 au plus.")
        row += 1
        self.dispositions_cg_status_field = IntLineEdit(self.rest_d(
            self.check_list.dispositions_cg_status))
        self.dispositions_cg_ri_field = IntLineEdit(self.rest_d(
            self.check_list.dispositions_cg_ri))
        self.add_element(mentions_gribox, row, "<b>07. c.</b> Les dispositions portant limitation des pouvoirs des <br/> administrateurs ou membres du comité de gestion",
                         self.dispositions_cg_status_field, self.dispositions_cg_ri_field, "Art 224 à Art 230 Pour la SCOOPS")
        row += 1
        self.dispositions_ca_status_field = IntLineEdit(self.rest_d(
            self.check_list.dispositions_ca_status))
        self.dispositions_ca_ri_field = IntLineEdit(self.rest_d(
            self.check_list.dispositions_ca_ri))
        self.add_element(mentions_gribox, row, "<b>07. d.</b> Les dispositions portant limitation des pouvoirs des administrateurs ou <br/>membres du Conseil d’Administration",
                         self.dispositions_ca_status_field, self.dispositions_ca_ri_field, "Art 296 à Art 307 Pour la COOP-CA et autres pouvoirs de l’Art 314 à l’Art 333")
        row += 1
        self.max_min_cs_s_status_field = IntLineEdit(self.rest_d(
            self.check_list.max_min_cs_s_status))
        self.max_min_cs_s_ri_field = IntLineEdit(self.rest_d(
            self.check_list.max_min_cs_s_ri))
        self.add_element(mentions_gribox, row, "<b>08.</b> Le nombre précis ou les nombres minimal et maximal des membres de la <br/>Commission de Surveillance",
                         self.max_min_cs_s_status_field, self.max_min_cs_s_ri_field, "Art 258 Pour la SCOOPS (de 3 à 5 Pers)")
        row += 1
        self.max_min_cs_ca_status_field = IntLineEdit(self.rest_d(
            self.check_list.max_min_cs_ca_status))
        self.max_min_cs_ca_ri_field = IntLineEdit(self.rest_d(
            self.check_list.max_min_cs_ca_ri))
        self.add_element(mentions_gribox, row, "<b>08. a.</b> Le nombre précis ou les nombres minimal et maximal des membres du <br/>Conseil de Surveillance",
                         self.max_min_cs_ca_status_field, self.max_min_cs_ca_ri_field, "Art 335 Pour la COOP-CA (de 3 à 5 Pers)")
        row += 1
        self.dispositions_mo_status_field = IntLineEdit(self.rest_d(
            self.check_list.dispositions_mo_status))
        self.dispositions_mo_ri_field = IntLineEdit(self.rest_d(
            self.check_list.dispositions_mo_ri))
        self.add_element(mentions_gribox, row, "<b>08. b.</b> Les dispositions relatives à l’exercice efficace des missions de ces organes",
                         self.dispositions_mo_status_field, self.dispositions_mo_ri_field, "Art 263 Pour la SCOOPS /Art 341 Pour la COOP-CA")
        row += 1
        self.mandat_cs_status_field = IntLineEdit(self.rest_d(
            self.check_list.mandat_cs_status))
        self.mandat_cs_ri_field = IntLineEdit(self.rest_d(
            self.check_list.mandat_cs_ri))
        self.add_element(mentions_gribox, row, "<b>09.</b> La durée du mandat des membres du comité de gestion, du conseil d’administration, <br/> du comité de surveillance et du conseil de surveillance",
                         self.mandat_cs_status_field, self.mandat_cs_ri_field, "Art 224 (Réf aux statuts) Pour la SCOOPS /Art 295 Pour la COOP-CA (Réf aux statuts)")
        row += 1
        self.parts_sociales_status_field = IntLineEdit(self.rest_d(
            self.check_list.parts_sociales_status))
        self.parts_sociales_ri_field = IntLineEdit(self.rest_d(
            self.check_list.parts_sociales_ri))
        self.add_element(mentions_gribox, row, "<b>10.</b> Toute limite relative au pourcentage maximal de parts sociales que peut détenir <br/> un seul membre Pour la SCOOPS",
                         self.parts_sociales_status_field, self.parts_sociales_ri_field, "Art 210 Réf aux statuts et ne peut excéder 5 fois <br/> le montant des parts sociales souscrites) Pour la COOP-CA Art 371")
        row += 1
        self.declatation_status_field = IntLineEdit(self.rest_d(
            self.check_list.declatation_status))
        self.declatation_ri_field = IntLineEdit(self.rest_d(
            self.check_list.declatation_ri))
        self.add_element(mentions_gribox, row, "<b>11.</b> Une déclaration précisant que la société coopérative est organisée et exploitée <br/> et exerce ses activités selon les principes coopératifs et le rappel de ces principes",
                         self.declatation_status_field, self.declatation_ri_field, "Art 6")
        row += 1
        self.id_apport_numeraire_status_field = IntLineEdit(self.rest_d(
            self.check_list.id_apport_numeraire_status))
        self.id_apport_numeraire_ri_field = IntLineEdit(self.rest_d(
            self.check_list.id_apport_numeraire_ri))
        self.add_element(mentions_gribox, row, "<b>12.</b> L’identité des apporteurs en numéraires avec pour chacun d’eux le montant des <br/> apports, le nombre et la valeur des parts sociales remis en contrepartie de chaque apport",
                         self.id_apport_numeraire_status_field, self.id_apport_numeraire_ri_field, "Art 30, 31, 32, 33,35, 36,")
        row += 1
        self.id_apport_nature_status_field = IntLineEdit(self.rest_d(
            self.check_list.id_apport_nature_status))
        self.id_apport_nature_ri_field = IntLineEdit(self.rest_d(
            self.check_list.id_apport_nature_ri))
        self.add_element(mentions_gribox, row, "<b>13. a.</b> L’identité des apporteurs en nature",
                         self.id_apport_nature_status_field, self.id_apport_nature_ri_field, "Point 12 de l’Art 18")
        row += 1
        self.evaluation_apport_status_field = IntLineEdit(self.rest_d(
            self.check_list.evaluation_apport_status))
        self.evaluation_apport_ri_field = IntLineEdit(self.rest_d(
            self.check_list.evaluation_apport_ri))
        self.add_element(mentions_gribox, row, "<b>13. b.</b> La nature et l’évaluation de l’apport effectué par chacun d’eux, le nombre et la valeur <br/>des parts sociales remises en contrepartie de chaque apport,  Le régime des biens ou valeurs apportés <br/>lorsque leur valeur excède celle des apports exigés ;",
                         self.evaluation_apport_status_field, self.evaluation_apport_ri_field, "Point 13 de l’Art 18")
        row += 1
        self.capital_social_status_field = IntLineEdit(self.rest_d(
            self.check_list.capital_social_status))
        self.capital_social_ri_field = IntLineEdit(self.rest_d(
            self.check_list.capital_social_ri))
        self.add_element(mentions_gribox, row, "<b>14. a.</b> Le montant du capital social, les limitations minimales et maximales y afférentes",
                         self.capital_social_status_field, self.capital_social_ri_field, "Art 53, 57 et 58 en général. Art 207 Pour la SCOOPS et 269 Pour la COOP-CA")
        row += 1
        self.valeur_nominale_status_field = IntLineEdit(self.rest_d(
            self.check_list.valeur_nominale_status))
        self.valeur_nominale_ri_field = IntLineEdit(self.rest_d(
            self.check_list.valeur_nominale_ri))
        self.add_element(mentions_gribox, row, "<b>14. b.</b> La valeur nominale des diverses catégories de parts, les conditions précises de leur émission<br/> ou souscription ;",
                         self.valeur_nominale_status_field, self.valeur_nominale_ri_field, "Art 44 et 45 en général. Pour la COOP-CA Art 376 et 377")
        row += 1
        self.stipulations_status_field = IntLineEdit(self.rest_d(
            self.check_list.stipulations_status))
        self.stipulations_ri_field = IntLineEdit(self.rest_d(
            self.check_list.stipulations_ri))
        self.add_element(mentions_gribox, row, "<b>15.</b> Les stipulations relatives à la répartition du résultat et notamment, des excédents<br/> et des réserves ;",
                         self.stipulations_status_field, self.stipulations_ri_field, "Art 46 alinéa en général. Pour SCOOPS alinéa 2 de l’Art 209 Pour la COOP-CA Art 363 alinéa 4")
        row += 1
        self.modalite_status_field = IntLineEdit(self.rest_d(
            self.check_list.modalite_status))
        self.modalite_ri_field = IntLineEdit(self.rest_d(
            self.check_list.modalite_ri))
        self.add_element(mentions_gribox, row, "<b>16.</b> Les modalités de fonctionnement de la société coopérative ;",
                         self.modalite_status_field, self.modalite_ri_field, "Art 95 à 121 en général .Pour SCOOPS art 217 à 263 Pour la COOP-CA Art 291 à 368")
        row += 1
        self.signature_int_status_field = IntLineEdit(self.rest_d(
            self.check_list.signature_int_status))
        self.signature_int_ri_field = IntLineEdit(self.rest_d(
            self.check_list.signature_int_ri))
        self.add_element(mentions_gribox, row, "<b>17.</b> La signature des initiateurs ou l’apposition de leur empreinte digitale",
                         self.signature_int_status_field, self.signature_int_ri_field, "Point 17 de l’Art 18")
        row += 1
        self.etendue_status_field = IntLineEdit(self.rest_d(
            self.check_list.etendue_status))
        self.etendue_ri_field = IntLineEdit(self.rest_d(
            self.check_list.etendue_ri))
        self.add_element(mentions_gribox, row, "<b>18.</b> L’étendue des transactions avec les usagers non coopérateurs, tout en ayant en vue<br/>la sauvegarde de l’autonomie de la société coopérative ;",
                         self.etendue_status_field, self.etendue_ri_field, "Art 4 al. 2")
        row += 1
        qss = "padding:5px;padding-left:25px;padding-right:25px;background: gray;font-size:30px;color:#fff"
        mentions_gribox.addWidget(FHeader(
            "Les mentions facultatives", qss), row, 0, 1, 4)
        row += 1
        self.rendement_status_field = IntLineEdit(self.rest_d(
            self.check_list.rendement_status))
        self.rendement_ri_field = IntLineEdit(self.rest_d(
            self.check_list.rendement_ri))
        self.add_element(mentions_gribox, row, "<b>1. a.</b> Le taux de rendement maximal qui peut être appliqué aux prêts et aux épargnes des membres",
                         self.rendement_status_field, self.rendement_ri_field, "Art 18. 1bis alinéa 1")
        row += 1
        self.remuneration_status_field = IntLineEdit(self.rest_d(
            self.check_list.remuneration_status))
        self.remuneration_ri_field = IntLineEdit(self.rest_d(
            self.check_list.remuneration_ri))
        self.add_element(mentions_gribox, row, "<b>1. b.</b> Le taux de rémunération maximale qui peut être appliqué aux parts de membres ;",
                         self.remuneration_status_field, self.remuneration_ri_field, "Art 239 ; 240 alinéa4 et 231(Art 18. 1bis alinéa 1)")
        row += 1
        self.limite_imposee_status_field = IntLineEdit(self.rest_d(
            self.check_list.limite_imposee_status))
        self.limite_imposee_ri_field = IntLineEdit(self.rest_d(
            self.check_list.limite_imposee_ri))
        self.add_element(mentions_gribox, row, "<b>2.</b> Toute limite imposée aux activités commerciales de la société coopérative.",
                         self.limite_imposee_status_field, self.limite_imposee_ri_field, "COOP–CA Art 313,SCOOPS Art 258 et 259")
        row += 1
        mentions_gribox.addWidget(FHeader(
            "Règlement Intérieur, outre les mentions obligatoires des statuts, le règlement intérieur contient les prescriptions suivantes :", qss), row, 0, 1, 4)
        row += 1
        self.indemnit_status_field = IntLineEdit(self.rest_d(
            self.check_list.indemnit_status))
        self.indemnit_ri_field = IntLineEdit(self.rest_d(
            self.check_list.indemnit_ri))
        self.add_element(mentions_gribox, row, "<b>1.</b> Les conditions de paiement d’indemnités aux membres du conseil d’administration ou du comité<br/> de gestion, du conseil ou du comité de surveillance, définies dans le respect des dispositions<br/> des articles 225 et 305 ;",
                         self.indemnit_status_field, self.indemnit_ri_field, "Scoops : Art 225; Scoop-CA : Art 305")
        row += 1
        self.souscription_status_field = IntLineEdit(self.rest_d(
            self.check_list.souscription_status))
        self.souscription_ri_field = IntLineEdit(self.rest_d(
            self.check_list.souscription_ri))
        self.add_element(mentions_gribox, row, "<b>2.</b> La souscription de parts sociales supplémentaires et leur nombre par coopérateur ;",
                         self.souscription_status_field, self.souscription_ri_field, "Pour la SCOOPS Art 210 Réf aux statuts et ne peut excéder <br/>5 fois le montant des parts sociales souscrites) Pour la COOP-CA Art 371")
        row += 1
        self.suspension_status_field = IntLineEdit(self.rest_d(
            self.check_list.suspension_status))
        self.suspension_ri_field = IntLineEdit(self.rest_d(
            self.check_list.suspension_ri))
        self.add_element(mentions_gribox, row, "<b>3.</b> Les critères et conditions de suspension des coopérateurs;",
                         self.suspension_status_field, self.suspension_ri_field, "Statut (initiateurs)")
        row += 1
        self.attribution_status_field = IntLineEdit(self.rest_d(
            self.check_list.attribution_status))
        self.attribution_ri_field = IntLineEdit(self.rest_d(
            self.check_list.attribution_ri))
        self.add_element(mentions_gribox, row, "<b>4.</b> La possibilité d’attribution d’un droit de vote plural dans le cas des unions, des fédérations et<br/>des confédérations ;",
                         self.attribution_status_field, self.attribution_ri_field, "Art 138")
        row += 1
        self.prescriptions_status_field = IntLineEdit(self.rest_d(
            self.check_list.prescriptions_status))
        self.prescriptions_ri_field = IntLineEdit(self.rest_d(
            self.check_list.prescriptions_ri))
        self.add_element(mentions_gribox, row, "<b>5.</b> Toutes autres prescriptions jugées nécessaires pour la réalisation de l’objet de la société <br/>coopérative et conformes aux principes coopératifs et aux dispositions impératives du présent<br/> Acte uniforme.",
                         self.prescriptions_status_field, self.prescriptions_ri_field, "AUSCOOP")
        vbox = QVBoxLayout()
        vbox.addLayout(pieces_v_gribox)
        vbox.addLayout(pieces_gribox)
        vbox.addLayout(mentions_gribox)
        self.piecesGroupBox.setLayout(vbox)
        # Durée statutaire de la société coopérative
        duree_fbox = QFormLayout()
        self.butt_continous = Button_save(u"Continuer")
        self.butt_continous.clicked.connect(self.goto_immatriculation)
        self.butt_continous.setMaximumWidth(200)
        duree_fbox.addRow("", self.butt_continous)

        if not self.check_integrity_validation():
            self.butt_continous.setEnabled(False)

        scroll = QScrollArea(self)
        scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        scroll.setWidgetResizable(True)
        # scroll.setFixedHeight(200)
        vbox = QVBoxLayout()
        vbox.addWidget(FHeader(
            "<h2>Check-list de Contrôle de dossiers des sociétés coopératives avant l’immatriculation et l’enregistrement par le SLDS-ES</h2>", css="color:green"))
        vbox.addWidget(FHeader(
            "<h4>Société Coopérative : {} </h4>".format(self.dmd.scoop)))
        scroll.setWidget(self.piecesGroupBox)
        vbox.addWidget(scroll)
        vbox.addLayout(duree_fbox)
        self.setLayout(vbox)

    def to_int_or_none(self, value):
        try:
            return int(value)
        except:
            return None

    def rest_d(self, data):
        if data:
            return str(data)
        return ''

    def check_box(self, check_object):
        check_object.clicked.connect(self.save)
        return check_object

    def save(self):
        self.butt_continous.setEnabled(False)
        self.check_l = self.dmd.check_list
        self.check_l.qualite_declarant_check = self.qualite_declarant_check.isChecked()
        self.check_l.status_check = self.status_check.isChecked()
        self.check_l.pieces_check = self.pieces_check.isChecked()
        self.check_l.autorisation_pre_immt_check = self.autorisation_pre_immt_check.isChecked()
        self.check_l.demande_immt_check = self.demande_immt_check.isChecked()
        self.check_l.pv_check = self.pv_check.isChecked()
        self.check_l.chronologique_check = self.chronologique_check.isChecked()
        self.check_l.compte_check = self.compte_check.isChecked()
        self.check_l.dispositions_check = self.dispositions_check.isChecked()
        self.check_l.pv_delib_ca_check = self.pv_delib_ca_check.isChecked()
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
        self.check_l.duree_ri = self.to_int_or_none(
            self.duree_ri_field.text())
        self.check_l.lien_commun_status = self.to_int_or_none(
            self.lien_commun_status_field.text())
        self.check_l.lien_commun_ri = self.to_int_or_none(
            self.lien_commun_ri_field.text())
        self.check_l.coord_initiateur_status = self.to_int_or_none(
            self.coord_initiateur_status_field.text())
        self.check_l.coord_initiateur_ri = self.to_int_or_none(
            self.coord_initiateur_ri_field.text())
        self.check_l.max_min_admin_cg_status = self.to_int_or_none(
            self.max_min_admin_cg_status_field.text())
        self.check_l.max_min_admin_cg_ri = self.to_int_or_none(
            self.max_min_admin_cg_ri_field.text())
        self.check_l.max_min_admin_ca_status = self.to_int_or_none(
            self.max_min_admin_ca_status_field.text())
        self.check_l.max_min_admin_ca_ri = self.to_int_or_none(
            self.max_min_admin_ca_ri_field.text())
        self.check_l.dispositions_cg_status = self.to_int_or_none(
            self.dispositions_cg_status_field.text())
        self.check_l.dispositions_cg_ri = self.to_int_or_none(
            self.dispositions_cg_ri_field.text())
        self.check_l.dispositions_ca_status = self.to_int_or_none(
            self.dispositions_ca_status_field.text())
        self.check_l.dispositions_ca_ri = self.to_int_or_none(
            self.dispositions_ca_ri_field.text())
        self.check_l.max_min_cs_s_status = self.to_int_or_none(
            self.max_min_cs_s_status_field.text())
        self.check_l.max_min_cs_s_ri = self.to_int_or_none(
            self.max_min_cs_s_ri_field.text())
        self.check_l.max_min_cs_ca_status = self.to_int_or_none(
            self.max_min_cs_ca_status_field.text())
        self.check_l.max_min_cs_ca_ri = self.to_int_or_none(
            self.max_min_cs_ca_ri_field.text())
        self.check_l.dispositions_mo_status = self.to_int_or_none(
            self.dispositions_mo_status_field.text())
        self.check_l.dispositions_mo_ri = self.to_int_or_none(
            self.dispositions_mo_ri_field.text())
        self.check_l.mandat_cs_status = self.to_int_or_none(
            self.mandat_cs_status_field.text())
        self.check_l.mandat_cs_ri = self.to_int_or_none(
            self.mandat_cs_ri_field.text())
        self.check_l.parts_sociales_status = self.to_int_or_none(
            self.parts_sociales_status_field.text())
        self.check_l.parts_sociales_ri = self.to_int_or_none(
            self.parts_sociales_ri_field.text())
        self.check_l.declatation_status = self.to_int_or_none(
            self.declatation_status_field.text())
        self.check_l.declatation_ri = self.to_int_or_none(
            self.declatation_ri_field.text())
        self.check_l.id_apport_numeraire_status = self.to_int_or_none(
            self.id_apport_numeraire_status_field.text())
        self.check_l.id_apport_numeraire_ri = self.to_int_or_none(
            self.id_apport_numeraire_ri_field.text())
        self.check_l.id_apport_nature_status = self.to_int_or_none(
            self.id_apport_nature_status_field.text())
        self.check_l.id_apport_nature_ri = self.to_int_or_none(
            self.id_apport_nature_ri_field.text())
        self.check_l.evaluation_apport_status = self.to_int_or_none(
            self.evaluation_apport_status_field.text())
        self.check_l.evaluation_apport_ri = self.to_int_or_none(
            self.evaluation_apport_ri_field.text())
        self.check_l.capital_social_status = self.to_int_or_none(
            self.capital_social_status_field.text())
        self.check_l.capital_social_ri = self.to_int_or_none(
            self.capital_social_ri_field.text())
        self.check_l.valeur_nominale_status = self.to_int_or_none(
            self.valeur_nominale_status_field.text())
        self.check_l.valeur_nominale_ri = self.to_int_or_none(
            self.valeur_nominale_ri_field.text())
        self.check_l.stipulations_status = self.to_int_or_none(
            self.stipulations_status_field.text())
        self.check_l.stipulations_ri = self.to_int_or_none(
            self.stipulations_ri_field.text())
        self.check_l.modalite_status = self.to_int_or_none(
            self.modalite_status_field.text())
        self.check_l.modalite_ri = self.to_int_or_none(
            self.modalite_ri_field.text())
        self.check_l.signature_int_status = self.to_int_or_none(
            self.signature_int_status_field.text())
        self.check_l.signature_int_ri = self.to_int_or_none(
            self.signature_int_ri_field.text())
        self.check_l.etendue_status = self.to_int_or_none(
            self.etendue_status_field.text())
        self.check_l.etendue_ri = self.to_int_or_none(
            self.etendue_ri_field.text())
        self.check_l.rendement_status = self.to_int_or_none(
            self.rendement_status_field.text())
        self.check_l.rendement_ri = self.to_int_or_none(
            self.rendement_ri_field.text())
        self.check_l.remuneration_status = self.to_int_or_none(
            self.remuneration_status_field.text())
        self.check_l.remuneration_ri = self.to_int_or_none(
            self.remuneration_ri_field.text())
        self.check_l.limite_imposee_status = self.to_int_or_none(
            self.limite_imposee_status_field.text())
        self.check_l.limite_imposee_ri = self.to_int_or_none(
            self.limite_imposee_ri_field.text())
        self.check_l.indemnit_status = self.to_int_or_none(
            self.indemnit_status_field.text())
        self.check_l.indemnit_ri = self.to_int_or_none(
            self.indemnit_ri_field.text())
        self.check_l.souscription_status = self.to_int_or_none(
            self.souscription_status_field.text())
        self.check_l.souscription_ri = self.to_int_or_none(
            self.souscription_ri_field.text())
        self.check_l.suspension_status = self.to_int_or_none(
            self.suspension_status_field.text())
        self.check_l.suspension_ri = self.to_int_or_none(
            self.suspension_ri_field.text())
        self.check_l.attribution_status = self.to_int_or_none(
            self.attribution_status_field.text())
        self.check_l.attribution_ri = self.to_int_or_none(
            self.attribution_ri_field.text())
        self.check_l.prescriptions_status = self.to_int_or_none(
            self.prescriptions_status_field.text())
        self.check_l.prescriptions_ri = self.to_int_or_none(
            self.prescriptions_ri_field.text())
        self.check_l.save()
        if self.check_integrity_validation():
            self.butt_continous.setEnabled(True)

    def check_integrity_validation(self):
        return (self.qualite_declarant_check.isChecked() and
                self.status_check.isChecked() and
                self.pieces_check.isChecked() and
                self.autorisation_pre_immt_check.isChecked() and
                self.demande_immt_check.isChecked() and
                self.pv_check.isChecked() and
                self.chronologique_check.isChecked() and
                self.compte_check.isChecked() and
                self.dispositions_check.isChecked() and
                self.pv_delib_ca_check.isChecked() and
                not check_is_empty(self.forme_scoop_status_field) and
                not check_is_empty(self.forme_scoop_ri_field) and
                not check_is_empty(self.denomination_status_field) and
                not check_is_empty(self.denomination_ri_field) and
                not check_is_empty(self.nature_domaine_status_field) and
                not check_is_empty(self.nature_domaine_ri_field) and
                not check_is_empty(self.duree_status_field) and
                not check_is_empty(self.duree_ri_field) and
                not check_is_empty(self.lien_commun_status_field) and
                not check_is_empty(self.lien_commun_ri_field) and
                not check_is_empty(self.coord_initiateur_status_field) and
                not check_is_empty(self.coord_initiateur_ri_field) and
                not check_is_empty(self.max_min_admin_cg_status_field) and
                not check_is_empty(self.max_min_admin_cg_ri_field) and
                not check_is_empty(self.max_min_admin_ca_status_field) and
                not check_is_empty(self.max_min_admin_ca_ri_field) and
                not check_is_empty(self.dispositions_cg_status_field) and
                not check_is_empty(self.dispositions_cg_ri_field) and
                not check_is_empty(self.dispositions_ca_status_field) and
                not check_is_empty(self.dispositions_ca_ri_field) and
                not check_is_empty(self.max_min_cs_s_status_field) and
                not check_is_empty(self.max_min_cs_s_ri_field) and
                not check_is_empty(self.max_min_cs_ca_status_field) and
                not check_is_empty(self.max_min_cs_ca_ri_field) and
                not check_is_empty(self.dispositions_mo_status_field) and
                not check_is_empty(self.dispositions_mo_ri_field) and
                not check_is_empty(self.mandat_cs_status_field) and
                not check_is_empty(self.mandat_cs_ri_field) and
                not check_is_empty(self.parts_sociales_status_field) and
                not check_is_empty(self.parts_sociales_ri_field) and
                not check_is_empty(self.declatation_status_field) and
                not check_is_empty(self.declatation_ri_field) and
                not check_is_empty(self.id_apport_nature_status_field) and
                not check_is_empty(self.id_apport_nature_ri_field) and
                not check_is_empty(self.evaluation_apport_status_field) and
                not check_is_empty(self.evaluation_apport_ri_field) and
                not check_is_empty(self.capital_social_status_field) and
                not check_is_empty(self.capital_social_ri_field) and
                not check_is_empty(self.valeur_nominale_status_field) and
                not check_is_empty(self.valeur_nominale_ri_field) and
                not check_is_empty(self.stipulations_status_field) and
                not check_is_empty(self.stipulations_ri_field) and
                not check_is_empty(self.modalite_status_field) and
                not check_is_empty(self.modalite_ri_field) and
                not check_is_empty(self.signature_int_status_field) and
                not check_is_empty(self.signature_int_ri_field) and
                not check_is_empty(self.etendue_status_field) and
                not check_is_empty(self.etendue_ri_field) and
                not check_is_empty(self.rendement_status_field) and
                not check_is_empty(self.rendement_ri_field) and
                not check_is_empty(self.remuneration_status_field) and
                not check_is_empty(self.remuneration_ri_field) and
                not check_is_empty(self.limite_imposee_status_field) and
                not check_is_empty(self.limite_imposee_ri_field) and
                not check_is_empty(self.indemnit_status_field) and
                not check_is_empty(self.indemnit_ri_field) and
                not check_is_empty(self.souscription_status_field) and
                not check_is_empty(self.souscription_ri_field) and
                not check_is_empty(self.suspension_status_field) and
                not check_is_empty(self.suspension_ri_field) and
                not check_is_empty(self.attribution_status_field) and
                not check_is_empty(self.attribution_ri_field) and
                not check_is_empty(self.prescriptions_status_field) and
                not check_is_empty(self.prescriptions_ri_field))

    def add_element(self, objet_, row, text, field1, field2, helper=None):
        field1.textChanged.connect(self.save)
        field2.textChanged.connect(self.save)
        objet_.addWidget(FHeader("{}".format(text)), row, 0)
        objet_.addWidget(field1, row, 1)
        objet_.addWidget(field2, row, 2)
        if helper:
            objet_.addWidget(FHeader(helper, css="font-size: 15px;"), row, 3)

    def goto_immatriculation(self):
        self.dmd.status = Demande.IMMATRICULAITON
        self.dmd.save()
        from ui.immatriculation import ImmatriculationSCoopViewWidget
        self.change_main_context(
            ImmatriculationSCoopViewWidget, table_p=self, dmd=self.dmd)
