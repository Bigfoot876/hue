#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3 as lite
import sys

con = lite.connect('test.db')

cur = con.cursor()
cur.execute('''
	CREATE TABLE Lamps(
	   Id		INT PRIMARY KEY NOT NULL,
	   name		textNOT NULL,
	   lampon	INT NOT NULL,
	   bri	INT NOT NULL,
	   hue	INT
 	);
	''')

cur.execute("INSERT INTO Lamps VALUES(1,'Lampe1', 0, 10, 20);")
cur.execute("INSERT INTO Lamps VALUES(2,'Lampe2', 0, 10, 20);")
	
cur.execute("SELECT * FROM Lamps;")

rows = cur.fetchall()

print '[Id, Name, lampon, bri, hue]'

for l in rows:
    print list(l)

print 'Updating Lampe1...'
cur.execute("UPDATE Lamps set lampon=1,bri=1000,hue=2000 where name='Lampe1';")

cur.execute("SELECT * FROM Lamps;")

rows = cur.fetchall()

print '[Id, Name, lampon, bri, hue]'

for l in rows:
    print list(l)

cur.execute("drop table Lamps;")
