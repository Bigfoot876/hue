#!/usr/bin/python
from threading import Thread
import sqlite3 as lite
import sys
import os.path
import requests
import json
from time import sleep
import RPi.GPIO as GPIO

HueKey = "9QzpiSZhWWsY3PoRxpfvGAKCkTxhWcluhac54pBP"
HueIp = "192.168.0.100"
Bulbs = 6
DbUpdateSleep = 0.05
ButtonSleep = 0.3
DimButtonSleep = 0.3
DimAmount = 4
DbName = "LightStateDB.db"


sceneoff = {"on":False}
sceneon = {"on":True}
scene1 = {"on":True, "bri":175, "ct":447, "sat":200, "hue":13544}
scene2 = {"on":True, "bri":175, "ct":346, "sat":121, "hue":15324}
scene3 = {"on":True, "bri":175, "ct":233, "sat":251, "hue":34075}
scene4 = {"on":True, "bri":175, "ct":156, "sat":55, "hue":33042}

# Switch 1 Pins: ON, OFF, UP, DOWN
Switch1 = [13,15,16,18]

Switch1_On1_Bulps = [1,2,3,5]
Switch1_On1_Bulp_Scenes = [sceneoff,scene2,scene3,scene4]
Switch1_On2_Bulps = [1,2,3,5]
Switch1_On2_Bulp_Scenes = [scene1,scene1,sceneoff,scene1]
Switch1_On3_Bulps = [1,2,3,5]
Switch1_On3_Bulp_Scenes = [scene3,scene2,scene3,sceneoff]
Switch1_On4_Bulps = [1,2,3,5]
Switch1_On4_Bulp_Scenes = [scene1,sceneoff,sceneoff,sceneoff]









url = "http://%s/api/%s/lights/" %(HueIp, HueKey)

def createnewdb():
	CheckIfDbExists = os.path.isfile(DbName)
	if CheckIfDbExists:
		os.remove(DbName)
		print "Old DB Deleted"
	
	
	con = lite.connect(DbName)
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
	con = lite.connect(DbName)
	while True:
		ALL = requests.get(url)
		ALL = ALL.json()
		sleep (DbUpdateSleep)

		#       Set Values in DB
		with con:
			cur = con.cursor()
			BulbId = 1
			while BulbId < Bulbs:
				cur.execute("UPDATE Lights SET Lampon=?,Bri=?,Hue=?,Sat=?,Ct=? WHERE Id=?;",(ALL['1']['state']['on'], ALL['1']['state']['bri'], ALL['1']['state']['hue'], ALL['1']['state']['sat'], ALL['1']['state']['ct'], BulbId))
				BulbId += 1


	

