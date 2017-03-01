import requests
import json
import time
coun = 0

if coun == 0:
	coun += 1
	r = requests.get('http://192.168.0.100/api/9QzpiSZhWWsY3PoRxpfvGAKCkTxhWcluhac54pBP/lights/1')
        r = r.json()


	


	u = requests.get('http://192.168.0.100/api/9QzpiSZhWWsY3PoRxpfvGAKCkTxhWcluhac54pBP/lights/2')
        u = u.json()
      
	n = requests.get('http://192.168.0.100/api/9QzpiSZhWWsY3PoRxpfvGAKCkTxhWcluhac54pBP/lights/3')
        n = n.json()
      

	a = requests.get('http://192.168.0.100/api/9QzpiSZhWWsY3PoRxpfvGAKCkTxhWcluhac54pBP/lights/4')
        a = a.json()
      
      

	w = requests.get('http://192.168.0.100/api/9QzpiSZhWWsY3PoRxpfvGAKCkTxhWcluhac54pBP/lights/5')
        w = w.json()
      
      

	y = requests.get('http://192.168.0.100/api/9QzpiSZhWWsY3PoRxpfvGAKCkTxhWcluhac54pBP/lights/6')
	y = y.json()
      
        
	
print "Name:",r['name'],"On:",r['state']['on'], "	Bri:",r['state']['bri'], "	Ct:",r['state']['ct'], "	Hue:",r['state']['hue'], "	Sat:",r['state']['sat']
print "Name:",u['name'],"On:",u['state']['on'], "	Bri:",u['state']['bri'], "	Ct:",u['state']['ct'], "	Hue:",u['state']['hue'], "	Sat:",u['state']['sat']
print "Name:",n['name'],"On:",n['state']['on'], "	Bri:",n['state']['bri'], "	Ct:",n['state']['ct'], "	Hue:",n['state']['hue'], "	Sat:",n['state']['sat']
print "Name:",a['name'],"On:",a['state']['on'], "	Bri:",a['state']['bri'], "	Ct:",a['state']['ct'], "	Hue:",a['state']['hue'], "	Sat:",a['state']['sat']
print "Name:",w['name'],"On:",w['state']['on'], "	Bri:",w['state']['bri'], "	Ct:",w['state']['ct']	
print "Name:",y['name'],"On:",y['state']['on'], "	Bri:",y['state']['bri']

