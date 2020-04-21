import random
import datetime
import string
from openpyxl import Workbook

#header
header = 'NoPeg,No. Akun,No.,Nama,Auto-Assign,Tanggal,Jam Kerja,Awal tugas,Akhir tugas,Masuk,Keluar,Normal,Waktu real,Telat,Plg Awal,Bolos,Waktu Lembur,Waktu Kerja,Status,Hrs C/In,Hrs C/Out,Departemen,NDays,Akhir Pekan,Hari Libur,Lama Hadir,NDays_OT,Lembur A.Pekan,Libur Lembur'.split(',')

#misc
''' Auto-Assign, Status, Hari Libur, Libur Lembur is empty'''
ety = ' '
n_tab = '\"1'

#employee untuk kolom NoPeg, Akun, No., Nama, Auto-Assign, Status, Hrs C/In, Hrs C/Out, Departemen
emp = [{'nopeg':'1','akun':'1','nomor':'1','nama':'Ape','assign':' ','status':' ','hcin':' ','hcout':' ','dpt':'Animal'},
		{'nopeg':'2','akun':'2','nomor':'2','nama':'Bull','assign':' ','status':' ','hcin':' ','hcout':' ','dpt':'Animal'},	
		{'nopeg':'3','akun':'3','nomor':'3','nama':'Cat','assign':' ','status':' ','hcin':' ','hcout':' ','dpt':'Animal'},
		{'nopeg':'4','akun':'4','nomor':'4','nama':'Dog','assign':' ','status':' ','hcin':' ','hcout':' ','dpt':'Animal'},
		{'nopeg':'5','akun':'5','nomor':'5','nama':'Elk','assign':' ','status':' ','hcin':' ','hcout':' ','dpt':'Animal'},
		{'nopeg':'6','akun':'6','nomor':'6','nama':'Fowl','assign':' ','status':' ','hcin':' ','hcout':' ','dpt':'Animal'}]

#date time
dt_st = datetime.date(2020,1,1)
dt_fn = datetime.date(2020,1,10)
dt_dlt = (dt_fn-dt_st)
dt_ls = [dt_st+datetime.timedelta(days=i) for i in range(dt_dlt.days+1)]
hr_in = datetime.time(8,0,0)
hr_out = [datetime.time(16,0,0),datetime.time(13,0,0)]
hr_off = datetime.time(0,0,0)
sf_ls = ['Senin-Jumat','Sabtu-Minggu']
n_tab = '\'1'

def late_in(hi,ci):
	if ci > hi:
		return ci-hi
	else:
		return datetime.timedelta(0,0,0)
def early_out(ho,co):
	if ho > co:
		return ho-co
	else:
		return datetime.timedelta(0,0,0)
def o_time(hi,ci,ho,co):
	if ci < hi and co > ho:
		return (hi-ci)+(co-ho)
	elif ci < hi and co < ho:
		return hi-ci
	elif ci > hi and co > ho:
		return co-ho
	else:
		return datetime.timedelta(0,0,0)
def w_time(hi,ci,ho,co):
	if ci>hi:
		return ho-ci
	elif co>ho:
		return co-hi
	else:
		return ho-hi
def t_time(a,ci,co):
	return a+(co-ci)
def nw_ot(hi,ci,ho,co):
	return round((co-ci)/(ho-hi),2)


