#!/usr/bin/env python
# -*- coding: utf-8 -*-
# maintainer: fadiga

# from PyQt4.QtGui import QStatusBar
from PyQt4.QtCore import QThread, SIGNAL, QObject, Qt
import json
# import os
import requests
# import threading
# import time
from configuration import Config

from models import (CooperativeCompanie, Demande,
                    Office, CheckList, CooperativeMember, Immatriculation)
# from Common.ui.statusbar import GStatusBar

base_url = Config.BASE_URL


class UpdaterInit(QObject):

    def __init__(self):
        QObject.__init__(self)

        if not Config.SERV:
            print("Not Serveur ")
            return

        self.check = TaskThreadServer(self)
        self.connect(self.check, SIGNAL('setStatus'),
                     self.update_data, Qt.QueuedConnection)
        self.check.start()

    def end_update_data(self):
        n = 0
        while n != 100000:
            n += 1
            print("{} Lapin".format(n))

    def update_data(self):
        print("update_data")

        if Office().select().count() == 0:
            return

        office = Office().select().where(Office.id == 1).get()
        if not office.is_syncro:
            resp = self.sender("add-office", office.data())
            if resp.get("save"):
                office.updated()

        for model in [CooperativeCompanie, CooperativeMember, CheckList, Demande, Immatriculation]:
            for m in model.all():
                print(m)
                if not m.is_syncro:
                    resp = self.sender("update-data", m.data())
                    if resp.get("save"):
                        m.updated()

        self.emit(SIGNAL("end_update_data"))

    def sender(self, url, data):
        url = base_url + "scoop/" + url
        print(data)
        client = requests.session()
        response = client.get(url, data=json.dumps(data))
        print("response : ", response)
        try:
            return json.loads(response.content.decode('UTF-8'))
        except ValueError:
            return False


class TaskThreadServer(QThread):

    def __init__(self, parent):
        QThread.__init__(self, parent)
        self.parent = parent

    def run(self):
        print("RUN")
        self.parent.update_data()

        import threading
        threading.Timer(5.0, self.parent.update_data).start()
