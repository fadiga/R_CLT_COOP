#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# vim: ai ts=4 sts=4 et sw=4 nu
# maintainer: Fad
from __future__ import (
    unicode_literals, absolute_import, division, print_function)
import os
# from datetime import datetime
from PyQt4.QtGui import (QVBoxLayout)
try:
    from PyQt4.QtWebKit import QWebView
except:
    pass
# from PyQt4.QtCore import QUrl
from jinja2 import Environment, FileSystemLoader

from Common.tabpane import tabbox
from Common.ui.common import FWidget, FPageTitle, FBoxTitle, FMainWindow
# from Common.ui.table import FTableWidget
# from Common.ui.util import (show_date, formatted_number, date_on_or_end)

from models import CooperativeCompanie
# from configuration import Config


ROOT_DIR = os.path.dirname(os.path.abspath('__file__'))
# BASE_URL = 'file://' + ROOT_DIR


class DashbordViewWidget(FWidget):

    """ Shows the home page  """

    def __init__(self, parent=0, *args, **kwargs):
        super(DashbordViewWidget, self).__init__(
            parent=parent, *args, **kwargs)

        self.parentWidget().set_window_title("TABLEAU DE BORD")

        self.parent = parent
        vbox = QVBoxLayout()
        # self.resize(self.wc, self.hc)
        self.title = FPageTitle("TABLEAU DE BORD")

        self.title_alert = FBoxTitle(u"Les alertes")
        jinja = Environment(loader=FileSystemLoader('static'))
        template = jinja.get_template('chart.html')

        cc_list = CooperativeCompanie.select().order_by('-start_date')
        dataset = {
            "wc": self.width(),
            "hc": self.height(),
            "toal_scoop": cc_list.count(),
            "sc_coop_ca": cc_list.where(CooperativeCompanie.forme == "b").count(),
            "sc_scoops": cc_list.where(CooperativeCompanie.forme == "a").count(),
            "union": cc_list.where(CooperativeCompanie.forme == "bv").count(),
            "federation": cc_list.where(CooperativeCompanie.forme == "bf").count(),
            "confederation": cc_list.where(CooperativeCompanie.forme == "bc").count(),
        }

        graph1 = template.render(base_url=ROOT_DIR, data=dataset)

        template2 = jinja.get_template('table.html')
        table_html = template2.render(base_url=ROOT_DIR, dataset=dataset)

        web_graphic = QWebView()
        web_graphic.setHtml(graph1)
        tab_graphic = QVBoxLayout()
        # tab_graphic.setMargin(20)
        tab_graphic.addWidget(web_graphic)

        web_table = QWebView()
        web_table.setHtml(table_html)
        tab_table = QVBoxLayout()
        tab_table.addWidget(web_table)

        tab_widget = tabbox((tab_graphic, u"Graphique"), (tab_table, u"Tableau"))
        # tab_widget1 = tabbox((tab_table, u"Tableau"))

        vbox.addWidget(self.title)
        vbox.addWidget(tab_widget)
        # vbox.addWidget(tab_widget1)
        self.setLayout(vbox)
