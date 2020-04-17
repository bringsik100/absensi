import random
import datetime

#header
header = 'NoPeg,No. Akun,No.,Nama,Auto-Assign,Tanggal,Jam Kerja,Awal tugas,Akhir tugas,Masuk,Keluar,Normal,Waktu real,Telat,Plg Awal,Bolos,Waktu Lembur,Waktu Kerja,Status,Hrs C/In,Hrs C/Out,Departemen,NDays,Akhir Pekan,Hari Libur,Lama Hadir,NDays_OT,Lembur A.Pekan,Libur Lembur'.replace(',','\t')

#misc
''' Auto-Assign, Status, Hari Libur, Libur Lembur is empty'''
empty = ' '
norm_tab = '\"1'

#employee
employee = [['1','1','1','Ape','SSI'],
			['2','2','2','Bull','SSI'],
			['3','3','3','Cow','SSI'],
			['4','4','4','Dog','SSI'],
			['5','5','5','Elk','SSI'],
			['6','6','6','Fowl','SSI']]

nopeg = []
noakun = []
nomor = []
nama = []
departemen = []

for i in employee:
	nopeg.append(i[0])
	noakun.append(i[1])
	nomor.append(i[2])
	nama.append(i[3])
	departemen.append(i[4])

#date time
date_start = datetime.date(2018,12,1)
date_finish = datetime.date(2018,12,10)
date_delta = (date_finish-date_start)
dates = []
date_check_in = []
date_check_out = []
date_hour_in = []
date_hour_out = []
n_days = []
w_days = []

for i in range(date_delta.days+1):
	x = date_start+datetime.timedelta(days=i)
	dates.append(x)
	
	hour_in = datetime.time(8,0,0)
	hour_out = [datetime.time(16,0,0),datetime.time(13,0,0)]
	hour_off = datetime.time(0,0,0)
	cin = random.randint(7,8)
	cot = [random.randint(16,18),random.randint(15,18)]
	
	if x.weekday() == 6:
		n_days.append(' ')
		w_days.append('\"1')
		date_hour_in.append(datetime.datetime.combine(x,hour_off))
		date_hour_out.append(datetime.datetime.combine(x,hour_off))
		date_check_in.append(datetime.datetime.combine(x,hour_off))
		date_check_out.append(datetime.datetime.combine(x,hour_off))
	elif x.weekday() == 5:
		n_days.append('\"1')
		w_days.append(' ')
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
		n_days.append('\"1')
		w_days.append(' ')
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

#total attendance
	total_att = []

	for i in range(len(date_check_in)):
		xx = date_check_out[i] - date_check_in[i]
		total_att.append(xx)

#title
#title='F:/abs-{}.txt'.format(date_finish)

#shift
	shift_list = ['Senin-Jumat','Sabtu-Minggu']
	sched_shift = []

	for i in dates:
		if i.weekday() == 5 or 6:
			sched_shift.append(shift_list[1])
		else:
			sched_shift.append(shift_list[0])

#normal column, real time column, & day out
	time_real = []
	day_out = []

	for i in date_check_in:
		if i.hour == 0:
			time_real.append(empty)
			day_out.append('\"True\"')
		else:
			time_real.append('\"1')
			day_out.append(empty)

#late & overtime check in
cin_late = []
cin_over = []

for i in range(len(date_check_in)):
	if date_hour_in[i] < date_check_in[i]:
		x = date_check_in[i] - date_hour_in[i]
		cin_late.append(x)
		cin_over.append(datetime.timedelta(0,0,0))
	elif date_hour_in[i] > date_check_in[i]:
		x = date_hour_in[i] - date_check_in[i]
		cin_late.append(datetime.timedelta(0,0,0))
		cin_over.append(x)
	else:
		cin_late.append(datetime.timedelta(0,0,0))
		cin_over.append(datetime.timedelta(0,0,0))

#early & overtime check out
cot_early = [] 
cot_over = []

for i in range(len(date_check_out)):
	if date_hour_out[i] > date_check_out[i]:
		x = date_hour_out[i] - date_check_out[i]
		cot_early.append(x)
		cot_over.append(datetime.timedelta(0,0,0))
	elif date_hour_out[i] > date_check_out[i]:
		x = date_check_out[i] - date_hour_out[i]
		cot_early.append(datetime.timedelta(0,0,0))
		cot_over.append(x)
	else:
		cot_early.append(datetime.timedelta(0,0,0))
		cot_over.append(datetime.timedelta(0,0,0))

#total overtime
total_over = []

for i in range(len(cin_over)):
	x = cin_over[i]+cot_over[i]
	total_over.append(x)

#work time
work_hour = []

for i in range(len(date_hour_in)):
	x = date_hour_out[i] - date_hour_in[i]
	y = x-(cin_late[i]-cot_early[i])
	work_hour.append(y)

#hrs check in, hrs check out, & departemen value

t_val = '\"True\"'

#printing result
print(header)
for i in range(len(employee)):
	print('\n')
	for x in range(len(dates)):
		print('{0}\t{1}\t{2}\t{3}\t{4}\t{5}\t{6}\t{7}\t{8}\t{9}\t{10}\t{11}\t{12}\t{13}\t{14}\t{15}\t{16}\t{17}\t{18}\t{19}\t{20}\t{21}\t{22}\t{23}\t{24}\t{25}\t{26}\t{27}\t{28}'.format(nopeg[i],
		noakun[i],nomor[i],nama[i],empty,dates[x].isoformat(),sched_shift[i],date_hour_in[i].strftime('%H:%M'),date_hour_out[i].strftime('%H:%M'),date_check_in[i].strftime('%H:%M'),date_check_out[i].strftime('%H:%M'),norm_tab,time_real[i],cin_late[i],cot_early[i],
		day_out[i],total_over[i],work_hour[i],empty,t_val,t_val,departemen[i],n_days[i],w_days[i],empty,total_att[i],empty,empty,empty))
	
