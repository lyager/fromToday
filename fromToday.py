#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import re
from datetime import datetime
from dateutil.relativedelta import *
#from dateutil.relativedelta import relativedelta

EXC_INT = Exception("Date interpretation")

class Usage(Exception):
    def __init__(self, msg):
        self.msg = msg

def _dateAdd(s, reldate):
    m = re.match(r'(\d+) d', s)
    if m:
        return reldate+relativedelta(days=int(m.group(1)))
    m = re.match(r'(\d+) y', s)
    if m:
        return reldate+relativedelta(years=int(m.group(1)))
    m = re.match(r'^tod', s)
    if m:
        return reldate+relativedelta(days=0)
    m = re.match(r'^tom', s)
    if m:
        return reldate+relativedelta(days=1)

    # Weekdays
    m = re.match(r'^mon', s)
    if m:
        return reldate+relativedelta(weekday=MO)
    m = re.match(r'^tue', s)
    if m:
        return reldate+relativedelta(weekday=TU)
    m = re.match(r'^wed', s)
    if m:
        return reldate+relativedelta(weekday=WE)
    m = re.match(r'^thu', s)
    if m:
        return reldate+relativedelta(weekday=TH)
    m = re.match(r'^fri', s)
    if m:
        return reldate+relativedelta(weekday=FR)
    m = re.match(r'^sat', s)
    if m:
        return reldate+relativedelta(weekday=SA)
    m = re.match(r'^sun', s)
    if m:
        return reldate+relativedelta(weekday=SU)

    # Next Weekdays
    m = re.match(r'^next (.+)', s)
    if m: 
        dateAdd = reldate+relativedelta(days=7)
        return _dateAdd(m.group(1), dateAdd)

def input(s):

    #print datetime.today()+_dateAdd(s)
    print _dateAdd(s, datetime.today())


def main(argv=None):
    if argv == None:
        argv = sys.argv
    try:
        input(argv[1])
    except Exception, msg:
        print "Missing argument."

if __name__ == "__main__":
    sys.exit(main())


