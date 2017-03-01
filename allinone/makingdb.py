import sqlite3 as lite
import sys
import os.path


CheckIfDbExists = os.path.isfile("LightStateDB.db")
if CheckIfDbExists:
	os.remove('LightStateDB.db')

elif CheckIfDbExists == False:

	con = lite.connect('LightStateDB.db')

	Counter = 0
	Bulbs = 6

	L1ID = 1
	L1NAME = 'Name1'
	L1ON = 1
	L1BRI = 150
	L1HUE = 9000
	L1SAT = 225
	L1CT = 224

	with con:
		cur = con.cursor()
		cur.execute("CREATE TABLE Lights(Id INT, Name TEXT, Lampon INT, Bri INT, Hue INT, Sat INT, Ct INT)")
		while Counter < Bulbs:
			Counter += 1
			cur.execute("INSERT INTO Lights VALUES(?,?,?,?,?,?,?);",(L1ID, L1NAME, L1ON, L1BRI, L1HUE, L1SAT, L1CT))
			L1ID += 1
		