def mainfunc():
	print 'Program running..'
	con = lite.connect(DbName)
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

		L1ID = 1
		L1ON = Lamp[0]['on']
		L1BRI = Lamp[0]['bri']
		L1BRI = int(L1BRI)

		L2ID = 2
		L2ON = Lamp[1]['on']
		L2BRI = Lamp[1]['bri']
		L2BRI = int(L2BRI)

		L3ID = 3
		L3ON = Lamp[2]['on']
		L3BRI = Lamp[2]['bri']
		L3BRI = int(L3BRI)

		L4ID = 4
		L4ON = Lamp[3]['on']
		L4BRI = Lamp[3]['bri']
		L4BRI = int(L4BRI)

		L5ID = 5
		L5ON = Lamp[4]['on']
		L5BRI = Lamp[4]['bri']
		L5BRI = int(L5BRI)

		L6ID = 6
		L6ON = Lamp[5]['on']
		L6BRI = Lamp[5]['bri']
		L6BRI = int(L6BRI)

		def lightup( LID, LON, LBRI ):
			L = "%s%s/state" %(url, LID)
			if LBRI - 254 / DimAmount < 254 - 254 / DimAmount and LON == 1:
				LBRI += 254 / DimAmount
				bri_up = {"on":True, "bri":LBRI}
				u = requests.put(L, json.dumps(bri_up), timeout=5)

			else:
				bri = 254
				bri_up = {"bri":bri}
				u = requests.put(L, json.dumps(bri_up), timeout=5)
		

		def lightdown( LID, LON, LBRI ):
			L = "%s%s/state" %(url, LID)
			if LBRI >= 254 / DimAmount and LON == 1:
				LBRI -= 254 / DimAmount
				bri_down = {"on":True, "bri":LBRI}
				u = requests.put(L, json.dumps(bri_down), timeout=5)

			else:
				bri = 0
				bri_down = {"on":True, "bri":bri}
				u = requests.put(L, json.dumps(bri_down), timeout=5)


		def lighton( LID, LON, SCE ):
			L = "%s%s/state" %(url, LID)
			if LON == 0:
				u = requests.put(L, json.dumps(sceneon), timeout=5)

			else: # LON == 1:
				u = requests.put(L, json.dumps(SCE), timeout=5)


		def lightoff( LID, LON ):
			L = "%s%s/state" %(url, LID)
			u = requests.put( L, json.dumps(sceneoff), timeout=5)


					########## Afbryder Sovevrelse	 ##########
						##### Afbryder Knap Op #####

		
		if (GPIO.input(Switch1[0]) == 1):
			Counter += 1
			Count = 0
			if Counter == 1:
				
				while len(Switch1_On1_Bulps) > Count:
					light_on1 = lighton( Switch1_On1_Bulps[Count], Lamp[(Switch1_On1_Bulps[Count])]['on'], Switch1_On1_Bulp_Scenes[Count] )
					Count += 1
			elif Counter == 2:
				while len(Switch1_On2_Bulps) > Count:
					light_on1 = lighton( Switch1_On2_Bulps[Count], Lamp[(Switch1_On2_Bulps[Count])]['on'], Switch1_On2_Bulp_Scenes[Count] )
					Count += 1
			elif Counter == 3:
				while len(Switch1_On3_Bulps) > Count:
					light_on1 = lighton( Switch1_On3_Bulps[Count], Lamp[(Switch1_On3_Bulps[Count])]['on'], Switch1_On3_Bulp_Scenes[Count] )
					Count += 1
			elif Counter == 4:
				while len(Switch1_On4_Bulps) > Count:
					light_on1 = lighton( Switch1_On4_Bulps[Count], Lamp[(Switch1_On4_Bulps[Count])]['on'], Switch1_On4_Bulp_Scenes[Count] )
					Count += 1
				Counter = 0
			sleep(ButtonSleep)

		if (GPIO.input(Switch1[1]) == 1):
			light_off1 = lightoff( L1ID, L1ON )
			light_off2 = lightoff( L2ID, L2ON )
			light_off3 = lightoff( L3ID, L3ON )
			light_off5 = lightoff( L5ID, L5ON )
			sleep(ButtonSleep)
		if (GPIO.input(Switch1[2]) == 1):
			bri_up1 = lightup( L1ID, L1ON, L1BRI )
			bri_up2 = lightup( L2ID, L2ON, L2BRI )
			bri_up3 = lightup( L3ID, L3ON, L3BRI )
			bri_up5 = lightup( L5ID, L5ON, L5BRI )
			sleep(DimButtonSleep)

		if (GPIO.input(Switch1[3]) == 1):
			bri_down1 = lightdown( L1ID, L1ON, L1BRI )
			bri_down2 = lightdown( L2ID, L2ON, L2BRI )
			bri_down3 = lightdown( L3ID, L3ON, L3BRI )
			bri_down5 = lightdown( L5ID, L5ON, L5BRI )
			sleep(DimButtonSleep)

GPIO.setmode(GPIO.BOARD)
for swi1 in Switch1:
	GPIO.setup(swi1, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)

createnewdb()
if __name__ == '__main__':
	Thread(target = updatedb).start()
	Thread(target = mainfunc).start()
