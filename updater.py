#!/usr/bin/env python
# -*- coding: utf-8 -*-
# maintainer: fadiga

# from PyQt4.QtGui import QStatusBar
from PyQt4.QtCore import QThread, SIGNAL, QObject, Qt
import json
# import os
import requests
from threading import Timer, Thread, Event
# import time
from configuration import Config

from models import (CooperativeCompanie, Demande,
                    Office, CheckList, CooperativeMember, Immatriculation)
# from Common.ui.statusbar import GStatusBar
from Common.ui.util import internet_on

base_url = Config.BASE_URL


class UpdaterInit(QObject):

    def __init__(self):
        QObject.__init__(self)

        if not Config.SERV:
            print("Not Serveur ")
            return
        self.stopFlag = Event()
        self.check = TaskThreadServer(self)
        self.connect(self.check, SIGNAL('UpdaterInit'),
                     self.update_data, Qt.QueuedConnection)
        self.check.start()

    def end_update_data(self):
        n = 0
        while n != 100000:
            n += 1
            print("{} Lapin".format(n))

    def update_data(self):
        print("update_data")

        if not internet_on(base_url):
            print("Pas de d'internet !")
            return

        if Office().select().count() == 0:
            return

        office = Office().select().where(Office.id == 1).get()
        if not office.is_syncro:
            resp = self.sender("add-office", office.data())
            if resp.get("save"):
                office.updated()

        for model in [CooperativeCompanie, CooperativeMember, CheckList, Demande, Immatriculation]:
            # print("sending :", model)
            for m in model.all():
                if not m.is_syncro:
                    print(m.data())
                    resp = self.sender("update-data", m.data())
                    # print(resp)
                    if resp.get("save"):
                        m.updated()

        # self.emit(SIGNAL("UpdaterInit"))

    def sender(self, url, data):
        client = requests.session()
        url = base_url + "scoop/" + url
        response = client.get(url, data=json.dumps(data))
        # print("response : ", response)
        try:
            return json.loads(response.content.decode('UTF-8'))
        except ValueError:
            return False


class TaskThreadServer(QThread):

    def __init__(self, parent):
        QThread.__init__(self, parent)
        self.parent = parent
        self.stopped = parent.stopFlag

    def run(self):
        print("RUN")
        while not self.stopped.wait(10):
            self.parent.update_data()
