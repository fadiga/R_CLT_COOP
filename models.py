#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# vim: ai ts=4 sts=4 et sw=4 nu
# maintainer: Fadiga

from __future__ import (
    unicode_literals, absolute_import, division, print_function)

from datetime import datetime

from peewee import (DateTimeField, DateField, CharField,
                    IntegerField, BooleanField, ForeignKeyField)
from data_helper import (get_entity_name, get_postes, get_formes, get_qualities,
                         get_activities, get_spinneret_activites, get_imm_code)
from Common.models import BaseModel

FDATE = u"%c"
NOW = datetime.now()


class Office(BaseModel):

    slug_region = CharField(verbose_name=("Code region"))
    slug_cercle = CharField(verbose_name=("Code cercle"))
    slug = CharField(verbose_name=("Code"))
    phone = CharField(verbose_name=("Code"), null=True)
    email_org = CharField(verbose_name=("Code"), null=True)
    bp = CharField(verbose_name=("Code"), null=True)
    adress_org = CharField(verbose_name=("Code"), null=True)

    def region_name(self):
        return get_entity_name(self.slug_region)

    def cercle_name(self):
        return get_entity_name(self.slug_cercle)

    def __str__(self):
        return "{} - {} / {}".format(
            self.slug, self.region_name(), self.cercle_name())

    def data(self):
        return {
            "slug": self.slug
        }


