#!/usr/bin/env python3
"""
Absensi
"""

__author__ = "bringsik100"
__version__ = "0.1.3b"
__license__ = "MIT"

"""
alur program
+ import library
+ modul data
- koneksi ke database
- lihat / sunting tabel pegawai,jadwal,liburan
+ modul laporan
- lihat / sunting laporan
+ modul output
- output ke excel / database
+ fungsi main()
"""

"""import library"""
from random import randint as ri
import datetime as dd
from datetime import datetime as dt
from datetime import timedelta as td
import sqlite3 as db
import string
import sys
import json
import csv
from openpyxl import Workbook
import proses 
import output
import getdata

'''modul database'''

cnxn = getdata.DataBase('data/report.db')

def user_sql():
	'''modul untuk menjalankan perintah SQL'''
	print(" masukkan perintah SQL disini\t:\n ;")
	sql = str(input())
	try:
		conn.execute(sql)
	except Exception:
		print(f'gagal mengeksekusi "{sql}" karena :\n{sys.exc_info()}\n')

def view(nama_tabel):
	'''menampilkan isi tabel'''
	try:
		cnxn
		curs = cnxn.cursor
		rows = curs.execute(f'select * from {nama_tabel};').fetchall()
		print(rows)
	except Exception:
		print(f'gagal menampilkan isi tabel karena :\n{sys.exc_info()}\n')

def buat():
	"""modul untuk mengisi absen otomatis"""
	cls()
	print("""
		metode pengisian :
		masukkan tanggal awal dan akhir dengan format YYYY-MM-DD dimana 
		YYYY = 4 angka tahun
		MM = 2 angka bulan 
		DD = 2 angka tanggal
	""")
	
	"""tanya tanggal awal dan akhir otomatis"""
	awal = proses.get_input(' masukkan tanggal awal absensi: ') 
	akhir = proses.get_input(' masukkan tanggal akhir absensi: ')
	hasil = []
	
	"""main proses"""
	"""proses ada di dalam modul proses"""
	proses.process(awal,akhir,hasil)
	"""otomatis menyimpan ke database"""
	try:
		output.pt_db(hasil)		
	except Exception:
		print(f"gagal menyimpan ke database karena : \n{Exception}\n")
		print(f"laporan dari system : \n{sys.exc_info()}")
	return hasil

def cetak():
	"""memproses data dari penampung untuk di cetak ke layar atau berkas"""
	
	cls()
	print("""
	pilih format output dari 5 opsi
	 0 = layar
	 1 = excel
	 2 = JSON
	 3 = csv
	 4 = text
	""")
	"""pilih opsi output"""
	opsi = str(input (" opsi : "))
	
	if opsi =='0':
		"""cetak ke layar"""
		output.pt_screen(hasil)
	
	elif opsi == '1':
		"""cetak ke excell"""
		judul_opsi = input("beri judul : " )
		if judul_opsi == None:
			judul_blank = dt.today.strftime('%Y-%m-%d-%H.%M.%s')
			ouput.pt_excell(judul_blank,hasil)
		else:
			ouput.pt_excell(judul_opsi,hasil)
		
	elif opsi == '2':
		"""cetak ke JSON"""
		judul_opsi = input("beri judul : " )
		if judul_opsi == None:
			judul_blank = dt.today.strftime('%Y-%m-%d-%H.%M.%s')
			ouput.pt_json(judul_blank,hasil)
		else:
			ouput.pt_json(judul_opsi,hasil)
		
	elif 'opsi' == '3':
		"""cetak ke csv"""
		judul_opsi = input("beri judul : " )
		if judul_opsi == None:
			judul_blank = dt.today.strftime('%Y-%m-%d-%H.%M.%s')
			ouput.pt_csv(judul_blank,hasil)
		else:
			ouput.pt_csv(judul_opsi,hasil)
	
	elif opsi == '4':
		"""cetak ke text"""
		judul_opsi = input("beri judul : " )
		if judul_opsi == None:
			judul_blank = dt.today.strftime('%Y-%m-%d-%H.%M.%s')
			ouput.pt_txt(judul_blank,hasil)
		else:
			ouput.pt_txt(judul_opsi,hasil)
	else:
		"""opsi diluar batas"""
		print("\n"+"pilihan anda tidak ada dalm daftar \n\n ulangi lagi?")
	
		answer = input("\n\njawab Y atau N: ")
		if answer.lower() == 'y':
			return this_output()
		else:
			pass

def cls():
	"""modul untuk membersihkan layar"""
	import os
	os.system('cls' if os.name == 'nt' else 'clear')

def keluar():
	"""modul untuk keluar"""
	print('Terima Kasih')
	sys.exit

def ulang():
	"""opsi ulangi proses"""
	print("\n\nulangi proses ?")
	answer = input("\n\njawab Y atau N: ")
	if answer.lower() == 'y':
		return main()
	else:
		keluar()

def main():
	"""fungsi utama, semua data diproses disini"""
	"""salam pembuka"""
	cls()
	print("""
	SELAMAT DATANG DI ABTOMATIS
	MODUL PENGISI ABSENSI OTOMATIS
	""")
	"""modul menu"""
	def menu():
		print("""
1 - lihat data laporan        2 - lihat data pegawai
3 - lihat data jadwal         4 - lihat data liburan
O - ubah / hapus data laporan P - ubah / hapus data pegawai
J - ubah / hapus data jadwal  L - ubah / hapus data liburan
B - buat laporan otomatis     C - cetak laporan
M - lihat opsi \t\t Q - keluar
		""")
	
	def opsi_input():
		menu()
		opsi = str(input("pilih opsi :\t"))
		if opsi.lower() == '1': # lihat data laporan
			view('laporan')
			opsi_input()
		elif opsi.lower() == '2': # lihat data pegawai
			view('pegawai')
			cls()
			opsi_input()
		elif opsi.lower() == '3': # lihat data jadwal
			view('jadwal')
			cls()
			opsi_input()
		elif opsi.lower() == '4': # lihat data liburan
			view('libur')
			opsi_input()
		elif opsi.lower() == 'o': # ubah data laporan
			pass
		elif opsi.lower() == 'p': # ubah data pegawai
			this_menu = getdata.Ubah('data/report.db','pegawai')
			this_menu.column = ['nopeg','noakun','nokartu','nama','titel','departemen']
			this_menu.menu()
			opsi_input()
		elif opsi.lower() == 'j': # ubah data jadwal
			this_menu = getdata.Ubah('data/report.db','jadwal')
			this_menu.column = ['nama','`Jam Masuk`','`Jam Keluar`','`Telat,`Pulang Cepat`','`Harus CIn`','`Harus COut`','`Normal`','`Akhir Pekan`','`Hari Libur`','`Waktu Real`']
			this_menu.menu()
			opsi_input()
		elif opsi.lower() == 'l': # ubah data liburan
			this_menu = getdata.Ubah('data/report.db','liburan')
			this_menu.column = ['tanggal text','hari text']
			opsi_input()
		elif opsi.lower() == 'b': # buat laporan otomatis
			cls()
			buat()
			opsi_input()
		elif opsi.lower() == 'c': # cetak laporan
			cls()
			cetak()
			opsi_input()
		elif opsi.lower() == 'q': # keluar
			cls()
			keluar()
		elif opsi.lower() == 'm': # lihat menu
			cls()
			opsi_input()
		else: # opsi tidak dikenali
			print(f'opsi {opsi} tidak ditemukan, ulangi?\n')
			ulang()
	
	opsi_input()

if __name__=='__main__':
	main()
