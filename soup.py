import requests
import json
import sqlite3 as lite
from time import sleep
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setup(16, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(18, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)


url = "http://192.168.0.100/api/9QzpiSZhWWsY3PoRxpfvGAKCkTxhWcluhac54pBP/lights/"
con = lite.connect('test.db')


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




while True:

########## Afbryder Sovevrelse ##########


	##### Afbryder Knap Op #####

        if (GPIO.input(16) == 1):
		

		### Light 1 ###
		if L1BRI < 229 and L1ON == "1":
		        L1BRI += 25
		        bri_up = {"on":True, "bri":L1BRI}
		        u = requests.put(url + L1, json.dumps(bri_up), timeout=5)
			with con:
		                cur = con.cursor()
		                cur.execute("UPDATE Lights SET Bri=? WHERE Id=?;",(L1BRI, L1ID))

		elif L1BRI > 228 and L1ON == "1":
			bri = 254
		        bri_max = {"bri":bri}
		        u = requests.put(url + L1, json.dumps(bri_max), timeout=5)
			with con:
				cur = con.cursor()
				cur.execute("UPDATE Lights SET Bri=? WHERE Id=?;",(bri, L1ID))
		sleep(0.5)

	##### Afbryder Knap Ned #####

        if (GPIO.input(18) == 1):


		### Light 1 ###
                if L1BRI > 25 and L1ON == "1":
                        L1BRI -= 25
                        bri_down = {"on":True, "bri":L1BRI}
                        u = requests.put(url + L1, json.dumps(bri_down), timeout=5)
                        with con:
                                cur = con.cursor()
                                cur.execute("UPDATE Lights SET Bri=? WHERE Id=?;",(L1BRI, L1ID))

                elif L1BRI < 26 and L1ON == "1":
                        bri = 0
                        bri_down = {"on":False, "bri":bri}
                        u = requests.put(url + L1, json.dumps(bri_down), timeout=5)
                        with con:
                                cur = con.cursor()
                                cur.execute("UPDATE Lights SET Lampon=?, Bri=? WHERE Id=?;",("False", bri, L1ID))




                ### Light 2 ###
                if L2BRI > 25 and L2ON == "1":
                        L2BRI -= 25
                        bri_down = {"on":True, "bri":L2BRI}
                        u = requests.put(url + L2, json.dumps(bri_down), timeout=5)
                        with con:
                                cur = con.cursor()
                                cur.execute("UPDATE Lights SET Bri=? WHERE Id=?;",(L2BRI, L2ID))

                elif L2BRI < 26 and L2ON == "1":
                        bri = 0
                        bri_down = {"on":False, "bri":bri}
                        u = requests.put(url + L2, json.dumps(bri_down), timeout=5)
                        with con:
                                cur = con.cursor()
                                cur.execute("UPDATE Lights SET Lampon=?, Bri=? WHERE Id=?;",("False", bri, L2ID))
		sleep(0.5)











"""





#Light 2
if L2BRI < 229 and L2ON == "1":
        L2BRI += 25
        bri_up = {"on":True, "bri":L2BRI}
        u = requests.put(url + L2, json.dumps(bri_up), timeout=5)
        with con:
                cur = con.cursor()
                cur.execute("UPDATE Lights SET Bri=? WHERE Id=?;",(L2BRI, L2ID))



elif L2BRI > 228 and L2ON == "1":
        bri = 254
        bri_max = {"bri":bri}
        u = requests.put(url + L2, json.dumps(bri_max), timeout=5)
        with con:
                cur = con.cursor()
                cur.execute("UPDATE Lights SET Bri=? WHERE Id=?;",(bri, L2ID))


#Light 3
if L3BRI < 229 and L3ON == "1":
        L3BRI += 25
        bri_up = {"on":True, "bri":L3BRI}
        u = requests.put(url + L3, json.dumps(bri_up), timeout=5)
        with con:
                cur = con.cursor()
                cur.execute("UPDATE Lights SET Bri=? WHERE Id=?;",(L3BRI, L3ID))



elif L3BRI > 228 and L3ON == "1":
        bri = 254
        bri_max = {"bri":bri}
        u = requests.put(url + L3, json.dumps(bri_max), timeout=5)
        with con:
                cur = con.cursor()
                cur.execute("UPDATE Lights SET Bri=? WHERE Id=?;",(bri, L3ID))

#Light 4
if L4BRI < 229 and L4ON == "1":
        L4BRI += 25
        bri_up = {"on":True, "bri":L4BRI}
        u = requests.put(url + L4, json.dumps(bri_up), timeout=5)
        with con:
                cur = con.cursor()
                cur.execute("UPDATE Lights SET Bri=? WHERE Id=?;",(L4BRI, L4ID))



elif L4BRI > 228 and L4ON == "1":
        bri = 254
        bri_max = {"bri":bri}
        u = requests.put(url + L4, json.dumps(bri_max), timeout=5)
        with con:
                cur = con.cursor()
                cur.execute("UPDATE Lights SET Bri=? WHERE Id=?;",(bri, L4ID))

#Light 5
if L5BRI < 229 and L5ON == "1":
        L5BRI += 25
        bri_up = {"on":True, "bri":L5BRI}
        u = requests.put(url + L5, json.dumps(bri_up), timeout=5)
        with con:
                cur = con.cursor()
                cur.execute("UPDATE Lights SET Bri=? WHERE Id=?;",(L5BRI, L5ID))



elif L5BRI > 228 and L5ON == "1":
        bri = 254
        bri_max = {"bri":bri}
        u = requests.put(url + L5, json.dumps(bri_max), timeout=5)
        with con:
                cur = con.cursor()
                cur.execute("UPDATE Lights SET Bri=? WHERE Id=?;",(bri, L5ID))

#Light 6
if L6BRI < 229 and L6ON == "1":
        L6BRI += 25
        bri_up = {"on":True, "bri":L6BRI}
        u = requests.put(url + L6, json.dumps(bri_up), timeout=5)
        with con:
                cur = con.cursor()
                cur.execute("UPDATE Lights SET Bri=? WHERE Id=?;",(L6BRI, L6ID))



elif L6BRI > 228 and L6ON == "1":
        bri = 254
        bri_max = {"bri":bri}
        u = requests.put(url + L6, json.dumps(bri_max), timeout=5)
        with con:
                cur = con.cursor()
                cur.execute("UPDATE Lights SET Bri=? WHERE Id=?;",(bri, L6ID))

"""
