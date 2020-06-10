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
"""import library"""
import json
import sys
import pytest

class test_Emp:
	'''
	fungsi untuk create, read, write, edit, dan delete item dalam jadwal.json
	'''
	def __init__(self):
		print("ready")

	def test_buffer(self):
		'''membaca file jadwal.json'''
		with open('data/jadwal.json') as source:
			return  json.load(source)
	def test_view_all(self):
		"""tampilkan data di layar"""
		for i in self.test_buffer():
			print("ID {i} = {self.buffer()[i]}")
		return test_main()

	def test_view_id(self):
		"""tampilkan data jadwal dari pilihan id"""
		self.pid = str(input('masukkan id jadwal :  '))
		try:
			if self.pid in self.test_buffer():
				print(self.test_buffer()[self.pid])
				return test_main()
			else:
				print(f"jadwal dengan ID {self.pid} tidak ditemukan \nulangi?\npilih Y untuk mengulangi pencarian\n")
				pilihan =str(input("ulangi pencarian? "))
				if pilihan.lower()=='y':
					return view_id()
				else:
					return test_main()
		except Exception:
			print(sys.exc_info())
			return test_main()
	
	def test_find_elem(self):
		"""mencari data jadwal dengan kata kunci"""
		self.args=input('masukkan data yang dicari :')
		try:
			for id in self.test_buffer():
				if self.args in self.test_buffer()[id]:
					print(f'{self.arg} ada di dalam {self.test_buffer()[id]}')
					return test_main()
				else:
					print(f'data {self.arg} tidak ditemukan')
					pilihan =str(input("ulangi pencarian? "))
				if pilihan.lower()=='y':
					return find_elem()
				else:
					return test_main()
		except Exception:
			print(sys.exc_info())
			return test_main()

	def test_edit_elem(self):
		"""menyunting data dari buffer"""
		self.pid = str(input('masukkan id jadwal :  '))
		self.kwargs=input('masukkan data :')
		try:
			self.test_buffer().update({self.pid:{self.kwargs}})
			return test_main()
		except Exception:
			print(sys.exc_info())
			return test_main()

	def test_Add_elem(self):
		""" menambahkan data ke dalam buffer"""
		self.kwargs=input('masukkan data :')
		try:
			self.new_pid = str(len(self.test_buffer()+1))
			self.test_buffer().update({self.new_pid:{self.kwargs}})
		except Exception:
			print(sys.exc_info())
			return test_main()

	def test_del_data(self):
		"""menghapus data di dalam buffer"""
		self.pid = str(input('masukkan id jadwal :  '))
		try:
			del self.test_buffer()[self.pid]
		except Exception:
			print(sys.exc_info())
			return test_main()

	def test_write_data(self):
		""" menulis data dari buffer ke dalam jadwal.json"""
		with open('data/jadwal.json','w') as source:
			source.write(json.dump(self.test_buffer))

def test_keluar():
	print("\terima kasih")
	return sys.exit

def test_main():
	"""modul utama"""
	def test_menu():
		"""pilihan menu"""
		print("""\n
		pilih perintah :
		1 tampilkan semua data
		2 tampilkan data per id
		3 cari data
		4 sunting data
		5 tambah data
		6 tulis data
		7 hapus data
		0 keluar
		\n""")
	test_menu()

	data = test_Emp()

	opsi = int(input("pilih opsi : "))
	try:
		if opsi == 1:
			data.view_all()
		elif opsi == 2:
			data.view_id()
		elif opsi == 3:
			data.find_elem()
		elif opsi == 4:
			data.edit_elem()
		elif opsi == 5:
			data.add_elem()
		elif opsi == 6:
			data.write_data()
		elif opsi == 7:
			data.del_data()
		elif opsi == 0:
			test_keluar()
		else:
			print(f'opsi {opsi} tidak ditemukan, ulangi lagi?')
			return test_main()
	except BaseException:
		test_keluar()


if __name__ == '__main__':
	test_main()
