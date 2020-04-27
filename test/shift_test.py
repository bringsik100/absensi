import json
from datetime import datetime as dt
from datetime import timedelta as dt

class test_shift_rule:
	'''class untuk menentukan shift'''
	def __init__(self,**kwargs):
		'''shift'''
		self.name = name
		self.weekdays = weekdays
		self.hour_start = hour_start
		self.hour_end = hour_end
		self.late_tol = late_tol
		self.early_tol = early_tol
		self.chin_min = chin_min
		self.chin_max = chin_max
		self.chout_min = chout_min
		self.chout_max = chout_max
		self.shift_buff=[]
		self.shift_buff.append(list(self.name, self.weekdays
		, self.hour_start, self.hour_end, self.late_tol
		, self.early_tol, self.chin_min, self.chin_max
		, self.chout_min, self.chout_max))

	def test_shift_sorc(self):
		'''membaca daftar shift dari shift.json '''
		return self.inp = 'data/shift.json'

	def test_shift_printa(self):
		'''menampilkan data shift dari file dan buffer ke layar'''
		print(self.test_shift_sorc + self.shift_buff)

	def test_shift_printb(self):
		'''menampilkan data shift dari buffer ke layar'''
		print(self.shift_buff)

	def test_shift_write(self):
		with open(self.test_shift_sorc,'w') as buff:
			x = json,loads(buff.read())
			y = json.dump(self.shift_buff)
			x = x + y
			buff.write(x)

if __name__ == '__main__':
	main()
