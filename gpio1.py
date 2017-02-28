import time
import RPi.GPIO as GPIO
import requests
import json

url = "http://192.168.0.100/api/9QzpiSZhWWsY3PoRxpfvGAKCkTxhWcluhac54pBP/lights/2/state"
url1 = "http://192.168.0.100/api/9QzpiSZhWWsY3PoRxpfvGAKCkTxhWcluhac54pBP/lights/1/state"
url2 = "http://192.168.0.100/api/9QzpiSZhWWsY3PoRxpfvGAKCkTxhWcluhac54pBP/lights/3/state"


data_on = {"on":True}
data_off = {"on":False}
scene1 = {"sat":254, "bri":254, "hue":5000}
scene2 = {"sat":225, "bri":225, "hue":5000}
scene3 = {"sat":200, "bri":200, "hue":5000}
scene4 = {"sat":175, "bri":175, "hue":5000}
scene5 = {"sat":150, "bri":150, "hue":5000}
scene6 = {"sat":125, "bri":125, "hue":5000}
scene7 = {"sat":100, "bri":100, "hue":5000}
scene8 = {"sat":75, "bri":75, "hue":5000}
scene9 = {"sat":50, "bri":50, "hue":5000}



GPIO.setmode(GPIO.BOARD)
GPIO.setup(16, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(18, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
b = False
c = 0
while True:
	if (GPIO.input(16) == 1):
		b ^= True
		if (b == True):
			r = requests.put(url, json.dumps(data_on), timeout=5)
			u = requests.put(url1, json.dumps(data_on), timeout=5)
			n = requests.put(url2, json.dumps(data_on), timeout=5)
			time.sleep(1)
		else:
			r = requests.put(url, json.dumps(data_off), timeout=5)
			u = requests.put(url1, json.dumps(data_off), timeout=5)
                        n = requests.put(url2, json.dumps(data_off), timeout=5)
			time.sleep(1)

	if (GPIO.input(18) == 1):
		c = c + 1
		if (c == 1):
			r1 = requests.put(url, json.dumps(scene1), timeout=5)
                        u1 = requests.put(url1, json.dumps(scene1), timeout=5)
                        n1 = requests.put(url2, json.dumps(scene1), timeout=5)
			time.sleep(0.5)
		elif (c == 2):
			r1 = requests.put(url, json.dumps(scene2), timeout=5)
                        u1 = requests.put(url1, json.dumps(scene2), timeout=5)
                        n1 = requests.put(url2, json.dumps(scene2), timeout=5)
			time.sleep(0.5)
		elif (c == 3):
			r1 = requests.put(url, json.dumps(scene3), timeout=5)
                        u1 = requests.put(url1, json.dumps(scene3), timeout=5)
                        n1 = requests.put(url2, json.dumps(scene3), timeout=5)
			time.sleep(0.5)
		if (c == 4):
                        r1 = requests.put(url, json.dumps(scene4), timeout=5)
                        u1 = requests.put(url1, json.dumps(scene4), timeout=5)
                        n1 = requests.put(url2, json.dumps(scene4), timeout=5)
                        time.sleep(0.5)
                elif (c == 5):
                        r1 = requests.put(url, json.dumps(scene5), timeout=5)
                        u1 = requests.put(url1, json.dumps(scene5), timeout=5)
                        n1 = requests.put(url2, json.dumps(scene5), timeout=5)
                        time.sleep(0.5)
                elif (c == 6):
                        r1 = requests.put(url, json.dumps(scene6), timeout=5)
                        u1 = requests.put(url1, json.dumps(scene6), timeout=5)
                        n1 = requests.put(url2, json.dumps(scene6), timeout=5)
                        time.sleep(0.5)
		if (c == 7):
                        r1 = requests.put(url, json.dumps(scene7), timeout=5)
                        u1 = requests.put(url1, json.dumps(scene7), timeout=5)
                        n1 = requests.put(url2, json.dumps(scene7), timeout=5)
                        time.sleep(0.5)
                elif (c == 8):
                        r1 = requests.put(url, json.dumps(scene8), timeout=5)
                        u1 = requests.put(url1, json.dumps(scene8), timeout=5)
                        n1 = requests.put(url2, json.dumps(scene8), timeout=5)
                        time.sleep(0.5)
                elif (c == 9):
                        r1 = requests.put(url, json.dumps(scene9), timeout=5)
                        u1 = requests.put(url1, json.dumps(scene9), timeout=5)
                        n1 = requests.put(url2, json.dumps(scene9), timeout=5)
                        time.sleep(0.5)
                        c = 0

GPIO.cleanup()

