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
f = io.open('por_palabras.csv', encoding='utf-8')
db_text = []
i = 0
for l in f.readlines()[1:]:
    id = i
    tmp = l.split(',')
    print(tmp)
    palabra  = tmp[1].strip()
    numero   = tmp[2].strip()
    sufijo   = tmp[3].strip()
    frec     = tmp[4].strip()
    sufijada = tmp[5].strip()
    
    
    db_text.append((id, palabra, sufijo, numero, sufijada, frec))
    i = i+1

cur.executemany('INSERT INTO morfemas_palabra  VALUES (%s,%s,%s,%s,%s,%s)',db_text)
conn.commit()
f.close()
cur = conn.cursor()
		

# Armo tabla sufijo
f = io.open('por_sufijos.csv', encoding='utf-8')
db_text = []
i = 0
for l in f.readlines()[1:]:
    id = i
    tmp = l.split(',')
    print(tmp)
    Sufijo              = tmp[0].strip()
    Numero              = tmp[1].strip()
    frec_afijada        = float(tmp[2])
    frec_pseudoafijada  = float(tmp[3])
    prop_frec_afij      = float(tmp[4])    
    count_afijada       = float(tmp[5])
    count_pseudoafijada = float(tmp[6])
    prop_count_afij     = float(tmp[7])
    familia             = float(tmp[8])

    
    db_text.append((id, Sufijo, Numero, frec_afijada, frec_pseudoafijada, count_afijada, count_pseudoafijada, prop_frec_afij, prop_count_afij, familia))
    i = i+1


cur.executemany('INSERT INTO morfemas_sufijo  VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',db_text)
conn.commit()
f.close()
cur = conn.cursor()


















