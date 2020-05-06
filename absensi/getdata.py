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
def create_table(args):
	'''create / select table'''
	conn = sq.connect("data/absensi.db")
	curs = con.cursor
	try:
		curs.execute(args)
		print(f'eksekusi : {args} berhasil')
	except Exception:
		print(f' eksekusi gagal!\n{sys.exc_info()}\n')

curs.execute("""create table pegawai if not exist(ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
	no_peg int NOT NULL,
	no_akun int NOT NULL,
	nama text,
	departemen text)""")
curs.execute("""create table jadwal if not exist(ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
	nama int,
	hour_start int,
	hour_end text,
	late_in text,
	early_out text,
	checkin_min text,
	checkin_max text,
	checkout_min text,
	checkout_max text)""")
curs.execute("""create table libur if not exist(ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
	tanggal text,
	hari text)""")
curs.execute("""create table log_absensi if not exist(ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
	NoPeg int not null,
	NoAkun int NOT NULL,
	Nama text,
	Auto-Assign int,
	Tanggal text,
	Jam_Kerja text,
	Awal_tugas text,
	Akhir_tugas text,
	Masuk_text,
	Keluar_text,
	Normal_int,
	Waktu_real int,
	Telat_text,
	Plg-Awal text,
	Bolos text,
	Waktu_Lembur text,
	Waktu_Kerja text,
	Status int,
	Hrs_CIn int,
	Hrs_COut int,
	Departemen text,
	NDays int,
	Akhir_Pekan int,
	Hari-Libur int,
	Lama_Hadir text,
	NDays_OT int,
	Lembur_A_Pekan int,
	Libur_Lembur int)""")

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