class CheckList(BaseModel):

    date = DateTimeField(default=NOW)
    qualite_declarant_check = BooleanField(default=False)
    status_check = BooleanField(default=False)
    pieces_check = BooleanField(default=False)
    autorisation_pre_immt_check = BooleanField(default=False)
    demande_immt_check = BooleanField(default=False)
    pv_check = BooleanField(default=False)
    chronologique_check = BooleanField(default=False)
    compte_check = BooleanField(default=False)
    dispositions_check = BooleanField(default=False)
    pv_delib_ca_check = BooleanField(default=False)
    forme_scoop_status = IntegerField(null=True)
    forme_scoop_ri = IntegerField(null=True)
    denomination_status = IntegerField(null=True)
    denomination_ri = IntegerField(null=True)
    nature_domaine_status = IntegerField(null=True)
    nature_domaine_ri = IntegerField(null=True)
    duree_status = IntegerField(null=True)
    duree_ri = IntegerField(null=True)
    lien_commun_status = IntegerField(null=True)
    lien_commun_ri = IntegerField(null=True)
    coord_initiateur_status = IntegerField(null=True)
    coord_initiateur_ri = IntegerField(null=True)
    max_min_admin_cg_status = IntegerField(null=True)
    max_min_admin_cg_ri = IntegerField(null=True)
    max_min_admin_ca_status = IntegerField(null=True)
    max_min_admin_ca_ri = IntegerField(null=True)
    dispositions_cg_status = IntegerField(null=True)
    dispositions_cg_ri = IntegerField(null=True)
    dispositions_ca_status = IntegerField(null=True)
    dispositions_ca_ri = IntegerField(null=True)
    max_min_cs_s_status = IntegerField(null=True)
    max_min_cs_s_ri = IntegerField(null=True)
    max_min_cs_ca_status = IntegerField(null=True)
    max_min_cs_ca_ri = IntegerField(null=True)
    dispositions_mo_status = IntegerField(null=True)
    dispositions_mo_ri = IntegerField(null=True)
    mandat_cs_status = IntegerField(null=True)
    mandat_cs_ri = IntegerField(null=True)
    parts_sociales_status = IntegerField(null=True)
    parts_sociales_ri = IntegerField(null=True)
    declatation_status = IntegerField(null=True)
    declatation_ri = IntegerField(null=True)
    id_apport_numeraire_status = IntegerField(null=True)
    id_apport_numeraire_ri = IntegerField(null=True)
    id_apport_nature_status = IntegerField(null=True)
    id_apport_nature_ri = IntegerField(null=True)
    evaluation_apport_status = IntegerField(null=True)
    evaluation_apport_ri = IntegerField(null=True)
    capital_social_status = IntegerField(null=True)
    capital_social_ri = IntegerField(null=True)
    valeur_nominale_status = IntegerField(null=True)
    valeur_nominale_ri = IntegerField(null=True)
    stipulations_status = IntegerField(null=True)
    stipulations_ri = IntegerField(null=True)
    modalite_status = IntegerField(null=True)
    modalite_ri = IntegerField(null=True)
    signature_int_status = IntegerField(null=True)
    signature_int_ri = IntegerField(null=True)
    etendue_status = IntegerField(null=True)
    etendue_ri = IntegerField(null=True)
    rendement_status = IntegerField(null=True)
    rendement_ri = IntegerField(null=True)
    remuneration_status = IntegerField(null=True)
    remuneration_ri = IntegerField(null=True)
    limite_imposee_status = IntegerField(null=True)
    limite_imposee_ri = IntegerField(null=True)
    indemnit_status = IntegerField(null=True)
    indemnit_ri = IntegerField(null=True)
    souscription_status = IntegerField(null=True)
    souscription_ri = IntegerField(null=True)
    suspension_status = IntegerField(null=True)
    suspension_ri = IntegerField(null=True)
    attribution_status = IntegerField(null=True)
    attribution_ri = IntegerField(null=True)
    prescriptions_status = IntegerField(null=True)
    prescriptions_ri = IntegerField(null=True)
    # META
    is_syncro = BooleanField(default=False)
    last_update_date = DateTimeField(null=True)

    def __str__(self):
        return "{}/{}".format(self.qualite_declarant_check, self.forme_scoop_status)

    def data(self):
        return {
            "date": self.date,
            "qualite_declarant_check": self.qualite_declarant_check,
            "status_check": self.status_check,
            "pieces_check": self.pieces_check,
            "autorisation_pre_immt_check": self.autorisation_pre_immt_check,
            "demande_immt_check": self.demande_immt_check,
            "pv_check": self.pv_check,
            "chronologique_check": self.chronologique_check,
            "compte_check": self.compte_check,
            "dispositions_check": self.dispositions_check,
            "pv_delib_ca_check": self.pv_delib_ca_check,
            "forme_scoop_status": self.forme_scoop_status,
            "forme_scoop_ri": self.forme_scoop_ri,
            "denomination_status": self.denomination_status,
            "denomination_ri": self.denomination_ri,
            "nature_domaine_status": self.nature_domaine_status,
            "nature_domaine_ri": self.nature_domaine_ri,
            "duree_status": self.duree_status,
            "duree_ri": self.duree_ri,
            "lien_commun_status": self.lien_commun_status,
            "lien_commun_ri": self.lien_commun_ri,
            "coord_initiateur_status": self.coord_initiateur_status,
            "coord_initiateur_ri": self.coord_initiateur_ri,
            "max_min_admin_cg_status": self.max_min_admin_cg_status,
            "max_min_admin_cg_ri": self.max_min_admin_cg_ri,
            "max_min_admin_ca_status": self.max_min_admin_ca_status,
            "max_min_admin_ca_ri": self.max_min_admin_ca_ri,
            "dispositions_cg_status": self.dispositions_cg_status,
            "dispositions_cg_ri": self.dispositions_cg_ri,
            "dispositions_ca_status": self.dispositions_ca_status,
            "dispositions_ca_ri": self.dispositions_ca_ri,
            "max_min_cs_s_status": self.max_min_cs_s_status,
            "max_min_cs_s_ri": self.max_min_cs_s_ri,
            "max_min_cs_ca_status": self.max_min_cs_ca_status,
            "max_min_cs_ca_ri": self.max_min_cs_ca_ri,
            "dispositions_mo_status": self.dispositions_mo_status,
            "dispositions_mo_ri": self.dispositions_mo_ri,
            "mandat_cs_status": self.mandat_cs_status,
            "mandat_cs_ri": self.mandat_cs_ri,
            "parts_sociales_status": self.parts_sociales_status,
            "parts_sociales_ri": self.parts_sociales_ri,
            "declatation_status": self.declatation_status,
            "declatation_ri": self.declatation_ri,
            "id_apport_numeraire_status": self.id_apport_numeraire_status,
            "id_apport_numeraire_ri": self.id_apport_numeraire_ri,
            "id_apport_nature_status": self.id_apport_nature_status,
            "id_apport_nature_ri": self.id_apport_nature_ri,
            "evaluation_apport_status": self.evaluation_apport_status,
            "evaluation_apport_ri": self.evaluation_apport_ri,
            "capital_social_status": self.capital_social_status,
            "capital_social_ri": self.capital_social_ri,
            "valeur_nominale_status": self.valeur_nominale_status,
            "valeur_nominale_ri": self.valeur_nominale_ri,
            "stipulations_status": self.stipulations_status,
            "stipulations_ri": self.stipulations_ri,
            "modalite_status": self.modalite_status,
            "modalite_ri": self.modalite_ri,
            "signature_int_status": self.signature_int_status,
            "signature_int_ri": self.signature_int_ri,
            "etendue_status": self.etendue_status,
            "etendue_ri": self.etendue_ri,
            "rendement_status": self.rendement_status,
            "rendement_ri": self.rendement_ri,
            "remuneration_status": self.remuneration_status,
            "remuneration_ri": self.remuneration_ri,
            "limite_imposee_status": self.limite_imposee_status,
            "limite_imposee_ri": self.limite_imposee_ri,
            "indemnit_status": self.indemnit_status,
            "indemnit_ri": self.indemnit_ri,
            "souscription_status": self.souscription_status,
            "souscription_ri": self.souscription_ri,
            "suspension_status": self.suspension_status,
            "suspension_ri": self.suspension_ri,
            "attribution_status": self.attribution_status,
            "attribution_ri": self.attribution_ri,
            "prescriptions_status": self.prescriptions_status,
            "prescriptions_ri": self.prescriptions_ri,
        }


