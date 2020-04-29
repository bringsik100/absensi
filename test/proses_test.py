import json
from datetime import datetime as dt
from datetime import timedelta as td
from random import randint as ri
class test_rules:
	'''class untuk menentukan jadwal'''
	def __init__(self,**kwargs):
		'''shift'''
		self.kwargs = kwargs
		self.buff={}
		self.buff.update(self.kwargs)

	def test_sumber(self):
		'''membaca daftar jadwal dari jadwal.json '''
		with open('test/data/jadwal.json','r') as srce:
			return json.load(srce)

	def test_printall(self):
		'''menampilkan data shift dari file dan buffer ke layar'''
		print(self.test_sumber() + self.buff)

	def test_printbuff(self):
		'''menampilkan data shift dari buffer ke layar'''
		print(self.buff)

	def test_write(self):
		with open(self.test_sumber,'w') as sorc:
			x = json.load(sorc.read())
			y = json.dump(self.buff)
			x = x + y
			sorc.write(x)
	def test_liburan(self):
		with open('test/data/liburan.json','r') as srce:
			json.load(srce)

class test_proses:
	
	def __init__(self,start,end):
		self.start = start
		self.end = end

	def test_holiday(self):
		with open('data/libur.json','r') as srce:
	return json.load(srce)

	def test_times(self):
		self.hour_in = td(hours = 8)	
		self.hour_out = [td(hours = 16), td(hours = 13)]
		self.hour_zero = td(hours = 0)
		self.check_in = td(hours = ri(7,9))
		if self.check_in.hours == 7:
			self.check_in + td(minutes = ri(0,59), seconds = ri(0,59))
		else:
			self.check_in + td(minutes = ri(0,15), seconds = ri(0,59))
		self.check_out = [td(hours = ri(16,18),minutes = ri(0,59), seconds = ri(0,59)),td(hours = ri(13,17), minutes = ri(0,59), seconds = ri(0,59)]

	def test_dates(self):
		self.delta = self.end - self.start
		self.date_list = []
		for date in self.delta.days+1:
		thisday = self.start + date
		if thisday in self.test_holiday:
			thisday_start = thisday_end = thisday_in = thisday_out = thisday + self.test_times.hour_zero
		
		else:
			if thisday.weekday == 6:				thisday_start = thisday_out = thisday_in = thisday_off =thisday + self.test_times.hour_zero
