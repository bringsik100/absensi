#!/usr/bin/env python3
"""
Pegawai
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
"""import library"""
import json

class Emp:
	'''
	fungsi untuk create, read, write, edit, dan delete item dalam employee.json
	'''
	def __init__(self):
		'''membaca file pegawai.json'''
		with open('data/pegawai.json') as source:
			self.buffer = json.load(source)
			return self.buffer

	def view_all(self):
		"""tampilkan data di layar"""
		print(self.buffer)

	def view_id(self,pid):
		"""tampilkan data pegawai dari pilihan id"""
		print(self.data[str(pid)])
	
	def find_elem(self,arg):
		"""mencari data pegawai dengan kata kunci"""
		for elem in self.data:
			if args in self.data[elem]:
				print(f'{arg} ada di dalam {self.data.[elem]}')
			else:
				print(f'data {arg} tidak ditemukan')

	def edit_elem(self,pid,**kwargs):
		"""menyunting data dari buffer"""
		self.buffer.update{[pid]:{kwargs}}
	
	def Add_elem(self,**kwargs):
		""" menambahkan data ke dalam buffer"""
		self.new_pid = str(len(self.buffer+1))
		self.buffer.update{self.new_pid:{kwargs}}

	def Delete(self,pid):
		"""menghapus data di dalam buffer"""
		self.pid = pid
		del self.buffer[self.pid]
	
	def Write(self):
		""" menulis data dari buffer ke dalam pegawai.json"""
		with open('data/pegawai.json','w') as source:
			source.write(json.dump(self.buffer))

def main():
	"""modul utama"""
	print("not ready yet")

if __name__ == '__main__':
	main()