class CooperativeCompanie(BaseModel):

    office = ForeignKeyField(Office)
    commune = CharField(null=True)
    vfq = CharField(null=True)
    rue = IntegerField(null=True)
    porte = IntegerField(null=True)
    bp = IntegerField(null=True)
    tel = IntegerField(null=True)
    email = CharField(null=True)
    denomination = CharField(null=True)
    commercial_name = CharField(null=True)
    created_year = IntegerField(null=True)
    forme = CharField()
    activity = CharField(null=True)
    spinneret = CharField(null=True)
    apports_numeraire = IntegerField(null=True)
    apports_nature = IntegerField(null=True)
    apports_industrie = IntegerField(null=True)
    created = BooleanField(default=False)
    immatricule = CharField(null=True)
    duree_statutaire = IntegerField(null=True)

    # META
    is_syncro = BooleanField(default=False)
    last_update_date = DateTimeField(null=True)
    start_date = DateTimeField(default=NOW)
    end_date = DateTimeField(null=True)

    def __str__(self):
        return self.denomination

    def membres(self):
        return CooperativeMember.select().where(CooperativeMember.scoop == self)

    def demande(self):
        return Demande.select().where(Demande.scoop == self).get()

    def display_forme(self):
        return get_formes().get(self.forme)

    def display_activity(self):
        return get_activities().get(self.activity)

    def display_spinneret(self):
        return get_spinneret_activites(self.activity).get(self.spinneret)

    def display_region(self):
        return get_entity_name(self.office.slug_region)

    def display_cercle(self):
        return get_entity_name(self.office.slug_cercle)

    def display_commune(self):
        return get_entity_name(self.commune)

    def display_vfq(self):
        return get_entity_name(self.vfq)

    def data(self):

        return {
            "office": self.office.slug,
            "commune": self.commune,
            "vfq": self.vfq,
            "rue": self.rue,
            "porte": self.porte,
            "bp": self.bp,
            "tel": self.tel,
            "email": self.email,
            "denomination": self.denomination,
            "commercial_name": self.commercial_name,
            "created_year": self.created_year,
            "forme": self.forme,
            "activity": self.activity,
            "spinneret": self.spinneret,
            "apports_numeraire": self.apports_numeraire,
            "apports_nature": self.apports_nature,
            "apports_industrie": self.apports_industrie,
            "created": self.created,
            "immatricule": self.immatricule,
            "duree_statutaire": self.duree_statutaire,
        }


