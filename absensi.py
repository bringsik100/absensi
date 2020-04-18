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

nopeg = [i[0] for i in employee]
noakun = [i[1] for i in employee]
nomor = [i[2] for i in employee]
nama = [i[3] for i in employee]
departemen = [i[4] for i in employee]

#date time
date_start = datetime.date(2020,1,1)
date_finish = datetime.date(2020,3,31)
date_delta = (date_finish-date_start)
date_list = [date_start+datetime.timedelta(days=i) for i in range(date_delta.days+1)]
hour_in = datetime.time(8,0,0)
hour_out = [datetime.time(16,0,0),datetime.time(13,0,0)]
hour_off = datetime.time(0,0,0)
cin = random.randint(7,8)
cot = [random.randint(16,18),random.randint(15,18)]

def dates(a)
	#a is a date_list
	c_in = []
	c_out = []
	h_in = []
	h_out = []
	n_days = []
	w_days = []
	for i in range(a):
		if i.weekday() == 6:
			n_days.append(' ')
			w_days.append('\"1')
			h_in.append(datetime.datetime.combine(i,hour_off))
			h_out.append(datetime.datetime.combine(i,hour_off))
			c_in.append(datetime.datetime.combine(i,hour_off))
			c_out.append(datetime.datetime.combine(i,hour_off))
		elif x.weekday() == 5:
			n_days.append('\"1')
			w_days.append(' ')
			h_in.append(datetime.datetime.combine(i,hour_in))
			h_out.append(datetime.datetime.combine(i,hour_out[1]))
		
			if cin == 8:
				check_in = datetime.time(cin,random.randint(0,15))
				check_out = datetime.time(cot[1],random.randint(0,59))
			else:
				check_in = datetime.time(cin,random.randint(45,59))
				check_out = datetime.time(cot[0],random.randint(0,59))
			c_in.append(datetime.datetime.combine(i,check_in))
			c_out.append(datetime.datetime.combine(i,check_out))

		else:
			n_days.append('\"1')
			w_days.append(' ')
			h_in.append(datetime.datetime.combine(i,hour_in))
			h_out.append(datetime.datetime.combine(i,hour_out[0]))
		
			if cin == 8:
				check_in = datetime.time(cin,random.randint(0,15))
				check_out = datetime.time(cot[1],random.randint(0,59))
			else:
				check_in = datetime.time(cin,random.randint(45,59))
				check_out = datetime.time(cot[0],random.randint(0,59))
			c_in.append(datetime.datetime.combine(i,check_in))
			c_out.append(datetime.datetime.combine(i,check_out))

	#total attendance
	t_att = []
	for x in range(len(date_check_in)):
		xx = c_out[x] - c_in[x]
		t_att.append(xx)

	#shift
	shift_l = ['Senin-Jumat','Sabtu-Minggu']
	s_shift = []

	for x in a:
		if x.weekday() == 5 or 6:
			s_shift.append(shift_l[1])
		else:
			s_shift.append(shift_l[0])

	#normal column, real time column, & day out
	t_real = []
	d_out = []

	for x in c_in:
		if i.hour == 0:
			t_real.append(empty)
			d_out.append('\"True\"')
		else:
			t_real.append('\"1')
			d_out.append(empty)

	#late & overtime check in
	cin_late = []
	cin_over = []

	for X in range(len(c_in)):
		if h_in[x] < c_in[x]:
			y = c_in[x] - h_in[x]
			cin_late.append(y)
			cin_over.append(datetime.timedelta(0,0,0))
		elif h_in[x] > c_in[x]:
			y = h_in[x] - c_in[x]
			cin_late.append(datetime.timedelta(0,0,0))
			cin_over.append(y)
		else:
			cin_late.append(datetime.timedelta(0,0,0))
			cin_over.append(datetime.timedelta(0,0,0))

	#early & overtime check out
	cot_early = [] 
	cot_over = []

	for i in range(len(c_out)):
		if h_out[i] > c_out[i]:
			x = h_out[i] - c_out[i]
			cot_early.append(x)
			cot_over.append(datetime.timedelta(0,0,0))
		elif h_out[i] > c_out[i]:
			x = c_out[i] - h_out[i]
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
	x = h_out[i] - date_hour_in[i]
	y = x-(cin_late[i]-cot_early[i])
	work_hour.append(y)

#hrs check in, hrs check out, & departemen value

t_val = '\"True\"'
#title
#title='F:/abs-{}.txt'.format(date_finish)
#printing result
print(header)
for i in range(len(employee)):
	print('\n')
	for x in range(len(dates)):
		print('{0}\t{1}\t{2}\t{3}\t{4}\t{5}\t{6}\t{7}\t{8}\t{9}\t{10}\t{11}\t{12}\t{13}\t{14}\t{15}\t{16}\t{17}\t{18}\t{19}\t{20}\t{21}\t{22}\t{23}\t{24}\t{25}\t{26}\t{27}\t{28}'.format(nopeg[i],
		noakun[i],nomor[i],nama[i],empty,dates[x].isoformat(),sched_shift[i],date_hour_in[i].strftime('%H:%M'),h_out[i].strftime('%H:%M'),date_check_in[i].strftime('%H:%M'),c_out[i].strftime('%H:%M'),norm_tab,time_real[i],cin_late[i],cot_early[i],
		day_out[i],total_over[i],work_hour[i],empty,t_val,t_val,departemen[i],n_days[i],w_days[i],empty,total_att[i],empty,empty,empty))
