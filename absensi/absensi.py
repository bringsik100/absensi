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

'''modul database'''
def cnxn():
	'''menyambungkan ke data/report.db'''
	try:
		conn=db.connect('data/report.db')
		print('koneksi berhasil')	
	except Exception:
		print(f'koneksi gagal\n{sys.exc_info()} \n')
		pass

def user_sql():
	'''modul untuk menjalankan perintah SQL'''
	cnxn
	print(" masukkan perintah SQL disini\t:\n")
	sql = str(input())
	if ';' not in sql:
		sql=sql+';'
	try:
		conn.execute(sql)
	except Exception:
		print(f'gagal mengeksekusi "{sql}" karena :\n{sys.exc_info()}\n')

def view_tabel(nama_tabel):
	'''menampilkan isi tabel'''
	cnxn()
	try:
		curs=conn.execute(f'select * from {nama_tabel};')
		print(curs)
	except Exception:
		print(f'gagal menampilkan isi tabel karena :\n{sys.exc_info()}\n')

"""salam pembuka"""
print("""
SELAMAT DATANG DI ABTOMATIS
MODUL PENGISI ABSENSI OTOMATIS
""")

def main():
	"""fungsi utama, semua data diproses disini"""
	
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
	
	def this_output():
		"""memproses data dari penampung untuk di cetak ke layar atau berkas"""
		
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
	
	this_output()
	
	"""opsi ulangi proses"""
	print("\n\nulangi proses ?")
	answer = input("\n\njawab Y atau N: ")
	if answer.lower() == 'y':
		return main()
	else:
		sys.exit
	conn.close()

if __name__=='__main__':
	main()
