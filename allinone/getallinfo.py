import requests
import json
from time import sleep
import sqlite3 as lite 
import sys

con = lite.connect('LightStateDB.db')

while True:
	
        ALL = requests.get('http://192.168.0.100/api/9QzpiSZhWWsY3PoRxpfvGAKCkTxhWcluhac54pBP/lights')
        ALL = ALL.json()
	sleep (0.1)

	#	Light 1
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

	#	Light 3
	L3ID = 3
        L3NAME = ALL['3']['name']
        L3ON = ALL['3']['state']['on']
        L3BRI = ALL['3']['state']['bri']
        L3HUE = ALL['3']['state']['hue']
        L3SAT = ALL['3']['state']['sat']
        L3XY = ALL['3']['state']['xy']
        L3CT = ALL['3']['state']['ct']
        
	#	Light 4
	L4ID = 4
	L4NAME = ALL['4']['name']
        L4ON = ALL['4']['state']['on']
        L4BRI = ALL['4']['state']['bri']
        L4HUE = ALL['4']['state']['hue']
        L4SAT = ALL['4']['state']['sat']
        L4XY = ALL['4']['state']['xy']
        L4CT = ALL['4']['state']['ct']

	#	Light 5
	L5ID = 5
	L5NAME = ALL['5']['name']
        L5ON = ALL['5']['state']['on']
        L5BRI = ALL['5']['state']['bri']
        L5CT = ALL['5']['state']['ct']

	#	Light 6
	L6ID = 6
	L6NAME = ALL['6']['name']
        L6ON = ALL['6']['state']['on']
        L6BRI = ALL['6']['state']['bri']
	
	#	Set Values in DB
	with con:
		cur = con.cursor()
		cur.execute("UPDATE Lights SET Lampon=?,Bri=?,Hue=?,Sat=?,Ct=? WHERE Id=?;",(L1ON, L1BRI, L1HUE, L1SAT, L1CT, L1ID))
		cur.execute("UPDATE Lights SET Lampon=?,Bri=?,Hue=?,Sat=?,Ct=? WHERE Id=?;",(L2ON, L2BRI, L2HUE, L2SAT, L2CT, L2ID))
		cur.execute("UPDATE Lights SET Lampon=?,Bri=?,Hue=?,Sat=?,Ct=? WHERE Id=?;",(L3ON, L3BRI, L3HUE, L3SAT, L3CT, L3ID))
		cur.execute("UPDATE Lights SET Lampon=?,Bri=?,Hue=?,Sat=?,Ct=? WHERE Id=?;",(L4ON, L4BRI, L4HUE, L4SAT, L4CT, L4ID))
		cur.execute("UPDATE Lights SET Lampon=?,Bri=?,Ct=? WHERE Id=?;",(L5ON, L5BRI, L5CT, L5ID))
		cur.execute("UPDATE Lights SET Lampon=?,Bri=? WHERE Id=?;",(L6ON, L6BRI, L6ID))
