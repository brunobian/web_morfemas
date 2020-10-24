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
    sufijo   = tmp[3].strip()
    numero   = tmp[2].strip()
    sufijada = tmp[5].strip()
    frec     = tmp[4].strip()
    
    db_text.append((id, palabra, sufijo, numero, sufijada, frec))
    i = i+1

cur.execute('DROP TABLE morfemas_palabra ;')
cur.execute('CREATE TABLE morfemas_palabra (id serial NOT NULL PRIMARY KEY, col1 VARCHAR (10000), col2 VARCHAR (100000 ), col3 VARCHAR ( 100000 ), col4 VARCHAR ( 1000000 ), col5 VARCHAR ( 1000000 ), col6 VARCHAR ( 1000000 ));')
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
    count_afijada       = float(tmp[4])
    count_pseudoafijada = float(tmp[5])
    prop_frec_afij      = float(tmp[6])
    prop_count_afij     = float(tmp[7])
    
    db_text.append((id, Sufijo, Numero, frec_afijada, frec_pseudoafijada, count_afijada, count_pseudoafijada, prop_frec_afij, prop_count_afij))
    i = i+1


#cur.execute('DROP TABLE morfemas_sufijo ;')
cur.execute('CREATE TABLE morfemas_sufijo (id serial NOT NULL PRIMARY KEY, col1 VARCHAR (10000), col2 VARCHAR (100000 ), col3 VARCHAR ( 100000 ), col4 VARCHAR ( 1000000 ), col5 VARCHAR ( 1000000 ), col6 VARCHAR ( 1000000 ), col7 VARCHAR ( 1000000 ), col8 VARCHAR ( 1000000 ), col9 VARCHAR ( 1000000 ));')
cur.executemany('INSERT INTO morfemas_sufijo  VALUES VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)',db_text)
conn.commit()
f.close()
cur = conn.cursor()

cur.executemany('INSERT INTO morfemas_sufijo  VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)',db_text)
conn.commit()
f.close()
cur = conn.cursor()
