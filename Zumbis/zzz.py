import csv, sys, os, codecs, random
lista=[]
with open('arquivos.csv', 'r', encoding='iso-8859-1') as f:
    r = csv.reader(f.readlines())
    for linha in r:
        print (linha)
