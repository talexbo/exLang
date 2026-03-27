#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 21 18:27:40 2026

@author: alex
"""
import datetime, bday_messages
today = datetime.date(2026,3,21)
next_birthday = datetime.date(2026,5,13)
time_difference =  next_birthday - today
if time_difference == 0:
    print(bday_m)
else:
    print(f"My next birthday is {time_difference} days away!")
