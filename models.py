#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# vim: ai ts=4 sts=4 et sw=4 nu
# maintainer: Fadiga

from __future__ import (
    unicode_literals, absolute_import, division, print_function)

from datetime import datetime

from peewee import (DateTimeField, DateField, CharField, TextField,
                    IntegerField, FloatField, BooleanField, ForeignKeyField)

from Common.models import BaseModel

FDATE = u"%c"
NOW = datetime.now()


class Spinneret(BaseModel):
    name = CharField(unique=True, verbose_name=("Nom"))

    def __str__(self):
        return self.name


class Activity(BaseModel):
    name = CharField(unique=True, verbose_name=("Nom"))

    def __str__(self):
        return self.name


class CheckList(BaseModel):

    qualite_declarant = CharField()
    statuts = BooleanField(default=False)
    reglement_interieur = BooleanField(default=False)
    pv = BooleanField(default=False)
    demande_d_immatriculation = BooleanField(default=False)
    autorisations_preealables = BooleanField(default=False)
    is_existe_register_mb = BooleanField(default=False)
    is_existe_bank_account = BooleanField(default=False)
    no_plurality_mandates = BooleanField(default=False)
    is_existe_registre_pv = BooleanField(default=False)
    forme_scoop_status = IntegerField(null=True)
    forme_scoop_ri = IntegerField(null=True)
    denomination_status = IntegerField(null=True)
    denomination_ri = IntegerField(null=True)
    nature_domaine_status = IntegerField(null=True)
    nature_domaine_ri = IntegerField(null=True)
    duree_status = IntegerField(null=True)
    duree_ri = IntegerField(null=True)

    def __str__(self):
        return "{}/{}".format(self.qualite_declarant, self.forme_scoop_status)


class Immatriculation(BaseModel):

    identifiant = CharField()
    sex = CharField()
    full_name = CharField(verbose_name="Nom complet")
    position = CharField(verbose_name="Qualité")
    commune = CharField(null=True)
    quartier = CharField(null=True)
    rue = IntegerField(null=True)
    porte = IntegerField(null=True)
    bp = IntegerField(null=True)
    tel = IntegerField(null=True)
    email = CharField(null=True)
    # META
    is_syncro = BooleanField(default=False)

    def __str__(self):
        return "{}{}".format(self.identifiant, self.full_name)

    def create_ident(self):
        return "2015T2D1/0002B"


class CooperativeCompanie(BaseModel):

    duree_statutaire = IntegerField(null=True)
    vfq = CharField(null=True)
    commune = CharField(null=True)
    quartier = CharField(null=True)
    rue = IntegerField(null=True)
    porte = IntegerField(null=True)
    bp = IntegerField(null=True)
    tel = IntegerField(null=True)
    email = CharField(null=True)
    denomination = CharField(null=True)
    commercial_name = CharField(null=True)
    created_year = IntegerField(null=True)
    forme = CharField(null=True)
    activite = CharField(null=True)
    apports_amount = IntegerField(null=True)
    apports_nature = IntegerField(null=True)
    apports_industrie = IntegerField(null=True)
    created = BooleanField(default=False)
    immatriculation = ForeignKeyField(Immatriculation, null=True)

    # META
    is_syncro = BooleanField(default=False)
    start_date = DateTimeField(default=NOW)
    end_date = DateTimeField(null=True)

    def __str__(self):
        return self.denomination

    def membres(self):
        return CooperativeMember.select().where(CooperativeMember.scoop == self)


class Demande(BaseModel):

    declaration = 1
    add_member = 2
    check_list = 3
    immatriculation = 4
    end_procces = 5

    STATUS = {
        declaration: "Déclaration",
        add_member: "Ajout membre",
        check_list: "Vérification",
        immatriculation: "Immatriculation",
        end_procces: "end_procces",
    }

    declaration_date = DateField()
    check_list = ForeignKeyField(CheckList, null=True)
    scoop = ForeignKeyField(CooperativeCompanie, null=True)

    # META
    is_syncro = BooleanField(default=False)
    start_date = DateTimeField(default=NOW)
    status = CharField(default=declaration)
    end_date = DateTimeField(null=True)

    def __str__(self):
        return self.scoop.denomination


class CooperativeMember(BaseModel):
    """
    """
    PR = "a"
    SE = "b"
    MB = "bv"
    POSTE = {
        PR: ("President"),
        SE: ("Secrétaire"),
        MB: ("Membre"),
    }
    M = "M"
    F = "F"
    SEX = {
        M: "Homme",
        F: "Femme"
    }

    scoop = ForeignKeyField(CooperativeCompanie)
    full_name = CharField()
    sex = CharField()
    ddn = DateField()
    addres = CharField()
    nationality = CharField()
    phone = IntegerField()
    poste = CharField()
    add_date = DateField(default=NOW)

    def __str__(self):
        return self.full_name
