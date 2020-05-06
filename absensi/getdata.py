#!/usr/bin/env python3
"""
Data
"""

"""
daftar nama tabel

USERINFO	= data pegawai
DEPARTMENTS	= daftar departemen
SCHCLASS	= jadwal kerja
HOLIDAYS	= daftar hari libur
CHECKINOUT	= log absensi
CHECKEXACT	= validasi absensi
ATTPARAM	= parameter/peraturan absen
SystemLog	= log system

import library
"""
from datetime import datetime as dt
from datetime import timedelta as td
import sqlite3 as db
import sys
import os

'''
fungsi untuk create, read, write, edit, dan delete item dalam absensi.d
'''
'''connect ke database'''

def cnxn(expr):
	'''connect ke database dan membuat cursor, output berupa list'''
	conn = db.connect("data/absensi.sqlite")
	cursor = conn.execute(expr)
	try:
		conn.execute(expr)
		print(f'eksekusi : {expr} berhasil')
		return cursor
	except Exception:
		conn.close()
		print(f' eksekusi gagal!\n{sys.exc_info()}\n')

pegawai = cnxn("select USERID,Badgenumber,SSN,Name,INLATE,OUTEARLY,OVERTIME from userinfo;")#0-4
depart = cnxn("select DEPTID,DEPTNAME from departments;")#2
jadwal = cnxn("select SCHCLASSID,SCHNAME,STARTTIME,ENDTIME,LATEMINUTES,EARLYMINUTES,CHECKIN,CHECKOUT,WorkDay,WorkMins from schclass;")
liburan = cnxn("select HOLIDAYID,HOLIDAYNAME,HOLIDAYYEAR,HOLIDAYMONTH,HOLIDAYDAY from holidays;")
checkin = cnxn("select USERID,CHECKTIME,CHECKTYPE from checkinout;")
checkout = cnxn("select USERID,CHECKTIME,CHECKTYPE from checkinout;")
checkex = cnxn("select EXACTID,USERID,CHECKTIME,CHECKTYPE,ISADD,ISMODIFY,ISDELETE,MODIFYBY,DATE from checkexact;")
parameter = cnxn("select PARANAME,PARATYPE,PARAVALUE from attparam;")
systemlog = cnxn("select ID,Operator,LogTime,MachineAlias from systemlog;")
print('\n')

header = ("NoPeg","No. Akun","No.","Nama","Auto-Assign","Tanggal","Jam Kerja","Awal tugas","Akhir tugas"
,"Masuk","Keluar","Normal","Waktu real","Telat","Plg Awal","Bolos","Waktu Lembur","Waktu Kerja","Status"
,"Hrs C/In","Hrs C/Out","Departemen","NDays","Akhir Pekan","Hari Libur","Lama Hadir","NDays_OT"
,"Lembur A.Pekan","Libur Lembur")

for i in pegawai:
	print(list(i))

def main():
	pass
if __name__ == '__main__':
	main()
