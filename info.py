import requests
import json
import time

while True:
	r = requests.get('http://192.168.0.100/api/9QzpiSZhWWsY3PoRxpfvGAKCkTxhWcluhac54pBP/lights/1')
        r = r.json()
   #     with open('l1.txt', 'w') as outfile:
  #              json.dump(r, outfile)



	with open('l1.txt', 'w') as outfile:
		json.dump(r, outfile, sort_keys = True, indent = 4, ensure_ascii = False)






	u = requests.get('http://192.168.0.100/api/9QzpiSZhWWsY3PoRxpfvGAKCkTxhWcluhac54pBP/lights/2')
        u = u.json()
        with open('l2.txt', 'w') as outfile:
                json.dump(u, outfile)

	n = requests.get('http://192.168.0.100/api/9QzpiSZhWWsY3PoRxpfvGAKCkTxhWcluhac54pBP/lights/3')
        n = n.json()
        with open('l3.txt', 'w') as outfile:
                json.dump(n, outfile)

	a = requests.get('http://192.168.0.100/api/9QzpiSZhWWsY3PoRxpfvGAKCkTxhWcluhac54pBP/lights/4')
        a = a.json()
        with open('l4.txt', 'w') as outfile:
                json.dump(a, outfile)

	w = requests.get('http://192.168.0.100/api/9QzpiSZhWWsY3PoRxpfvGAKCkTxhWcluhac54pBP/lights/5')
        w = w.json()
        with open('l5.txt', 'w') as outfile:
                json.dump(w, outfile)

	y = requests.get('http://192.168.0.100/api/9QzpiSZhWWsY3PoRxpfvGAKCkTxhWcluhac54pBP/lights/6')
	y = y.json()
        with open('l6.txt', 'w') as outfile:
                json.dump(y, outfile)
        time.sleep(2)
	
#print "Name:",r['name'],"		On:",r['state']['on'], "		Bri:",r['state']['bri']
#print "Name:",u['name'],"		On:",u['state']['on'], "		Bri:",u['state']['bri']
#print "Name:",n['name'],"		On:",n['state']['on'], "		Bri:",n['state']['bri']
#print "Name:",a['name'],"		On:",a['state']['on'], "		Bri:",a['state']['bri']
#print "Name:",w['name'],"		On:",w['state']['on'], "		Bri:",w['state']['bri']
#print "Name:",y['name'],"		On:",y['state']['on'], "		Bri:",y['state']
