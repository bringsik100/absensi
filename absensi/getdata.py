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
'''
fungsi untuk create, read, write, edit, dan delete item dalam absensi.d
'''
'''connect ke database'''

"""
def cnxn(expr):
	'''connect ke database dan membuat cursor, output berupa list'''
	conn = db.connect("data/report.db")
	cursor = conn.execute(expr)
	try:
		conn.execute(expr)
		print(f'eksekusi : {expr} berhasil')
		return cursor
	except Exception:
		conn.close()
		print(f' eksekusi gagal!\n{sys.exc_info()}\n')"""

"""
pegawai = cnxn("select USERID,Badgenumber,SSN,Name,INLATE,OUTEARLY,OVERTIME from userinfo;")#0-4
depart = cnxn("select DEPTID,DEPTNAME from departments;")#2
jadwal = cnxn("select SCHCLASSID,SCHNAME,STARTTIME,ENDTIME,LATEMINUTES,EARLYMINUTES,CHECKIN,CHECKOUT,WorkDay,WorkMins from schclass;")
liburan = cnxn("select HOLIDAYID,HOLIDAYNAME,HOLIDAYYEAR,HOLIDAYMONTH,HOLIDAYDAY from holidays;")
checkin = cnxn("select USERID,CHECKTIME,CHECKTYPE from checkinout;")
checkout = cnxn("select USERID,CHECKTIME,CHECKTYPE from checkinout;")
checkex = cnxn("select EXACTID,USERID,CHECKTIME,CHECKTYPE,ISADD,ISMODIFY,ISDELETE,MODIFYBY,DATE from checkexact;")
parameter = cnxn("select PARANAME,PARATYPE,PARAVALUE from attparam;")
systemlog = cnxn("select ID,Operator,LogTime,MachineAlias from systemlog;")
print('\n')"""

header = ("NoPeg","No. Akun","No.","Nama","Auto-Assign","Tanggal","Jam Kerja","Awal tugas","Akhir tugas"
,"Masuk","Keluar","Normal","Waktu real","Telat","Plg Awal","Bolos","Waktu Lembur","Waktu Kerja","Status"
,"Hrs C/In","Hrs C/Out","Departemen","NDays","Akhir Pekan","Hari Libur","Lama Hadir","NDays_OT"
,"Lembur A.Pekan","Libur Lembur")

pro = process
hasil = []
pro(dt(2020,1,1,0,0,0),dt(2020,12,31,0,0,0),hasil)

conn = db.connect("data/report.db")
curs = conn.cursor()

for row in hasil:
	curs.execute("""insert into absensi(NoPeg
	,NoAkun
	,No
	,Nama
	,Auto_Assign
	,Tanggal
	,Jam_Kerja
	,Awal_tugas
	,Akhir_tugas
	,Masuk
	,Keluar
	,Normal
	,Waktu
	,Telat
	,Plg_Awal
	,Bolos
	,Waktu_Lembur
	,Waktu_Kerja
	,Status
	,Hrs_CIn
	,Hrs_COut
	,Departemen
	,NDays
	,Akhir_Pekan
	,Hari_Libur
	,Lama_Hadir
	,NDays_OT
	,Lembur_APekan
	,Libur_Lembur)
	 values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)""",row)

def main():
	pass
if __name__ == '__main__':
	main()
