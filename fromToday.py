#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import re
from datetime import datetime
from dateutil.relativedelta import *
#from dateutil.relativedelta import relativedelta

EXC_INT = Exception("Date interpretation")

def input(s):
    m = re.match(r'(\d+) d', s)
    if m:
        dateAdd = relativedelta(days=int(m.group(1)))
    m = re.match(r'(\d+) y', s)
    if m:
        dateAdd = relativedelta(years=int(m.group(1)))
    m = re.match(r'^tod', s)
    if m:
        dateAdd = relativedelta(days=0)
    m = re.match(r'^tom', s)
    if m:
        dateAdd = relativedelta(days=1)

    # Weekdays
    m = re.match(r'^mon', s)
    if m:
        dateAdd = relativedelta(weekday=MO)
    m = re.match(r'^tue', s)
    if m:
        dateAdd = relativedelta(weekday=TU)
    m = re.match(r'^wed', s)
    if m:
        dateAdd = relativedelta(weekday=WE)
    m = re.match(r'^thu', s)
    if m:
        dateAdd = relativedelta(weekday=TH)
    m = re.match(r'^fri', s)
    if m:
        dateAdd = relativedelta(weekday=FR)
    m = re.match(r'^sat', s)
    if m:
        dateAdd = relativedelta(weekday=SA)
    m = re.match(r'^sun', s)
    if m:
        dateAdd = relativedelta(weekday=SU)

    # Next Weekdays
    m = re.match(r'^next ', s)
    if m: 
        dateAdd = relativedelta(days=7)
        m = re.match(r'mon', s)
        if m:
            dateAdd += relativedelta(weekday=MO)
        m = re.match(r'tue', s)
        if m:
            dateAdd = relativedelta(weekday=TU)
        m = re.match(r'wed', s)
        if m:
            dateAdd = relativedelta(weekday=WE)
        m = re.match(r'thu', s)
        if m:
            dateAdd = relativedelta(weekday=TH)
        m = re.match(r'fri', s)
        if m:
            dateAdd = relativedelta(weekday=FR)
        m = re.match(r'sat', s)
        if m:
            dateAdd = relativedelta(weekday=SA)
        m = re.match(r'sun', s)
        if m:
            dateAdd = relativedelta(weekday=SU)
        else:
            raise EXC_INT

    # 
    print datetime.today()+dateAdd



input(sys.argv[1])
