#!/usr/bin/env python3
"""
Pegawai
"""


'''
fungsi untuk create, read, write, edit, dan delete item dalam employee.json
'''
import json

class test_sumber:
	'''fungsi untuk membaca pegawai.json'''
	def __init__(self):
		'''membaca input'''
		with open('test/data/pegawai.json','r') as srce:
			return json.load(srce)

	def test_print(self):
		print(self.source)
		
class test_masuk:
	'''fungsi untuk memasukkan data ke pegawai.json'''
	def __init__(self,**kwargs):
		'''input dari user'''
		self.nopeg = nopeg
		self.akun = akun
		self.nomor = nomor
		self.nama = nama
		self.dept = dept
		self.buffer = {}
		
		'''data ditampung di buffer dan ditampilkan di layar'''
		return self.buffer.update(self.nopeg, self.akun, self.nomor, self.nama, self.dept)
		print(self.buffer)
	
	def test_print_all(self):
		''' menampilkan data source dan buffer ke layar'''
		print(test_sumber.source + self.buffer)
	
	def test_print_buff(self):
		''' menampilkan data buffer ke layar'''
		print(self.buffer)
		
	def test_write(self):
		'''menulis isi source dan buffer ke pegawai.json'''
		with open('data/pegawai.json','w') as srce:
			x = json.dumps(test_sumber.source + self.buffer)
			srce.write(x)

if __name__ == '__main__':
	main()
