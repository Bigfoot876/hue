import sqlite3 as lite
import sys

con = lite.connect('test.db')

L1ID = 1
L1NAME = 'Name1'
L1ON = 1
L1BRI = 150
L1HUE = 9000
L1SAT = 225
L1CT = 224


L2ID = 2
L2NAME = 'Name2'
L2ON = 1
L2BRI = 150
L2HUE = 9000
L2SAT = 225
L2CT = 224

L3ID = 3
L3NAME = 'Name3'
L3ON = 1
L3BRI = 150
L3HUE = 9000
L3SAT = 225
L3CT = 224

L4ID = 4
L4NAME = 'Name4'
L4ON = 1
L4BRI = 150
L4HUE = 9000
L4SAT = 225
L4CT = 224

L5ID = 5
L5NAME = 'Name5'
L5ON = 1
L5BRI = 150
L5HUE = 9000
L5SAT = 225
L5CT = 224

L6ID = 6
L6NAME = 'Name6'
L6ON = 1
L6BRI = 150
L6HUE = 9000
L6SAT = 225
L6CT = 224





with con:
	cur = con.cursor()
	cur.execute("CREATE TABLE Lights(Id INT, Name TEXT, Lampon INT, Bri INT, Hue INT, Sat INT, Ct INT)")
	cur.execute("INSERT INTO Lights VALUES(?,?,?,?,?,?,?);",(L1ID, L1NAME, L1ON, L1BRI, L1HUE, L1SAT, L1CT))
	cur.execute("INSERT INTO Lights VALUES(?,?,?,?,?,?,?)",(L2ID, L2NAME, L2ON, L2BRI, L2HUE, L2SAT, L2CT))
	cur.execute("INSERT INTO Lights VALUES(?,?,?,?,?,?,?)",(L3ID, L3NAME, L3ON, L3BRI, L3HUE, L3SAT, L3CT))
	cur.execute("INSERT INTO Lights VALUES(?,?,?,?,?,?,?)",(L4ID, L4NAME, L4ON, L4BRI, L4HUE, L4SAT, L4CT))
	cur.execute("INSERT INTO Lights VALUES(?,?,?,?,?)",(L5ID, L5NAME, L5ON, L5BRI, L5CT))
	cur.execute("INSERT INTO Lights VALUES(?,?,?,?)",(L6ID, L6NAME, L6ON, L6BRI))

