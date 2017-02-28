import requests
import json
import sqlite3 as lite
from time import sleep
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setup(16, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(18, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(15, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(13, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)

url = "http://192.168.0.100/api/9QzpiSZhWWsY3PoRxpfvGAKCkTxhWcluhac54pBP/lights/"
con = lite.connect('test.db')


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


	def lightup( LID, LON, LBRI, L ):

		if LBRI < 204 and LON == "1":
			LBRI += 50
			bri_up = {"on":True, "bri":LBRI}
			u = requests.put(url + L, json.dumps(bri_up), timeout=5)
			with con:
				cur = con.cursor()
				cur.execute("UPDATE Lights SET Bri=? WHERE Id=?;",(LBRI, LID))

		elif LBRI > 203 and LON == "1":
			bri = 254
			bri_up = {"bri":bri}
			u = requests.put(url + L, json.dumps(bri_up), timeout=5)
			with con:
				cur = con.cursor()
				cur.execute("UPDATE Lights SET Bri=? WHERE Id=?;",(bri, LID))


	def lightdown( LID, LON, LBRI, L ): 

		if LBRI > 50 and LON == "1":
			LBRI -= 50
			bri_down = {"on":True, "bri":LBRI}
			u = requests.put(url + L, json.dumps(bri_down), timeout=5)
	                with con:
	                	cur = con.cursor()
	                        cur.execute("UPDATE Lights SET Bri=? WHERE Id=?;",(LBRI, LID))

		elif LBRI < 51 and LON == "1":
			bri = 0
	                bri_down = {"on":True, "bri":bri}
	                u = requests.put(url + L, json.dumps(bri_down), timeout=5)
	                with con:
	                	cur = con.cursor()
	                        cur.execute("UPDATE Lights SET Lampon=?, Bri=? WHERE Id=?;",("True", bri, LID))


	def lighton( LID, LON, L ):

		if LON == "0":
			on = {"on":True}
			u = requests.put(url + L, json.dumps(on), timeout=5)
			with con:
                                cur = con.cursor()
                                cur.execute("UPDATE Lights SET Lampon=? WHERE Id=?;",("True", LID))


	def lightoff( LID, LON, L ):

		if LON == "1":
			on = {"on":False}
			u = requests.put(url + L, json.dumps(on), timeout=5)
			with con:
                                cur = con.cursor()
                                cur.execute("UPDATE Lights SET Lampon=? WHERE Id=?;",("False", LID))


########## Afbryder Sovevrelse ##########


	##### Afbryder Knap Op #####

        if (GPIO.input(13) == 1):
		bri_up1 = lightup( L1ID, L1ON, L1BRI, L1 )
		bri_up2 = lightup( L2ID, L2ON, L2BRI, L2 )
		bri_up3 = lightup( L3ID, L3ON, L3BRI, L3 )
                bri_up4 = lightup( L4ID, L4ON, L4BRI, L4 )
		sleep(0.025)
        if (GPIO.input(15) == 1):
                bri_down1 = lightdown( L1ID, L1ON, L1BRI, L1 )
                bri_down2 = lightdown( L2ID, L2ON, L2BRI, L2 )
                bri_down3 = lightdown( L3ID, L3ON, L3BRI, L3 )
                bri_down4 = lightdown( L4ID, L4ON, L4BRI, L4 )
                sleep(0.025)

	if (GPIO.input(16) == 1):
		light_on1 = lighton( L1ID, L1ON, L1 )
                light_on2 = lighton( L2ID, L2ON, L2 )
                light_on3 = lighton( L3ID, L3ON, L3 )
                light_on4 = lighton( L4ID, L4ON, L4 )
		sleep(0.025)
	if (GPIO.input(18) == 1):
		light_off1 = lightoff( L1ID, L1ON, L1 )
                light_off2 = lightoff( L2ID, L2ON, L2 )
                light_off3 = lightoff( L3ID, L3ON, L3 )
                light_off4 = lightoff( L4ID, L4ON, L4 )
		sleep(0.025)
