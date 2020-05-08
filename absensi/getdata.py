#!/usr/bin/env python3
"""
Data
"""

"""
import library
"""
from datetime import datetime as dt
from datetime import timedelta as td
import sqlite3 as db
import sys
import os
from proses import process

"""
TODO:
- modul untuk menampilkan dan menyunting data pegawai
- modul untuk menampilkan dan menyunting jadwal
- modul untuk menampilkan dan menyunting liburan
"""

'''modul database'''

def cnxn():
	'''menyambungkan ke data/report.db'''
	try:
		conn=db.connect('data/report.db')
		print('koneksi berhasil')	
	except Exception:
		print(f'koneksi gagal\n{sys.exc_info()} \n')
		pass
	def tab_pegawai():
		try:
			conn.execute('''create table if not exist pegawai(
			noID integer primary key autoincrement
			,nopeg text
			,noakun text
			,nokartu text
			,nama text
			,titel text
			,departemen text)
			''')
			conn.commit()
			print('tabel pegawai berhasil dibuat')
		except Exception:
			print(f'tabel pegawai gagal dibuat karena:\n{sys.exc_info()} \n') 
	
	def tab_jadwal():
		try:
			conn.execute('''create table if not exist jadwal(
			noID integer primary key autoincrement
			,nama text
			,`Jam Masuk` text
			,`Jam Keluar` text
			,`Telat` text
			,`Pulang Cepat` text
			,`Harus CIn` text
			,`Harus COut` text
			,`Normal` text
			,`Akhir Pekan` text
			,`Hari Libur` text
			,`Waktu Real` text)
			''')
			conn.commit()
			print('tabel jadwal berhasil dibuat')
		except Exception:
			print(f'tabel jadwal gagal dibuat karena:\n{sys.exc_info()} \n')
	def tab_pegawai():
		try:
			conn.execute('''create table if not exist liburan(
			tanggal text
			,hari text)
			''')
			conn.commit()
			print('tabel liburan berhasil dibuat')
		except Exception:
			print(f'tabel liburan gagal dibuat karena:\n{sys.exc_info()} \n') 
	
	def create_table():
		try:
			"""buat table baru di database"""
			conn = db.connect("data/report.db")
			conn.execute("""create table if not exists absensi (row_id integer primary key autoincrement
			,`NoPeg` text
			,`No. Akun` text
			,`No.` text
			,`Nama` text
			,`Auto-Assign` text
			,`Tanggal` text
			,`Jam Kerja` text
			,`Awal tugas` text
			,`Akhir tugas` text
			,`Masuk` text
			,`Keluar` text
			,`Normal` text
			,`Waktu real` text
			,`Telat` text
			,`Plg Awal` text
			,`Bolos` text
			,`Waktu Lembur` text
			,`Waktu Kerja` text
			,`Status` text
			,`Hrs C/In` text
			,`Hrs C/Out` text
			,`Departemen` text
			,`NDays` text
			,`Akhir Pekan` text
			,`Hari Libur` text
			,`Lama Hadir` text
			,`NDays_OT` text
			,`Lembur A.Pekan` text
			,`Libur Lembur` text);""")
			conn.commit()
			print('tabel liburan berhasil dibuat')
		except Exception:
			print(f'tabel liburan gagal dibuat karena:\n{sys.exc_info()} \n') 
	
	conn.close()

def main():
	cnxn()
	pass
	
if __name__ == '__main__':
	main()
