import sqlite3 as lite
import sys

con = lite.connect('test.db')

L1ID = 1
L1NAME = 'SkabTest'
L1ON = 1
L1BRI = 150
L1HUE = 9000
L1SAT = 225
L1CT = 224

L2ID = 2
L2NAME =









with con:
	cur = con.cursor()
	cur.execute("CREATE TABLE Lights(Id INT, Name TEXT, Lampon INT, Bri INT, Hue INT, Sat INT, Ct INT)")
	cur.execute("INSERT INTO Lights VALUES(?,?,?,?,?,?,?);",(L1ID, L1NAME, L1ON, L1BRI, L1HUE, L1SAT, L1CT))
	cur.execute("INSERT INTO Lights VALUES(?,?,?,?,?,?,?)",(L2ID, L2NAME, L2ON, L2BRI, L2HUE, L2SAT, L2CT))
	cur.execute("INSERT INTO Lights VALUES(?,?,?,?,?,?,?)",(L3ID, L3NAME, L3ON, L3BRI, L3HUE, L3SAT, L3CT))
	cur.execute("INSERT INTO Lights VALUES(?,?,?,?,?,?,?)",(L4ID, L4NAME, L4ON, L4BRI, L4HUE, L4SAT, L4CT))
	cur.execute("INSERT INTO Lights VALUES(?,?,?,?,?)",(L5ID, L5NAME, L5ON, L5BRI, L5CT))
	cur.execute("INSERT INTO Lights VALUES(?,?,?,?)",(L6ID, L6NAME, L6ON, L6BRI))