class Immatriculation(BaseModel):

    TP = "tiers_avec_procuration"

    scoop = ForeignKeyField(CooperativeCompanie)
    name_declarant = CharField(verbose_name="Nom complet")
    quality = CharField(verbose_name="Qualité")
    date = DateField(default=NOW)
    procuration = CharField(verbose_name="Qualité")
    # META
    is_syncro = BooleanField(default=False)
    last_update_date = DateTimeField(null=True)

    def __str__(self):
        return "{}{}".format(self.identifiant, self.full_name)

    def create_ident(self):
        ident = "R-{year}-{cercle_code}/{incr}/{forme}".format(
            year=self.date.year, cercle_code=self.scoop.office.slug,
            incr=self.incr(), forme=self.get_forme_code())
        # print(ident)
        return ident

    def incr(self):
        return self.add("0000", str(self.scoop.id))

    def add(self, x, y):
        r = str(int(x) + int(y)).zfill(len(x))
        return r

    def get_forme_code(self):
        return "A" if self.scoop.forme == "a" else "B"

    def display_quality(self):
        return get_qualities().get(self.quality)

    def save_ident(self):
        self.save()
        self.scoop.immatricule = self.create_ident()
        self.scoop.created = True
        self.scoop.end_date = self.date
        self.scoop.save()

    def data(self):
        return {
            "scoop": self.scoop,
            "name_declarant": self.name_declarant,
            "quality": self.quality,
            "date": self.date,
            "procuration": self.procuration,
        }


class Demande(BaseModel):

    DECLARATION = 1
    ADDMEMBER = 2
    CHECKLIST = 3
    IMMATRICULAITON = 4
    ENDPROCCES = 5

    STATUS = {
        DECLARATION: "Déclaration",
        ADDMEMBER: "Ajout membre",
        CHECKLIST: "Vérification",
        IMMATRICULAITON: "Immatriculation",
        ENDPROCCES: "end_procces",
    }

    declaration_date = DateField()
    check_list = ForeignKeyField(CheckList, null=True)
    scoop = ForeignKeyField(CooperativeCompanie, null=True)
    # META
    is_syncro = BooleanField(default=False)
    last_update_date = DateTimeField(null=True)
    start_date = DateTimeField(default=NOW)
    status = CharField(default=DECLARATION)
    end_date = DateTimeField(null=True)

    def display_status(self):
        return self.STATUS.get(self.status)

    def __str__(self):
        return self.scoop.denomination

    def data(self):
        return {
            "declaration_date": self.declaration_date,
            "check_list": self.check_list,
            "scoop": self.scoop,
            "is_syncro": self.is_syncro,
            "last_update_date": self.last_update_date,
            "start_date": self.start_date,
            "status": self.status,
            "end_date": self.end_date,
        }


class CooperativeMember(BaseModel):
    """
    """

    M = "M"
    F = "F"
    SEX = {
        M: "Homme",
        F: "Femme"
    }

    scoop = ForeignKeyField(CooperativeCompanie)
    full_name = CharField()
    sex = CharField(null=True)
    ddn = DateField(null=True)
    addres = CharField(null=True)
    nationality = CharField(null=True)
    phone = IntegerField(null=True)
    poste = CharField(null=True)
    add_date = DateField(default=NOW)
    # META
    # is_syncro = BooleanField(default=False)
    # last_update_date = DateTimeField(null=True)

    def __str__(self):
        return self.full_name

    def display_poste(self):
        return get_postes().get(self.poste)

    def display_sex(self):
        return self.SEX.get(self.sex)

    def data(self):
        return {
            "scoop": self.scoop,
            "full_name": self.full_name,
            "sex": self.sex,
            "ddn": self.ddn,
            "addres": self.addres,
            "nationality": self.nationality,
            "phone": self.phone,
            "poste": self.poste,
            "add_date": self.add_date,
            "is_syncro": self.is_syncro,
            "last_update_date": self.last_update_date
        }
