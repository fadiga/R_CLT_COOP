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


class Settings(BaseModel):

    slug_region = CharField(verbose_name=("Code region"))
    slug_cercle = CharField(verbose_name=("Code cercle"))

    def region_name(self):
        return get_entity_name(self.slug_region)

    def cercle_name(self):
        return get_entity_name(self.slug_cercle)

    def __str__(self):
        return "{} > {}".format(self.region_name(), self.cercle_name())


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


class CooperativeCompanie(BaseModel):

    region = CharField(null=True)
    cercle = CharField(null=True)
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
        return get_entity_name(self.region)

    def display_cercle(self):
        return get_entity_name(self.cercle)

    def display_commune(self):
        return get_entity_name(self.commune)

    def display_vfq(self):
        return get_entity_name(self.vfq)


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
            year=self.date.year, cercle_code=get_imm_code(
                self.scoop.cercle), incr=self.incr(), forme=self.get_forme_code())
        # print(ident)
        return ident

    def incr(self):
        return self.add("0000", str(self.scoop.id))

    def add(self, x, y):
        r = str(int(x) + int(y)).zfill(len(x))
        return r

    def get_forme_code(self):
        print(self.scoop.forme)
        return "A" if self.scoop.forme == "a" else "B"

    def display_quality(self):
        return get_qualities().get(self.quality)

    def save_ident(self):
        self.save()
        self.scoop.immatricule = self.create_ident()
        self.scoop.created = True
        self.scoop.end_date = self.date
        self.scoop.save()


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

    def __str__(self):
        return self.full_name

    def display_poste(self):
        return get_postes().get(self.poste)

    def display_sex(self):
        return self.SEX.get(self.sex)
