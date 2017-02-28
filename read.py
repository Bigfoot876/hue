import json
import requests
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(16, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(18, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)

r = requests.get('http://192.168.0.100/api/9QzpiSZhWWsY3PoRxpfvGAKCkTxhWcluhac54pBP/lights/1')
r = r.json()

url1 = "http://192.168.0.100/api/9QzpiSZhWWsY3PoRxpfvGAKCkTxhWcluhac54pBP/lights/1/state"

with open('l1.txt') as infile:
	r = json.load(infile)
ru = r['state']['bri']
ruu = r['state']['on']


while True:
#	with open('l1.txt') as infile:
#		r = json.load(infile)
#	ru = r['state']['bri']
#	ruu = r['state']['on']
	
	if (GPIO.input(16) == 1):
		ruu ^= True
		if (ruu == True):
			data_on = {"on":True}
			u = requests.put(url1, json.dumps(data_on), timeout=5)
			time.sleep(1)
		else:
			data_off = {"on":False}
			r = requests.put(url1, json.dumps(data_off), timeout=5)
			time.sleep(1)
	if (GPIO.input(18) == 1):
		if ruu == False:
			ru1 = 25
			data_on = {"on":True, "sat":ru1, "bri":ru1,"hue":5000}
			u = requests.put(url1, json.dumps(data_on), timeout=5)
			time.sleep(1)
		elif ru < 225:
			ru1 = ru + 25
			data_on = {"on":True, "sat":ru1, "bri":ru1,"hue":5000}
			u = requests.put(url1, json.dumps(data_on), timeout=5)
			time.sleep(1)
			print ru1
		else:
			ru1 = 254
			data_on = {"on":True, "sat":ru1, "bri":ru1,"hue":5000}
			u = requests.put(url1, json.dumps(data_on), timeout=5)
			time.sleep(1)
	with open('l1.txt') as infile:
		r = json.load(infile)
	ru = r['state']['bri']
	ruu = r['state']['on']
