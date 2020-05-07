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

conn = db.connect("data/report.db")
curs = conn.cursor()

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

pro = process
hasil = []
pro(dt(2020,1,1,0,0,0),dt(2020,12,31,0,0,0), hasil)
items = []

for rows in hasil:
	litems = list(rows.values())
	conn.execute(f'''insert into absensi(
`NoPeg`
,`No. Akun`
,`No.`
,`Nama`
,`Auto-Assign`
,`Tanggal`
,`Jam Kerja`
,`Awal tugas`
,`Akhir tugas`
,`Masuk`
,`Keluar`
,`Normal`
,`Waktu real`
,`Telat`
,`Plg Awal`
,`Bolos`
,`Waktu Lembur`
,`Waktu Kerja`
,`Status`
,`Hrs C/In`
,`Hrs C/Out`
,`Departemen`
,`NDays`
,`Akhir Pekan`
,`Hari Libur`
,`Lama Hadir`
,`NDays_OT`
,`Lembur A.Pekan`
,`Libur Lembur`)
 values("{litems[0]}"
,"{litems[1]}"
,"{litems[2]}"
,"{litems[3]}"
,"{litems[4]}"
,"{litems[5]}"
,"{litems[6]}"
,"{litems[7]}"
,"{litems[8]}"
,"{litems[9]}"
,"{litems[10]}"
,"{litems[11]}"
,"{litems[12]}"
,"{litems[13]}"
,"{litems[14]}"
,"{litems[15]}"
,"{litems[16]}"
,"{litems[17]}"
,"{litems[18]}"
,"{litems[19]}"
,"{litems[20]}"
,"{litems[21]}"
,"{litems[22]}"
,"{litems[23]}"
,"{litems[24]}"
,"{litems[25]}"
,"{litems[26]}"
,"{litems[27]}"
,"{litems[28]}");''')
conn.commit()
conn.close()

def main():
	pass
if __name__ == '__main__':
	main()
