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
def create_table():
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
	conn.close()

def main():
	pass
	
if __name__ == '__main__':
	main()
