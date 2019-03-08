# !/usr/bin/env python
# -*- coding: utf-8 -*-
import datetime as dt
now = dt.datetime.now()
print(now)
d1 = dt.datetime.strptime('2022-02-22 16:30:30', '%Y-%m-%d %H:%M:%S')
d2 = dt.datetime.strptime('2025-01-23 15:30:30', '%Y-%m-%d %H:%M:%S')
print(d1)
print(d2)
delta = d2 - d1
print(delta.days)
print(delta)


