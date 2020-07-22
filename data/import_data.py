#!/usr/bin/env python3

import psycopg2
import io

database='morfemas'
host='localhost'
user='brunobian'
password='tusam.vive'
connectStr="dbname='"+database+"' user='"+user+"' host='"+host+"' password='"+password+"'"

conn = psycopg2.connect(connectStr)
cur = conn.cursor()

cur.execute('INSERT INTO morfemas_text  VALUES (%s,%s,%s,%s)',db_text)


f = io.open('textos.csv', encoding='latin-1')
db_text = []
for l in f.readlines():
    sl = l.split(',',3)
    id = int(sl[0])
    textnum = int(sl[1])
    textclass = int(sl[2])
    #text = unicode(sl[3][0:-1],'iso-8859-15')
    text = sl[3][0:-1]
    #print id, textnum, textclass, text
    
    db_text.append((id,textnum,textclass,text))

for i in db_text:
	print(i[0])
cur.executemany('INSERT INTO morfemas_text  VALUES (%s,%s,%s,%s)',db_text)
conn.commit()
f.close()
cur = conn.cursor()
