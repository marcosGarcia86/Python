#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import csv, sys, os, codecs
'''
arquivo = csv.reader(open('arquivo.csv', 'r'))
for linha in arquivo:
    print (linha)

'''
#with open('PE.pdf', 'r') as f:
with open('arquivo.csv', 'r', encoding='utf-8') as f:
    r = csv.reader(f)
    for linha in r:
        print (linha[0])
