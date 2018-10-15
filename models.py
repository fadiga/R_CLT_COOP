#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# vim: ai ts=4 sts=4 et sw=4 nu
# maintainer: Fadiga

from __future__ import (
    unicode_literals, absolute_import, division, print_function)

from datetime import datetime

from peewee import (DateTimeField, CharField, IntegerField, FloatField,
                    BooleanField, ForeignKeyField, TextField)

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


class CooperativeCompanies(BaseModel):
    name = CharField(unique=True, verbose_name=("Nom"))

    def __str__(self):
        return self.name