container = []
for i in range(len(emp)):
	for x in range(len(dt_ls)):	
		cl_con = {}
		ch_in = random.randint(7,9)
		cm_in = [random.randint(45,59),random.randint(0,15),random.randint(0,59)]
		ch_out = [random.randint(14,18),random.randint(13,18)]
		
		dt_in = datetime.datetime.combine(dt_ls[x],hr_in)

		if dt_ls[x].weekday() == 6:
			wr_sf = sf_ls[1]
			dt_out = datetime.datetime.combine(dt_ls[x],hr_out[1])
			dh_in = datetime.datetime.combine(dt_ls[x],hr_off)
			dh_out = datetime.datetime.combine(dt_ls[x],hr_off)
			t_real = ety
			dh_late = ety
			dh_early = ety
			day_o = n_tab
			ov_tm = ety
			wr_tm = ety
			n_day = ety
			we_tm = ety
			ttl_a = datetime.datetime.combine(dt_ls[x],hr_off)
			n_ot = ety
			w_ot = ety
			
			cl_con['nopeg'] = str(i+1)
			cl_con['noakun'] = str(i+1)
			cl_con['nomor'] = str(i+1)
			cl_con['nama'] = emp[i]['nama']
			cl_con['assign'] = ety
			cl_con['shift'] = wr_sf
			cl_con['date'] = dt_ls[x].strftime('%Y/%m/%d')
			cl_con['hour_on'] = dt_in.strftime('%H:%M')
			cl_con['hour_off'] = dt_out.strftime('%H:%M')
			cl_con['check_in'] = dh_in.strftime('%H:%M')
			cl_con['check_out'] = dh_out.strftime('%H:%M')
			cl_con['normal_time'] = n_tab
			cl_con['real_time'] = t_real
			cl_con['late'] = dh_late
			cl_con['early'] = dh_early
			cl_con['day_off'] = day_o
			cl_con['overtime'] = ov_tm
			cl_con['worktime'] = wr_tm
			cl_con['status'] = ety
			cl_con['man_cin'] = ety
			cl_con['man_cout'] = ety
			cl_con['dept'] = emp[i]['dpt']
			cl_con['normalday'] = n_day
			cl_con['weekday'] = we_tm
			cl_con['holiday'] = n_tab
			cl_con['total_att'] = ttl_a.strftime('%H:%M')
			cl_con['normal_ot'] = n_ot
			cl_con['week_ot'] = w_ot
			cl_con['holi_ot'] = ety
			container.append(cl_con)
			
		elif dt_ls[x].weekday() == 5:
			wr_sf = sf_ls[1]
			dt_out = datetime.datetime.combine(dt_ls[x],hr_out[1])
			dh_out = datetime.datetime.combine(dt_ls[x],datetime.time(ch_out[1],cm_in[2]))
			t_real = n_tab
			if ch_in == 7:
				tm_in = datetime.time(ch_in, cm_in[0])
				dh_in = datetime.datetime.combine(dt_ls[x],tm_in)
				dh_late = datetime.datetime.combine(dt_ls[x],hr_off) + late_in(dt_in,dh_in)
				dh_early = datetime.datetime.combine(dt_ls[x],hr_off) + late_in(dt_out,dh_out)
				ov_tm = datetime.datetime.combine(dt_ls[x],hr_off) + o_time(dt_in,dh_in,dt_out,dh_out)
				wr_tm = datetime.datetime.combine(dt_ls[x],hr_off) + w_time(dt_in,dh_in,dt_out,dh_out)
				ttl_a = t_time(datetime.datetime.combine(dt_ls[x],hr_off),dh_in,dh_out)
				w_ot = nw_ot(dt_in,dh_in,dt_out,dh_out)
				day_o = ety
				n_day = ety
				we_tm = n_tab
				n_ot = ety
				
				cl_con['nopeg'] = str(i+1)
				cl_con['noakun'] = str(i+1)
				cl_con['nomor'] = str(i+1)
				cl_con['nama'] = emp[i]['nama']
				cl_con['assign'] = ety
				cl_con['shift'] = wr_sf
				cl_con['date'] = dt_ls[x].strftime('%Y/%m/%d')
				cl_con['hour_on'] = dt_in.strftime('%H:%M')
				cl_con['hour_off'] = dt_out.strftime('%H:%M')
				cl_con['check_in'] = dh_in.strftime('%H:%M')
				cl_con['check_out'] = dh_out.strftime('%H:%M')
				cl_con['normal_time'] = n_tab
				cl_con['real_time'] = t_real
				cl_con['late'] = dh_late.strftime('%H:%M')
				cl_con['early'] = dh_early.strftime('%H:%M')
				cl_con['day_off'] = day_o
				cl_con['overtime'] = ov_tm.strftime('%H:%M')
				cl_con['worktime'] = wr_tm.strftime('%H:%M')
				cl_con['status'] = ety
				cl_con['man_cin'] = ety
				cl_con['man_cout'] = ety
				cl_con['dept'] = emp[i]['dpt']
				cl_con['normalday'] = n_day
				cl_con['weekday'] = we_tm
				cl_con['holiday'] = ety
				cl_con['total_att'] = ttl_a.strftime('%H:%M')
				cl_con['normal_ot'] = n_ot
				cl_con['week_ot'] = w_ot
				cl_con['holi_ot'] = ety
				container.append(cl_con)
				
			else:
				tm_in = datetime.time(ch_in, cm_in[1])
				dh_in = datetime.datetime.combine(dt_ls[x],tm_in)
				dh_late = datetime.datetime.combine(dt_ls[x],hr_off) + late_in(dt_in,dh_in)
				dh_early = datetime.datetime.combine(dt_ls[x],hr_off) + late_in(dt_out,dh_out)
				ov_tm = datetime.datetime.combine(dt_ls[x],hr_off) + o_time(dt_in,dh_in,dt_out,dh_out)
				wr_tm = datetime.datetime.combine(dt_ls[x],hr_off) + w_time(dt_in,dh_in,dt_out,dh_out)
				ttl_a = t_time(datetime.datetime.combine(dt_ls[x],hr_off),dh_in,dh_out)
				w_ot = nw_ot(dt_in,dh_in,dt_out,dh_out)
				day_o = ety
				n_day = ety
				we_tm = n_tab
				n_ot = ety
				
				cl_con['nopeg'] = str(i+1)
				cl_con['noakun'] = str(i+1)
				cl_con['nomor'] = str(i+1)
				cl_con['nama'] = emp[i]['nama']
				cl_con['assign'] = ety
				cl_con['shift'] = wr_sf
				cl_con['date'] = dt_ls[x].strftime('%Y/%m/%d')
				cl_con['hour_on'] = dt_in.strftime('%H:%M')
				cl_con['hour_off'] = dt_out.strftime('%H:%M')
				cl_con['check_in'] = dh_in.strftime('%H:%M')
				cl_con['check_out'] = dh_out.strftime('%H:%M')
				cl_con['normal_time'] = n_tab
				cl_con['real_time'] = t_real
				cl_con['late'] = dh_late.strftime('%H:%M')
				cl_con['early'] = dh_early.strftime('%H:%M')
				cl_con['day_off'] = day_o
				cl_con['overtime'] = ov_tm.strftime('%H:%M')
				cl_con['worktime'] = wr_tm.strftime('%H:%M')
				cl_con['status'] = ety
				cl_con['man_cin'] = ety
				cl_con['man_cout'] = ety
				cl_con['dept'] = emp[i]['dpt']
				cl_con['normalday'] = n_day
				cl_con['weekday'] = we_tm
				cl_con['holiday'] = ety
				cl_con['total_att'] = ttl_a.strftime('%H:%M')
				cl_con['normal_ot'] = n_ot
				cl_con['week_ot'] = w_ot
				cl_con['holi_ot'] = ety
				container.append(cl_con)
				
		else:
			wr_sf = sf_ls[0]
			dt_out = datetime.datetime.combine(dt_ls[x],hr_out[0])
			dh_out = datetime.datetime.combine(dt_ls[x],datetime.time(ch_out[0],cm_in[2]))
			t_real = n_tab
			if ch_in == 7:
				tm_in = datetime.time(ch_in, cm_in[0])
				dh_in = datetime.datetime.combine(dt_ls[x],tm_in)
				dh_late = datetime.datetime.combine(dt_ls[x],hr_off) + late_in(dt_in,dh_in)
				dh_early = datetime.datetime.combine(dt_ls[x],hr_off) + late_in(dt_out,dh_out)
				ov_tm = datetime.datetime.combine(dt_ls[x],hr_off) + o_time(dt_in,dh_in,dt_out,dh_out)
				wr_tm = datetime.datetime.combine(dt_ls[x],hr_off) + w_time(dt_in,dh_in,dt_out,dh_out)
				ttl_a = t_time(datetime.datetime.combine(dt_ls[x],hr_off),dh_in,dh_out)
				n_ot = nw_ot(dt_in,dh_in,dt_out,dh_out)
				day_o = ety
				n_day = n_tab
				we_tm = ety
				w_ot = ety
				
				cl_con['nopeg'] = str(i+1)
				cl_con['noakun'] = str(i+1)
				cl_con['nomor'] = str(i+1)
				cl_con['nama'] = emp[i]['nama']
				cl_con['assign'] = ety
				cl_con['shift'] = wr_sf
				cl_con['date'] = dt_ls[x].strftime('%Y/%m/%d')
				cl_con['hour_on'] = dt_in.strftime('%H:%M')
				cl_con['hour_off'] = dt_out.strftime('%H:%M')
				cl_con['check_in'] = dh_in.strftime('%H:%M')
				cl_con['check_out'] = dh_out.strftime('%H:%M')
				cl_con['normal_time'] = n_tab
				cl_con['real_time'] = t_real
				cl_con['late'] = dh_late.strftime('%H:%M')
				cl_con['early'] = dh_early.strftime('%H:%M')
				cl_con['day_off'] = day_o
				cl_con['overtime'] = ov_tm.strftime('%H:%M')
				cl_con['worktime'] = wr_tm.strftime('%H:%M')
				cl_con['status'] = ety
				cl_con['man_cin'] = ety
				cl_con['man_cout'] = ety
				cl_con['dept'] = emp[i]['dpt']
				cl_con['normalday'] = n_day
				cl_con['weekday'] = we_tm
				cl_con['holiday'] = ety
				cl_con['total_att'] = ttl_a.strftime('%H:%M')
				cl_con['normal_ot'] = n_ot
				cl_con['week_ot'] = w_ot
				cl_con['holi_ot'] = ety
				container.append(cl_con)
				
			else:
				tm_in = datetime.time(ch_in, cm_in[1])
				dh_in = datetime.datetime.combine(dt_ls[x],tm_in)
				dh_late = datetime.datetime.combine(dt_ls[x],hr_off) + late_in(dt_in,dh_in)
				dh_early = datetime.datetime.combine(dt_ls[x],hr_off) + late_in(dt_out,dh_out)
				ov_tm = datetime.datetime.combine(dt_ls[x],hr_off) + o_time(dt_in,dh_in,dt_out,dh_out)
				wr_tm = datetime.datetime.combine(dt_ls[x],hr_off) + w_time(dt_in,dh_in,dt_out,dh_out)
				ttl_a = t_time(datetime.datetime.combine(dt_ls[x],hr_off),dh_in,dh_out)
				n_ot = nw_ot(dt_in,dh_in,dt_out,dh_out)
				day_o = ety
				n_day = n_tab
				we_tm = ety
				w_ot = ety
				
				cl_con['nopeg'] = str(i+1)
				cl_con['noakun'] = str(i+1)
				cl_con['nomor'] = str(i+1)
				cl_con['nama'] = emp[i]['nama']
				cl_con['assign'] = ety
				cl_con['shift'] = wr_sf
				cl_con['date'] = dt_ls[x].strftime('%Y/%m/%d')
				cl_con['hour_on'] = dt_in.strftime('%H:%M')
				cl_con['hour_off'] = dt_out.strftime('%H:%M')
				cl_con['check_in'] = dh_in.strftime('%H:%M')
				cl_con['check_out'] = dh_out.strftime('%H:%M')
				cl_con['normal_time'] = n_tab
				cl_con['real_time'] = t_real
				cl_con['late'] = dh_late.strftime('%H:%M')
				cl_con['early'] = dh_early.strftime('%H:%M')
				cl_con['day_off'] = day_o
				cl_con['overtime'] = ov_tm.strftime('%H:%M')
				cl_con['worktime'] = wr_tm.strftime('%H:%M')
				cl_con['status'] = ety
				cl_con['man_cin'] = ety
				cl_con['man_cout'] = ety
				cl_con['dept'] = emp[i]['dpt']
				cl_con['normalday'] = n_day
				cl_con['weekday'] = we_tm
				cl_con['holiday'] = ety
				cl_con['total_att'] = ttl_a.strftime('%H:%M')
				cl_con['normal_ot'] = n_ot
				cl_con['week_ot'] = w_ot
				cl_con['holi_ot'] = ety
				container.append(cl_con)


column = list(string.ascii_uppercase)+['AA','AB','AC']
wb = Workbook()
ws = wb.active
ws.title = 'Absensi'

#output to excell
for i in range(len(header)):
	ws.cell(column=i+1,row=1, value=header[i])

for x in range(len(container)):
	z=list(container[x].values())
	for y in range(len(column)):
		ws.cell(column=y+1,row=x+2,value=(z[y]))

wb.save('testing.xlsx')