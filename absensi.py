import random
import datetime
import os
import sys
import csv

#date time
date_start = datetime.date(2018,12,1)
date_finish = datetime.date(2018,12,10)
date_delta = (date_finish-date_start)
check_in = datetime.time(8,0,0)
check_in_normal = datetime.time(16,0,0)
check_in_weekend = datetime.time(8,0,0)

#header
header = 'NoPeg,No. Akun,No.,Nama,Auto-Assign,Tanggal,Jam Kerja,Awal tugas,Akhir tugas,Masuk,Keluar,Normal,Waktu real,Telat,Plg Awal,Bolos,Waktu Lembur,Waktu Kerja,Status,Hrs C/In,Hrs C/Out,Departemen,NDays,Akhir Pekan,Hari Libur,Lama Hadir,NDays_OT,Lembur A.Pekan,Libur Lembur'
title='F:/abs-{}.txt'.format(date_finish)
employee = [[1,1,1,'Ape'],[2,2,2,'Bull'],[3,3,3,'Cow'],[4,4,4,'Dog'],[5,5,5,'Elk'],[6,6,6,'Fowl']]

#data pegawai
nopeg = []
noakun = []
nomor = []
nama = []

for i in employee:
	nopeg.append(i[0])
	noakun.append(i[1])
	nomor.append(i[2])
	nama.append(i[3])

#tanggal & jam kerja
		

attend()
#misc
auto = ' '
status = ' '
hari_libur = ' '
libur_lembur = ' '