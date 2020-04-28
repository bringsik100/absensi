import json
from datetime import datetime as dt
from datetime import timedelta as dt

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

if __name__ == '__main__':
	main()
