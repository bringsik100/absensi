#!/usr/bin/env python3
"""
Data
"""

"""
- buat perintah Read untuk membaca data dan menampungnya ke dalam buffer
- buat perintah View untuk menampilkan buffer ke layar
- buat perintah Find untuk mencari data di dalam buffer
- buat perintah Edit untuk menyunting data di dalam buffer
- buat perintah Create untuk menambahkan data ke dalam buffer

import library
"""
import sqlite3 as sq
import sys
import os

'''
fungsi untuk create, read, write, edit, dan delete item dalam absensi.d
'''
'''connect ke database'''
conn = sq.connect("data/absensi.db")
'''create / select table'''
curs = con.cursor
curs.execute("""create table pegawai if not exist(ID data_type PRIMARY KEY ,
	no_peg data_type int,
	no_akun data_type int,
	nama data_type varchar,
	departemen data_type varchar)""")
curs.execute("""create table jadwal if not exist(ID data_type PRIMARY KEY ,
	nama data_type int,
	hour_start data_type int,
	hour_end data_type text,
	late_in data_type text,
	early_out data_type text,
	checkin_min data_type text,
	checkin_max data_type text,
	checkout_min data_type text,
	checkout_max data_type text)""")
curs.execute("""create table libur if not exist(ID data_type PRIMARY KEY ,
	tanggal data_type text,
	hari data_type varchar)""")
curs.execute("""create table log_absensi if not exist(ID data_type PRIMARY KEY ,
	"NoPeg" data_type int,
	"No. Akun" data_type int,
	"No." data_type int,
	"Nama" data_type varchar,
	"Auto-Assign" int,
	"Tanggal" data_type text,
	"Jam Kerja" data_type varchar,
	"Awal tugas" data_type text,
	"Akhir tugas" data_type text,
	"Masuk" data_type text,
	"Keluar" data_type text,
	"Normal" data_type int,
	"Waktu real" data_type int,
	"Telat" data_type text,
	"Plg Awal" data_type text,
	"Bolos" data_type text,
	"Waktu Lembur" data_type text,
	"Waktu Kerja" data_type text,
	"Status" data_type int,
	"Hrs C/In" data_type int,
	"Hrs C/Out" data_type int,
	"Departemen" data_type varchar,
	"NDays" data_type int,
	"Akhir Pekan" data_type int,
	"Hari Libur" data_type int,
	"Lama Hadir" data_type text,
	"NDays_OT" data_type int,
	"Lembur A.Pekan" data_type int,
	"Libur Lembur" data_type int)""")


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

conn.close()
if __name__ == '__main__':
	main()
