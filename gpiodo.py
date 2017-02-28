#       Username: 9QzpiSZhWWsY3PoRxpfvGAKCkTxhWcluhac54pBP

import requests
import json

url = "http://192.168.0.100/api/9QzpiSZhWWsY3PoRxpfvGAKCkTxhWcluhac54pBP/lights/2/state"


#data_on = {"on":True, "sat":bri, "bri":254,"hue":5000}
#data_off = {"on":False}

r = requests.get('http://192.168.0.100/api/9QzpiSZhWWsY3PoRxpfvGAKCkTxhWcluhac54pBP/lights/2')
#print (r.text)

r = r.json()
print r['state']['bri']
ru = r['state']['bri']
print r['state']['hue']
print r['state']['sat']




if ru < 203:
        ru = ru + 50
        data_on = {"on":True, "sat":ru, "bri":ru,"hue":5000}
        u = requests.put(url, json.dumps(data_on), timeout=5)

        print ru

else:
        ru = 254
        data_on = {"on":True, "sat":ru, "bri":ru,"hue":5000}
        u = requests.put(url, json.dumps(data_on), timeout=5)

