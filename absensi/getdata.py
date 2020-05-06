#!/usr/bin/env python3
"""
Data
"""

"""
daftar nama tabel

USERINFO 	= data pegawai
HOLIDAYS        = daftar hari libur
DEPARTMENTS	= daftar departemen
CHECKINOUT	= log absensi
SCHCLASS	= jadwal kerja
SystemLog 	= log system
Machines        = mesin absensi
CHECKEXACT	= validasi absensi
ATTPARAM	= parameter/peraturan absen

import library
"""
import sqlite3 as sq
import sys
import os

'''
fungsi untuk create, read, write, edit, dan delete item dalam absensi.d
'''
'''connect ke database'''
def exque(expr):
	'''create / select table'''
	conn = sq.connect("data/absensi.db")
	curs = con.cursor
	try:
		curs.execute(expr)
		print(f'eksekusi : {args} berhasil')
	except Exception:
		conn.close()
		print(f' eksekusi gagal!\n{sys.exc_info()}\n')



def main():
	"""modul utama"""
	def menu():
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
	menu()

	data = Emp()

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
			keluar()
		else:
			print(f'opsi {opsi} tidak ditemukan, ulangi lagi?')
			return main()
	except BaseException:
		keluar()

if __name__ == '__main__':
	main()
