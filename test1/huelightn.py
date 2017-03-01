from threading import Thread
import sqlite3 as lite
import sys
import os.path
import requests
import json
from time import sleep
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setup(16, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(18, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(15, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(13, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)



Bulbs = 6
DbUpdateSleep = 0.05
ButtonSleep = 0.3
DimButtonSleep = 0.3


L1ID = 1
L1ON = Lamp[0]['on']
L1BRI = Lamp[0]['bri']
L1BRI = int(L1BRI)
L1 = "1/state"

L2ID = 2
L2ON = Lamp[1]['on']
L2BRI = Lamp[1]['bri']
L2BRI = int(L2BRI)
L2 = "2/state"

L3ID = 3
L3ON = Lamp[2]['on']
L3BRI = Lamp[2]['bri']
L3BRI = int(L3BRI)
L3 = "3/state"

L4ID = 4
L4ON = Lamp[3]['on']
L4BRI = Lamp[3]['bri']
L4BRI = int(L4BRI)
L4 = "4/state"

L5ID = 5
L5ON = Lamp[4]['on']
L5BRI = Lamp[4]['bri']
L5BRI = int(L5BRI)
L5 = "5/state"

L6ID = 6
L6ON = Lamp[5]['on']
L6BRI = Lamp[5]['bri']
L6BRI = int(L6BRI)
L6 = "6/state"

scene1 = {"bri":175, "ct":447, "sat":200, "hue":13544}
scene2 = {"bri":175, "ct":346, "sat":121, "hue":15324}
scene3 = {"bri":175, "ct":233, "sat":251, "hue":34075}
scene4 = {"bri":175, "ct":156, "sat":55, "hue":33042}



def createnewdb():
	CheckIfDbExists = os.path.isfile("LightStateDB.db")
	if CheckIfDbExists:
		os.remove("LightStateDB.db")
		print "Old DB Deleted"
	
	
	con = lite.connect('LightStateDB.db')
	with con:
		cur = con.cursor()
		cur.execute("CREATE TABLE Lights(Id INT, Name TEXT, Lampon INT, Bri INT, Hue INT, Sat INT, Ct INT)")
		MakeDbCount = 0
		BulpID = 1
		while MakeDbCount < Bulbs:
			MakeDbCount += 1
			cur.execute("INSERT INTO Lights VALUES(?,?,?,?,?,?,?);",(BulpID, 'Bulp', 1, 1, 1, 1, 1))
			BulpID += 1
	print "New DB Created"


def updatedb():
	print 'DB update running..'
	con = lite.connect('LightStateDB.db')
	while True:
		ALL = requests.get('http://192.168.0.100/api/9QzpiSZhWWsY3PoRxpfvGAKCkTxhWcluhac54pBP/lights')
		ALL = ALL.json()
		sleep (DbUpdateSleep)

		#       Light 1
		L1ID = 1
		L1NAME = ALL['1']['name']
		L1ON = ALL['1']['state']['on']
		L1BRI = ALL['1']['state']['bri']
		L1HUE = ALL['1']['state']['hue']
		L1SAT = ALL['1']['state']['sat']
		L1XY = ALL['1']['state']['xy']
		L1CT = ALL['1']['state']['ct']
		
		#       Light 2
		L2ID = 2
		L2NAME = ALL['2']['name']
		L2ON = ALL['2']['state']['on']
		L2BRI = ALL['2']['state']['bri']
		L2HUE = ALL['2']['state']['hue']
		L2SAT = ALL['2']['state']['sat']
		L2XY = ALL['2']['state']['xy']
		L2CT = ALL['2']['state']['ct']

		#       Light 3
		L3ID = 3
		L3NAME = ALL['3']['name']
		L3ON = ALL['3']['state']['on']
		L3BRI = ALL['3']['state']['bri']
		L3HUE = ALL['3']['state']['hue']
		L3SAT = ALL['3']['state']['sat']
		L3XY = ALL['3']['state']['xy']
		L3CT = ALL['3']['state']['ct']

		#       Light 4
		L4ID = 4
		L4NAME = ALL['4']['name']
		L4ON = ALL['4']['state']['on']
		L4BRI = ALL['4']['state']['bri']
		L4HUE = ALL['4']['state']['hue']
		L4SAT = ALL['4']['state']['sat']
		L4XY = ALL['4']['state']['xy']
		L4CT = ALL['4']['state']['ct']

		#       Light 5
		L5ID = 5
		L5NAME = ALL['5']['name']
		L5ON = ALL['5']['state']['on']
		L5BRI = ALL['5']['state']['bri']
		L5CT = ALL['5']['state']['ct']

		#       Light 6
		L6ID = 6
		L6NAME = ALL['6']['name']
		L6ON = ALL['6']['state']['on']
		L6BRI = ALL['6']['state']['bri']

		#       Set Values in DB
		with con:
			cur = con.cursor()
			cur.execute("UPDATE Lights SET Lampon=?,Bri=?,Hue=?,Sat=?,Ct=? WHERE Id=?;",(L1ON, L1BRI, L1HUE, L1SAT, L1CT, L1ID))
			cur.execute("UPDATE Lights SET Lampon=?,Bri=?,Hue=?,Sat=?,Ct=? WHERE Id=?;",(L2ON, L2BRI, L2HUE, L2SAT, L2CT, L2ID))
			cur.execute("UPDATE Lights SET Lampon=?,Bri=?,Hue=?,Sat=?,Ct=? WHERE Id=?;",(L3ON, L3BRI, L3HUE, L3SAT, L3CT, L3ID))
			cur.execute("UPDATE Lights SET Lampon=?,Bri=?,Hue=?,Sat=?,Ct=? WHERE Id=?;",(L4ON, L4BRI, L4HUE, L4SAT, L4CT, L4ID))
			cur.execute("UPDATE Lights SET Lampon=?,Bri=?,Ct=? WHERE Id=?;",(L5ON, L5BRI, L5CT, L5ID))
			cur.execute("UPDATE Lights SET Lampon=?,Bri=? WHERE Id=?;",(L6ON, L6BRI, L6ID))

def mainfunc():
	print 'Program running..'
	url = "http://192.168.0.100/api/9QzpiSZhWWsY3PoRxpfvGAKCkTxhWcluhac54pBP/lights/"
	con = lite.connect('LightStateDB.db')
	Counter = 0
	while True:
		Lamp = []
		with con:
			cur = con.cursor()
			cur.execute("SELECT Lampon, Bri FROM Lights;")
			row = cur.fetchone()
			while row is not None:
				Lamp.append({'on': row[0], 'bri': row[1]})
				row = cur.fetchone()
"""
		L1ID = 1
		L1ON = Lamp[0]['on']
		L1BRI = Lamp[0]['bri']
		L1BRI = int(L1BRI)
		L1 = "1/state"
		
		L2ID = 2
		L2ON = Lamp[1]['on']
		L2BRI = Lamp[1]['bri']
		L2BRI = int(L2BRI)
		L2 = "2/state"

		L3ID = 3
		L3ON = Lamp[2]['on']
		L3BRI = Lamp[2]['bri']
		L3BRI = int(L3BRI)
		L3 = "3/state"

		L4ID = 4
		L4ON = Lamp[3]['on']
		L4BRI = Lamp[3]['bri']
		L4BRI = int(L4BRI)
		L4 = "4/state"

		L5ID = 5
		L5ON = Lamp[4]['on']
		L5BRI = Lamp[4]['bri']
		L5BRI = int(L5BRI)
		L5 = "5/state"

		L6ID = 6
		L6ON = Lamp[5]['on']
		L6BRI = Lamp[5]['bri']
		L6BRI = int(L6BRI)
		L6 = "6/state"

		scene1 = {"bri":175, "ct":447, "sat":200, "hue":13544}
		scene2 = {"bri":175, "ct":346, "sat":121, "hue":15324}
		scene3 = {"bri":175, "ct":233, "sat":251, "hue":34075}
		scene4 = {"bri":175, "ct":156, "sat":55, "hue":33042} """
		def lightup( LID, LON, LBRI, L ):
			if LBRI < 229 and LON == 1:
				LBRI += 25
				bri_up = {"on":True, "bri":LBRI}
				u = requests.put(url + L, json.dumps(bri_up), timeout=5)
				with con:
					cur = con.cursor()
					cur.execute("UPDATE Lights SET Bri=? WHERE Id=?;",(LBRI, LID))

			elif LBRI > 228 and LON == 1:
				bri = 254
				bri_up = {"bri":bri}
				u = requests.put(url + L, json.dumps(bri_up), timeout=5)
				with con:
					cur = con.cursor()
					cur.execute("UPDATE Lights SET Bri=? WHERE Id=?;",(bri, LID))
		
		def lightdown( LID, LON, LBRI, L ):
			if LBRI > 24 and LON == 1:
				LBRI -= 25
				bri_down = {"on":True, "bri":LBRI}
				u = requests.put(url + L, json.dumps(bri_down), timeout=5)
				with con:
					cur = con.cursor()
					cur.execute("UPDATE Lights SET Bri=? WHERE Id=?;",(LBRI, LID))

			elif LBRI < 25 and LON == 1:
				bri = 0
				bri_down = {"on":True, "bri":bri}
				u = requests.put(url + L, json.dumps(bri_down), timeout=5)
				with con:
					cur = con.cursor()
					cur.execute("UPDATE Lights SET Lampon=?, Bri=? WHERE Id=?;",("True", bri, LID))

		def lighton( LID, LON, L, SCE ):
			if LON == 0:
				on = {"on":True}
				u = requests.put(url + L, json.dumps(on), timeout=5)
				with con:
					cur = con.cursor()
					cur.execute("UPDATE Lights SET Lampon=? WHERE Id=?;",("True", LID))

			elif LON == 1:
				u = requests.put(url + L, json.dumps(SCE), timeout=5)

		def lightoff( LID, LON, L ):
			if LON == 1:
				on = {"on":False}
				u = requests.put(url + L, json.dumps(on), timeout=5)
				with con:
					cur = con.cursor()
					cur.execute("UPDATE Lights SET Lampon=? WHERE Id=?;",("False", LID))


					########## Afbryder Sovevrelse	 ##########
						##### Afbryder Knap Op #####
		if (GPIO.input(13) == 1):
			bri_up1 = lightup( L1ID, L1ON, L1BRI, L1 )
			bri_up2 = lightup( L2ID, L2ON, L2BRI, L2 )
			bri_up3 = lightup( L3ID, L3ON, L3BRI, L3 )
			bri_up5 = lightup( L5ID, L5ON, L5BRI, L5 )
			sleep(DimButtonSleep)

		if (GPIO.input(15) == 1):
			bri_down1 = lightdown( L1ID, L1ON, L1BRI, L1 )
			bri_down2 = lightdown( L2ID, L2ON, L2BRI, L2 )
			bri_down3 = lightdown( L3ID, L3ON, L3BRI, L3 )
			bri_down5 = lightdown( L5ID, L5ON, L5BRI, L5 )
			sleep(DimButtonSleep)

		if (GPIO.input(16) == 1):
			Counter += 1
			if Counter == 1:
				light_on1 = lighton( L1ID, L1ON, L1, scene1 )
				light_on2 = lighton( L2ID, L2ON, L2, scene1 )
				light_on3 = lighton( L3ID, L3ON, L3, scene1 )
				light_on5 = lighton( L5ID, L5ON, L5, scene1 )
			elif Counter == 2:
				light_on1 = lighton( L1ID, L1ON, L1, scene2 )
				light_on2 = lighton( L2ID, L2ON, L2, scene2 )
				light_on3 = lighton( L3ID, L3ON, L3, scene2 )
				light_on5 = lighton( L5ID, L5ON, L5, scene2 )
			elif Counter == 3:
				light_on1 = lighton( L1ID, L1ON, L1, scene3 )
				light_on2 = lighton( L2ID, L2ON, L2, scene3 )
				light_on3 = lighton( L3ID, L3ON, L3, scene3 )
				light_on5 = lighton( L5ID, L5ON, L5, scene3 )
			elif Counter == 4:
				light_on1 = lighton( L1ID, L1ON, L1, scene4 )
				light_on2 = lighton( L2ID, L2ON, L2, scene4 )
				light_on3 = lighton( L3ID, L3ON, L3, scene4 )
				light_on5 = lighton( L5ID, L5ON, L5, scene4 )
				Counter = 0
			sleep(ButtonSleep)

		if (GPIO.input(18) == 1):
			light_off1 = lightoff( L1ID, L1ON, L1 )
			light_off2 = lightoff( L2ID, L2ON, L2 )
			light_off3 = lightoff( L3ID, L3ON, L3 )
			light_off5 = lightoff( L5ID, L5ON, L5 )
			sleep(ButtonSleep)

createnewdb()
if __name__ == '__main__':
	Thread(target = updatedb).start()
	Thread(target = mainfunc).start()
