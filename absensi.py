import random
import datetime

#header
header = 'NoPeg,No. Akun,No.,Nama,Auto-Assign,Tanggal,Jam Kerja,Awal tugas,Akhir tugas,Masuk,Keluar,Normal,Waktu real,Telat,Plg Awal,Bolos,Waktu Lembur,Waktu Kerja,Status,Hrs C/In,Hrs C/Out,Departemen,NDays,Akhir Pekan,Hari Libur,		Lama Hadir,NDays_OT,Lembur A.Pekan,Libur Lembur'.replace(',','\t')

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

#globals
c_in = []
c_out = []
h_in = []
h_out = []
n_days = []
w_days = []
t_att = []
s_shift = []
t_real = []
d_out = []
cin_late = []
cin_over = []
cot_early = [] 
cot_over = []
total_over = []
w_hour = []

#date module
def dates(a):
	#a is a date_list
	global c_in
	global c_out
	global h_in
	global h_out
	global n_days
	global w_days
	global t_att
	global s_shift
	global t_real
	global d_out
	global cin_late
	global cin_over
	global cot_early
	global cot_over
	global total_over
	global w_hour
	
	for i in a:
		if i.weekday() == 6:
			n_days.append(' ')
			w_days.append('\"1')
			h_in.append(datetime.datetime.combine(i,hour_off))
			h_out.append(datetime.datetime.combine(i,hour_off))
			c_in.append(datetime.datetime.combine(i,hour_off))
			c_out.append(datetime.datetime.combine(i,hour_off))
		
		elif i.weekday() == 5:
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
	for x in range(len(c_in)):
		xx = c_out[x] - c_in[x]
		t_att.append(xx)

	#shift
	shift_l = ['Senin-Jumat','Sabtu-Minggu']
	for x in a:
		if x.weekday() == 5 or 6:
			s_shift.append(shift_l[1])
		else:
			s_shift.append(shift_l[0])

	#normal column, real time column, & day out
	for x in c_in:
		if x.hour == 0:
			t_real.append(empty)
			d_out.append('\"True\"')
		else:
			t_real.append(norm_tab)
			d_out.append(empty)

	#late & overtime check in
	for x in range(len(c_in)):
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
	for i in range(len(cin_over)):
		x = cin_over[i]+cot_over[i]
		total_over.append(x)

	#work time
	for i in range(len(h_in)):
		x = h_out[i] - h_in[i]
		y = x-(cin_late[i]-cot_early[i])
		w_hour.append(y)

#hrs check in, hrs check out, & departemen value
t_val = '\"True\"'

#title
#title='F:/abs-{}.txt'.format(date_finish)

#printing result

print(header)
for i in range(len(nama)):
	dates(date_list)
	for x in range(len(date_list)):
		print (nopeg[i],noakun[i],nomor[i],nama[i],empty,date_list[i],s_shift[i],h_in[i],h_out[i],c_in[i],c_out[i],norm_tab,t_real[i],cin_late[i],cot_early[i],d_out[i],total_over[i],w_hour[i],empty,t_val,t_val,departemen[i],n_days[i],w_days[i],empty,w_hour[i],empty,empty,empty)
		
