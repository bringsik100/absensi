import json
from datetime import datetime as dt
from datetime import timedelta as dt

class test_shift_rule:
	'''class untuk menentukan shift'''
	def __init__(self,**kwargs):
		'''shift'''
		self.kwargs = kwargs
		self.shift_buff={}
		self.shift_buff.update(self.kwargs)

	def test_shift_sorc(self):
		'''membaca daftar shift dari shift.json '''
		with open('data/json','r') as srce:
			return json.load(srce)

	def test_shift_printa(self):
		'''menampilkan data shift dari file dan buffer ke layar'''
		print(self.test_shift_sorc() + self.shift_buff)

	def test_shift_printb(self):
		'''menampilkan data shift dari buffer ke layar'''
		print(self.shift_buff)

	def test_shift_write(self):
		with open(self.test_shift_sorc,'w') as buff:
			x = json.load(buff.read())
			y = json.dump(self.shift_buff)
			x = x + y
			buff.write(x)

if __name__ == '__main__':
	main()
