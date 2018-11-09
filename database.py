#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# vim: ai ts=4 sts=4 et sw=4 nu
# maintainer: Fad
from __future__ import (unicode_literals, absolute_import, division,
                        print_function)

from models import (Spinneret, Activity, CooperativeMember,
                    CooperativeCompanie, CheckList, Demande, Cercle, Commune, VFQ)

from Common.cdatabase import AdminDatabase


class Setup(AdminDatabase):

    """docstring for FixtInit"""

    def __init__(self):
        super(AdminDatabase, self).__init__()
        for md in [Spinneret, Activity, CooperativeMember, Cercle, Commune, VFQ,
                   CooperativeCompanie, Demande, CheckList]:
            self.LIST_CREAT.append(md)
