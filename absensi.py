import random
import datetime

#header
header = 'NoPeg,No. Akun,No.,Nama,Auto-Assign,Tanggal,Jam Kerja,Awal tugas,Akhir tugas,Masuk,Keluar,Normal,Waktu real,Telat,Plg Awal,Bolos,Waktu Lembur,Waktu Kerja,Status,Hrs C/In,Hrs C/Out,Departemen,NDays,Akhir Pekan,Hari Libur,Lama Hadir,NDays_OT,Lembur A.Pekan,Libur Lembur'

#date time
date_start = datetime.date(2018,12,1)
date_finish = datetime.date(2018,12,10)
date_delta = (date_finish-date_start)
dates = []
date_check_in = []
date_check_out = []
date_hour_in = []
date_hour_out = []

for i in range(date_delta.days+1):
	x = date_start+datetime.timedelta(days=i)
	dates.append(x)
	
	hour_in = datetime.time(8,0,0)
	hour_out = [datetime.time(16,0,0),datetime.time(13,0,0)]
	hour_off = datetime.time(0,0,0)
	cin = random.randint(7,8)
	cot = [random.randint(16,18),random.randint(15,18)]
	
	if x.weekday() == 6:
		date_hour_in.append(datetime.datetime.combine(x,hour_off))
		date_hour_out.append(datetime.datetime.combine(x,hour_off))
		date_check_in.append(datetime.datetime.combine(x,hour_off))
		date_check_out.append(datetime.datetime.combine(x,hour_off))
	elif x.weekday() == 5:
		date_hour_in.append(datetime.datetime.combine(x,hour_in))
		date_hour_out.append(datetime.datetime.combine(x,hour_out[1]))
		
		if cin == 8:
			check_in = datetime.time(cin,random.randint(0,15))
			check_out = datetime.time(cot[1],random.randint(0,59))
		else:
			check_in = datetime.time(cin,random.randint(45,59))
			check_out = datetime.time(cot[0],random.randint(0,59))
		date_check_in.append(datetime.datetime.combine(x,check_in))
		date_check_out.append(datetime.datetime.combine(x,check_out))

	else:
		date_hour_in.append(datetime.datetime.combine(x,hour_in))
		date_hour_out.append(datetime.datetime.combine(x,hour_out[0]))
		
		if cin == 8:
			check_in = datetime.time(cin,random.randint(0,15))
			check_out = datetime.time(cot[1],random.randint(0,59))
		else:
			check_in = datetime.time(cin,random.randint(45,59))
			check_out = datetime.time(cot[0],random.randint(0,59))
		date_check_in.append(datetime.datetime.combine(x,check_in))
		date_check_out.append(datetime.datetime.combine(x,check_out))

#title
title='F:/abs-{}.txt'.format(date_finish)

#employee
employee = [[1,1,1,'Ape'],[2,2,2,'Bull'],[3,3,3,'Cow'],[4,4,4,'Dog'],[5,5,5,'Elk'],[6,6,6,'Fowl']]

nopeg = []
noakun = []
nomor = []
nama = []

for i in employee:
	nopeg.append(i[0])
	noakun.append(i[1])
	nomor.append(i[2])
	nama.append(i[3])

#misc
auto = ' '
status = ' '
hari_libur = ' '
libur_lembur = ' '
