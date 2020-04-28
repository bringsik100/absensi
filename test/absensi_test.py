#!/usr/bin/env python3
"""
Absensi
"""

__author__ = "bringsik100"
__version__ = "0.1.3b"
__license__ = "MIT"

from random import randint as ri
import datetime as dd
from datetime import datetime as dt
from datetime import timedelta as td
import string
import json
from openpyxl import Workbook
import test.proses_test
import test.pegawai_test
from test.output_test import test_out_put as out_p
import pytest

"""
alur program\
- salam pembuka
- tanya tanggal awal
- tanya tanggal akhir
- proses absensi
- pilih format output
- ulangi atau selesai
"""

"""salam pembuka"""
print("""
SELAMAT DATANG DI ABTOMATIS
MODUL PENGISI ABSENSI OTOMATIS
""")

"""tanya tanggal awal dan akhir"""
print("""
metode pengisian :
masukkan tanggal awal dan akhir dengan format YYYY-MM-DD dimana 
YYYY = 4 angka tahun
MM = 2 angka bulan 
DD = 2 angka tanggal
""")

"""fungsi untuk merubah input yang berformat string menjadi datetime"""
def getd(arg):
	x = input(arg )
	return dt.strptime(x,'%Y-%m-%d')

'''tanya tanggal awal dan akhir'''
mulai = dt(2020,10,10,0) #getd(' masukkan tanggal awal absensi: ')
akhir = dt(2020,10,20,0) #getd(' masukkan tanggal akhir absensi: ')

test.test_datecount(mulai,akhir)
test.test_proses()

if __name__=='__main__':
	main()
