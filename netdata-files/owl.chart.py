# -*- coding: utf-8 -*-
# Description: display data from owl energy monitor
# Author: gbilder

from __future__ import print_function
import os
import random
from base import SimpleService
#import sqlite3


OWL_FN = '/tmp/eagle-owl-live.txt'
def get_latest():
    a =[]
    with open(OWL_FN) as f:
        line = f.read()
        a = line.split("\t")

    return a

NAME = os.path.basename(__file__).replace(".chart.py", "")
# default module values
#update_every = 4
priority = 90000
retries = 60


class Service(SimpleService):
    def __init__(self, configuration=None, name=None):
        super(self.__class__,self).__init__(configuration=configuration, name=name)

    def check(self):
        return True
    
    def create(self):
        self.chart("owl.python", '', 'OWL energy monitor', 'watts',
                   'KW', 'wattsB', 'line', self.priority, self.update_every)
        self.dimension('watts')
        self.commit()
        return True
    
    def update(self, interval):
        self.begin("owl.python", interval)
        r = get_latest()
        kw = float(r[4])
        self.set("watts", kw)
        self.end()
        self.commit()
        return True
