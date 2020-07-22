#!/usr/bin/env python3

import psycopg2
import io

database='morfemas'
host='localhost'
user='brunobian'
password='tusam.vive'
connectStr="dbname='"+database+"' user='"+user+"' host='"+host+"' password='"+password+"'"
drop_talbes = 1

conn = psycopg2.connect(connectStr)
cur = conn.cursor()

# Armo tabla palabras
f = io.open('por_palabras.csv', encoding='latin-1')
db_text = []
i = 0
for l in f.readlines()[1:]:
    id = i
    palabra = l.split(',',2)
    sufijo =  l.split(',',0)
    numero =  l.split(',',1)
    sufijada =  l.split(',',3)
    
    db_text.append((id, palabra, sufijo, numero, sufijada))
    i = i+1

for i in db_text:
	print(i[0])
cur.executemany('INSERT INTO morfemas_palabra  VALUES (%s,%s,%s,%s,%s)',db_text)
conn.commit()
f.close()
cur = conn.cursor()

# Armo tabla sufijo
f = io.open('por_sufijos.csv', encoding='latin-1')
db_text = []
i = 0
for l in f.readlines()[1:]:
    id = i
    tmp = l.split(',')
    Sufijo              = tmp[0]
    Numero              = tmp[1]
    frec_afijada        = float(tmp[2])
    frec_pseudoafijada  = float(tmp[3])
    count_afijada       = float(tmp[4])
    count_pseudoafijada = float(tmp[5])
    prop_count_afij     = float(tmp[6])
    
    db_text.append((id, Sufijo, Numero, frec_afijada, frec_pseudoafijada, count_afijada, count_pseudoafijada, prop_count_afij))
    i = i+1

for i in db_text:
	print(i[0])
cur.executemany('INSERT INTO morfemas_sufijo  VALUES (%s,%s,%s,%s,%s,%s,%s,%s)',db_text)
conn.commit()
f.close()
cur = conn.cursor()
