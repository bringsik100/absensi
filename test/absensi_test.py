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
+ deklarasi fungsi objek
- fungsi ambil data pegawai, jadwal, judul, liburan
- fungsi perubah input 
- fungsi tanggal
- fungsi waktu
- fungsi output
+ fungsi test_main()
- salam pembuka
- dict template penampung < pegawai < tanggal < waktu < data
- input pegawai
- input tanggal
- input waktu
- pilih format output
- ulangi atau selesai
"""

"""import library"""
from random import randint as ri
import datetime as dd
from datetime import datetime as dt
from datetime import timedelta as td
import string
import json
import csv
from openpyxl import Workbook
import pytest
import proses_test
import output_test
import pytest

"""salam pembuka"""
print("""
SELAMAT DATANG DI ABTOMATIS
MODUL PENGISI ABSENSI OTOMATIS
""")

def test_main():
	"""fungsi utama, semua data diproses disini"""
	print("""
	metode pengisian :
	masukkan tanggal awal dan akhir dengan format YYYY-MM-DD dimana 
	YYYY = 4 angka tahun
	MM = 2 angka bulan 
	DD = 2 angka tanggal
	""")
	
	"""tanya tanggal awal dan akhir otomatis"""
	awal = proses_test._get_input(' masukkan tanggal awal absensi: ') 
	akhir = proses_test._get_input(' masukkan tanggal akhir absensi: ')
	hasil = []
	
	"""main proses"""
	"""proses ada di dalam modul proses"""
	proses_test.test_process(awal,akhir,hasil)
	
	def test_this_output():
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
		opsi = input (" opsi : ")
		
		if int(opsi) == 0:
			"""cetak ke layar"""
			output_test.test_pt_screen(hasil)
		
		elif int(opsi) == 1:
			"""cetak ke excell"""
			judul_opsi = input("beri judul : " )
			if judul_opsi == None:
				judul_blank = dt.today.strftime('%Y-%m-%d-%H.%M.%s')
				ouput_test.test_pt_excell(judul_blank,hasil)
			else:
				ouput_test.test_pt_excell(judul_opsi,hasil)
		
		elif int(opsi) == 2:
			"""cetak ke JSON"""
			judul_opsi = input("beri judul : " )
			if judul_opsi == None:
				judul_blank = dt.today.strftime('%Y-%m-%d-%H.%M.%s')
				ouput_test.test_pt_json(judul_blank,hasil)
			else:
				ouput_test.test_pt_json(judul_opsi,hasil)
		
		elif int(opsi) == 3:
			"""cetak ke csv"""
			judul_opsi = input("beri judul : " )
			if judul_opsi == None:
				judul_blank = dt.today.strftime('%Y-%m-%d-%H.%M.%s')
				ouput_test.test_pt_csv(judul_blank,hasil)
			else:
				ouput_test.test_pt_csv(judul_opsi,hasil)
		
		elif int(opsi) == 4:
			"""cetak ke text"""
			judul_opsi = input("beri judul : " )
			if judul_opsi == None:
				judul_blank = dt.today.strftime('%Y-%m-%d-%H.%M.%s')
				ouput_test.test_pt_txt(judul_blank,hasil)
			else:
				ouput_test.test_pt_txt(judul_opsi,hasil)
		else:
			"""opsi diluar batas"""
			print("\n"+"pilihan anda tidak ada dalm daftar \n\n ulangi lagi?")
			
			answer = input("\n\njawab Y atau N: ")
			if answer.lower() == 'y':
				return test_this_output()
			else:
				pass
	
	test_this_output()
	
	"""opsi ulangi proses"""
	print("\n\nulangi proses ?")
	answer = input("\n\njawab Y atau N: ")
	if answer.lower() == 'y':
		return test_main()
	else:
		pass

if __name__=='__main__':
	test_main()
