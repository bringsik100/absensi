#!/usr/bin/env python3
"""
Jadwal
"""
"""
- buat perintah Read untuk membaca data dan menampungnya ke dalam buffer
- buat perintah View untuk menampilkan buffer ke layar
- buat perintah Find untuk mencari data di dalam buffer
- buat perintah Edit untuk menyunting data di dalam buffer
- buat perintah Create untuk menambahkan data ke dalam buffer
- buat perintah Delete untuk menghapus data di dalam buffer
- buat perintah Write untuk menuliskan buffer ke dalam data
"""

import json
from datetime import datetime as dt
from datetime import timedelta as dt

"""import library"""
import json

class Sched:
	'''
	fungsi untuk create, read, write, edit, dan delete item dalam jadwal.json
	'''
	def __init__(self):

	def view_all(self):
		'''membaca file jadwal.json'''
		with open('data/jadwal.json') as source:
			self.buffer = json.load(source)

		"""tampilkan data di layar"""
		print(self.buffer)

	def view_id(self,pid):
		"""tampilkan data jadwal dari pilihan id"""
		print(self.buffer[str(pid)])
	
	def find_elem(self,arg):
		"""mencari data jadwal dengan kata kunci"""
		for elem in self.buffer:
			if args in self.buffer[elem]:
				print(f'{arg} ada di dalam {self.buffer[elem]}')
			else:
				print(f'data {arg} tidak ditemukan')

	def edit_elem(self,pid,**kwargs):
		"""menyunting data dari buffer"""
		self.buffer.update{[str(pid)]:{kwargs}}
	
	def Add_elem(self,**kwargs):
		""" menambahkan data ke dalam buffer"""
		self.new_pid = str(len(self.buffer+1))
		self.buffer.update{self.new_pid:{kwargs}}

	def Delete(self,pid):
		"""menghapus data di dalam buffer"""
		self.pid = pid
		del self.buffer[str(self.pid)]
	
	def Write(self):
		""" menulis data dari buffer ke dalam pegawai.json"""
		with open('data/jadwal.json','w') as source:
			source.write(json.dump(self.buffer))

def main():
	"""modul utama"""
	def menu():
		"""pilihan menu"""
		print("""\n
		pilih perintah :
		1 tampilkan data
		2 cari data
		3 sunting data 
		4 tambah data 
		5 tulis data 
		0 hapus data 
		\n""")
	menu()
	
	data = Sched()
	
	opsi = input("pilih opsi : ")
	try:
		if int(opsi) == 1:
			data.view_all()
		elif int(opsi) == 2:
			data.view_all()
		elif int(opsi) == 3:
			data.view_all()
		elif int(opsi) == 4:
			data.view_all()
		elif int(opsi) == 5:
			data.view_all()
		elif int(opsi) == 0:
			data.view_all()
		else:
	except Exception:
		print(Exception)
		pass

if __name__ == '__main__':
	main()
