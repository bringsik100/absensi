#!/usr/bin/env python3
"""
Absensi
"""

__author__ = "bringsik100"
__version__ = "0.1.3"
__license__ = "MIT"

from random import randint as ri
import datetime as dd
from datetime import datetime as dt
from datetime import timedelta as td
import string
import json
from openpyxl import Workbook
import test.attend_test
import test.employee_test
from test.output_test import test_out_put as out_p
import pytest

"""
alur program
- tanya tanggal awal
- tanya tanggal akhir
- proses absensi
- pilih output
"""
print("""
SELAMAT DATANG DI ABTOMATIS
MODUL PENGISI ABSENSI OTOMATIS
""")


print("""
metode pengisian :
masukkan tanggal awal dan akhir dengan format YYYY-MM-DD dimana 
YYYY = 4 angka tahun
MM = 2 angka bulan 
DD = 2 angka tanggal
""")
def getd(arg):
	x = input(arg )
	return dt.strptime(x,'%Y-%m-%d')

mulai = dt(2020,10,10,0) #getd(' masukkan tanggal awal absensi: ')
akhir = dt(2020,10,20,0) #getd(' masukkan tanggal akhir absensi: ')

jadwal = test.attend_test.test_datecount(mulai,akhir)

waktu = test.attend_test.test_timecount

daftar_peg = test.employee_test.test_source_emp.test_read()

def ngetes(*args):
	for i in args:
		print(i)

for pegawai in daftar_peg:

	for tanggal in jadwal.dates:
	
		if tanggal.weekday == 6:
			jam_masuk = td(0)
			jam_keluar = td(0)
			cek_masuk = td(0)
			cek_keluar = td(0)
		
			waktu(jam_masuk,jam_keluar,cek_masuk,cek_keluar)
			
			ngetes(waktu.hour_in
				,waktu.hour_out
				,waktu.check_in
				,waktu.check_out)
	
		elif tanggal.weekday == 5:
			jam_masuk = td(hours=8)
			jam_keluar = td(hours=15)
			cek_masuk = td(hours = ri(7,9), minutes = ri(0,59), seconds = ri(0,59))
			cek_keluar = td(hours = ri(14,18), minutes = ri(0,59), seconds = ri(0,59))
		
			waktu(jam_masuk,jam_keluar,cek_masuk,cek_keluar)
			ngetes(waktu.hour_in
				,waktu.hour_out
				,waktu.check_in
				,waktu.check_out)
	
		else:
			jam_masuk = td(hours=8)
			jam_keluar = td(hours=16)
			cek_masuk = td(hours = ri(7,9), minutes = ri(0,59), seconds = ri(0,59))
			cek_keluar = td(hours = ri(14,18), minutes = ri(0,59), seconds = ri(0,59))
		
			waktu(jam_masuk,jam_keluar,cek_masuk,cek_keluar)
			ngetes(waktu.hour_in
				,waktu.hour_out
				,waktu.check_in
				,waktu.check_out)