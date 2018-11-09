#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Autor: Fadiga

from __future__ import (unicode_literals, absolute_import, division,
                        print_function)

import os
import sys
sys.path.append(os.path.abspath('../'))

from Common.fixture import AdminFixture
from models import Activity, Spinneret


class FixtInit(AdminFixture):

    """docstring for FixtInit"""

    def __init__(self):
        super(AdminFixture, self).__init__()

        self.LIST_CREAT.append(
            Activity(slug="agriculture_et_peche", name=u"Agriculture et pêche"))
        self.LIST_CREAT.append(
            Activity(slug="matieres_premieres_energies", name=u"Matières premières et énergies"))
        self.LIST_CREAT.append(Activity(slug="industrie", name=u"Industrie"))
        self.LIST_CREAT.append(Activity(slug="tourisme", name=u"Tourisme"))
        self.LIST_CREAT.append(
            Activity(slug="politique_economique", name=u"Politique économique"))
        self.LIST_CREAT.append(
            Spinneret(activity=Activity.get(Activity.slug == "agriculture_et_peche"),
                      slug="cereales", name=u"Céréales"))
        self.LIST_CREAT.append(
            Spinneret(activity=Activity.get(Activity.slug == "agriculture_et_peche"),
                      slug="coton", name=u"Coton"))
        self.LIST_CREAT.append(
            Spinneret(activity=Activity.get(Activity.slug == "agriculture_et_peche"),
                      slug="elevage", name=u"Élevage"))
        self.LIST_CREAT.append(
            Spinneret(activity=Activity.get(Activity.slug == "agriculture_et_peche"),
                      slug="peche_et_pisciculture", name=u"Pêche et pisciculture"))
        self.LIST_CREAT.append(
            Spinneret(activity=Activity.get(Activity.slug == "matieres_premieres_energies"),
                      slug="or", name=u"Or"))
