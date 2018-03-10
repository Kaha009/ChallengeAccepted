import requests
import json
from datetime import datetime
import calendar

import sys
#keyy=dict( id = 524901, APPID='5406123f5d87031c2bcc522a7f0b5636')
#def  getDay():
zipp=sys.argv[1]
fip = str(zipp)
degree_sign= u'\N{DEGREE SIGN}'
class Dayz:
	def __init__(self,day,desc,humidity,temp):
		self.day=self.whatday(day)
		self.desc = desc.title()
		self.humidity='Humidity-'+str(humidity) +'%'
		self.temp=str(temp)+degree_sign+'F'
		print(self.day +': '+self.desc+', '+self.temp +', '+self.humidity  )
	def whatday(self,dae):
		td = datetime.strptime(dae,'%Y-%m-%d').strftime('%A')
		
		if td == list(calendar.day_name)[datetime.today().weekday()]:return "Today"
		else: return td



with requests.Session() as r:
	#fi = r.get()
	keyy = {'zip':fip,'units':'imperial','APPID':'5406123f5d87031c2bcc522a7f0b5636'}
	fi = r.get('http://api.openweathermap.org/data/2.5/forecast', params = keyy)

	

	try:
		n1 = '12:00:00'
		bruh = fi.json()['cnt'] - 1
		now = datetime.now()
		today9am = now.replace(hour=9,minute=0,second=0,microsecond=0)
		if(now>today9am):
			Dayz(fi.json()['list'][0]['dt_txt'][:10],
			fi.json()['list'][0]['weather'][0]['description'],
			fi.json()['list'][0]['main']['humidity'], 
			fi.json()['list'][0]['main']['temp'])


		for x in range (0,bruh):
			if n1 in fi.json()['list'][x]['dt_txt']:
				#print("----------")
				Dayz(fi.json()['list'][x]['dt_txt'][:10], #YYYY-mm-dd
				fi.json()['list'][x]['weather'][0]['description'], #Clear Sky
				fi.json()['list'][x]['main']['humidity'], 
				fi.json()['list'][x]['main']['temp'])
				#print("\n")
	except KeyError:
		print("Invalid zipcode")

	#or n1 in noon:
	#	print('please')
	#print noon
#http://api.openweathermap.org/data/2.5/forecast?id=524901&APPID=5406123f5d87031c2bcc522a7f0b5636
r.close()

