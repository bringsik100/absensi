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
import sys

class Emp:
	'''
	fungsi untuk create, read, write, edit, dan delete item dalam pegawai.json
	'''
	def __init__(self):
		print("ready")

	def view_all(self):
		'''membaca file pegawai.json'''
		with open('data/pegawai.json') as source:
			self.buffer = json.load(source)
		"""tampilkan data di layar"""
		for i in self.buffer:
			print(f'ID {i} = {self.buffer[i]}')
		return main()
	def view_id(self):
		self.buffef =self.view_all()
		"""tampilkan data pegawai dari pilihan id"""
		self.pid =str(input('masukkan id pegawai :  '))
		try:
			if self.pid in self.buffer:
				print(self.buffer[self.pid])
				return main()
			else:
				print(f"pegawai dengan ID {self.pid} tidak ditemukan \nulangi?\npilih Y untuk mengulangi pencarian\n")
				pilihan =str(input("ulangi pencarian? "))
				if pilihan.lower()=='y':
					return view_id()
				else:
					return main()
		except Exception:
			print(sys.exc_info())
			pass
	def find_elem(self,arg):
		"""mencari data pegawai dengan kata kunci"""
		for elem in self.buffer:
			if args in self.buffer[elem]:
				print(f'{arg} ada di dalam {self.buffer[elem]}')
			else:
				print(f'data {arg} tidak ditemukan')

	def edit_elem(self,pid,**kwargs):
		"""menyunting data dari buffer"""
		self.buffer.update({[str(pid)]:{kwargs}})
	
	def Add_elem(self,**kwargs):
		""" menambahkan data ke dalam buffer"""
		self.new_pid = str(len(self.buffer+1))
		self.buffer.update({self.new_pid:{kwargs}})

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
	def menu():
		"""pilihan menu"""
		print("""\n
		pilih perintah :
		1 tampilkan data
		2 cari data
		3 sunting data 
		4 tambah data 
		5 tulis data 
		6 hapus data
		0 keluar 
		\n""")
	menu()
	
	data = Emp()
	
	opsi = int(input("pilih opsi : "))
	try:
		if opsi == 1:
			data.view_all()
		elif opsi == 2:
			data.view_id()
		elif opsi == 3:
			data.view_all()
		elif opsi == 4:
			data.view_all()
		elif opsi == 5:
			data.view_all()
		elif opsi == 0:
			sys.exit
		else:
			pass
	except BaseException:
		print(sys.exc_info())
		sys.exit


if __name__ == '__main__':
	main()
