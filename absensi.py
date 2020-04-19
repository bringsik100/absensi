import random
import datetime

#header
header = 'NoPeg,No. Akun,No.,Nama,Auto-Assign,Tanggal,Jam Kerja,Awal tugas,Akhir tugas,Masuk,Keluar,Normal,Waktu real,Telat,Plg Awal,Bolos,Waktu Lembur,Waktu Kerja,Status,Hrs C/In,Hrs C/Out,Departemen,NDays,Akhir Pekan,Hari Libur,Lama Hadir,NDays_OT,Lembur A.Pekan,Libur Lembur'.replace(',','\t')

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
	if ci > hi:
		return datetime.timedelta(0,0,0)
	else:
		return hi-ci
	if ho > co:
		return datetime.timedelta(0,0,0)
	else:
		return co-ho
	return (hi-ci)+(co-ho)
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
print(header)

for i in range(len(emp)):
	for x in range(len(dt_ls)):
		ch_in = random.randint(7,9)
		cm_in = [random.randint(45,59),random.randint(0,15),random.randint(0,59)]
		ch_out = [random.randint(16,18),random.randint(15,18)]
		
		dt_in = datetime.datetime.combine(dt_ls[x],hr_in)

		if dt_ls[x].weekday() == 6:
			wr_sf = sf_ls[1]
			dt_out = datetime.datetime.combine(dt_ls[x],hr_out[1])
			dh_in = datetime.datetime.combine(dt_ls[x],hr_off)
			dh_out = datetime.datetime.combine(dt_ls[x],hr_off)
			t_real = ety
			dh_late = datetime.datetime.combine(dt_ls[x],hr_off)
			dh_early = datetime.datetime.combine(dt_ls[x],hr_off)
			day_o = n_tab
			ov_tm = datetime.datetime.combine(dt_ls[x],hr_off)
			wr_tm = datetime.datetime.combine(dt_ls[x],hr_off)
			n_day = ety
			we_tm = ety
			ttl_a = datetime.datetime.combine(dt_ls[x],hr_off)
			n_ot = ety
			w_ot = ety
			print('{0}\t{1}\t{2}\t{3}\t{4}\t{5}\t{6}\t{7}\t{8}\t{9}\t{10}\t{11}\t{12}\t{13}\t{14}\t{15}\t{16}\t{17}\t{18}\t{19}\t{20}\t{21}\t{22}\t{23}\t{24}\t{25}\t{26}\t{27}\t{28}\t{29}'.format(emp[i]['nopeg'],
		emp[i]['akun'],
		emp[i]['nomor'],
		emp[i]['nama'],
		emp[i]['assign'],
		dt_ls[x].strftime('%Y-%m-%d'),
		wr_sf,
		dt_in.strftime('%H:%M'),
		dt_out.strftime('%H:%M'),
		dh_in.strftime('%H:%M'),
		dh_out.strftime('%H:%M'),
		n_tab,
		t_real,
		dh_late,
		dh_early.strftime('%H:%M'),
		day_o,
		ov_tm.strftime('%H:%M'),
		wr_tm.strftime('%H:%M'),
		emp[i]['status'],
		emp[i]['hcin'],
		emp[i]['hcout'],
		emp[i]['dpt'],
		n_day,
		we_tm,
		ety,
		ttl_a.strftime('%H:%M'),
		n_ot,
		w_ot,
		ety,
		ety))
			
		elif dt_ls[x].weekday() == 5:
			wr_sf = sf_ls[1]
			dt_out = datetime.datetime.combine(dt_ls[x],hr_out[1])
			dh_out = datetime.datetime.combine(dt_ls[x],datetime.time(ch_out[1],cm_in[2]))
			t_real = n_tab
			if ch_in == 7:
				tm_in = datetime.time(ch_in, cm_in[0])
				dh_in = datetime.datetime.combine(dt_ls[x],tm_in)
				dh_late = datetime.datetime.combine(dt_ls[x],hr_off) + late_in(dt_in,dh_in)
				dh_early = dt_ls[x] + late_in(dt_out,dh_out)
				ov_tm = dt_ls[x] + o_time(dt_in,dh_in,dt_out,dh_out)
				wr_tm = dt_ls[x] + w_time(dt_in,dh_in,dt_out,dh_out)
				ttl_a = t_time(dt_ls[x],dh_in,dh_out)
				w_ot = nw_ot(dt_in,dh_in,dt_out,dh_out)
				day_o = ety
				n_day = ety
				we_tm = n_tab
				n_ot = ety
				print('{0}\t{1}\t{2}\t{3}\t{4}\t{5}\t{6}\t{7}\t{8}\t{9}\t{10}\t{11}\t{12}\t{13}\t{14}\t{15}\t{16}\t{17}\t{18}\t{19}\t{20}\t{21}\t{22}\t{23}\t{24}\t{25}\t{26}\t{27}\t{28}\t{29}'.format(emp[i]['nopeg'],
		emp[i]['akun'],
		emp[i]['nomor'],
		emp[i]['nama'],
		emp[i]['assign'],
		dt_ls[x].strftime('%Y-%m-%d'),
		wr_sf,
		dt_in.strftime('%H:%M'),
		dt_out.strftime('%H:%M'),
		dh_in.strftime('%H:%M'),
		dh_out.strftime('%H:%M'),
		n_tab,
		t_real,
		dh_late,
		dh_early.strftime('%H:%M'),
		day_o,
		ov_tm.strftime('%H:%M'),
		wr_tm.strftime('%H:%M'),
		emp[i]['status'],
		emp[i]['hcin'],
		emp[i]['hcout'],
		emp[i]['dpt'],
		n_day,
		we_tm,
		ety,
		ttl_a.strftime('%H:%M'),
		n_ot,
		w_ot,
		ety,
		ety))
			else:
				tm_in = datetime.time(ch_in, cm_in[1])
				dh_in = datetime.datetime.combine(dt_ls[x],tm_in)
				dh_late = datetime.datetime.combine(dt_ls[x],hr_off) + late_in(dt_in,dh_in)
				dh_early = dt_ls[x] + late_in(dt_out,dh_out)
				ov_tm = dt_ls[x] + o_time(dt_in,dh_in,dt_out,dh_out)
				wr_tm = dt_ls[x] + w_time(dt_in,dh_in,dt_out,dh_out)
				ttl_a = t_time(dt_ls[x],dh_in,dh_out)
				w_ot = nw_ot(dt_in,dh_in,dt_out,dh_out)
				day_o = ety
				n_day = ety
				we_tm = n_tab
				n_ot = ety
				print('{0}\t{1}\t{2}\t{3}\t{4}\t{5}\t{6}\t{7}\t{8}\t{9}\t{10}\t{11}\t{12}\t{13}\t{14}\t{15}\t{16}\t{17}\t{18}\t{19}\t{20}\t{21}\t{22}\t{23}\t{24}\t{25}\t{26}\t{27}\t{28}\t{29}'.format(emp[i]['nopeg'],
		emp[i]['akun'],
		emp[i]['nomor'],
		emp[i]['nama'],
		emp[i]['assign'],
		dt_ls[x].strftime('%Y-%m-%d'),
		wr_sf,
		dt_in.strftime('%H:%M'),
		dt_out.strftime('%H:%M'),
		dh_in.strftime('%H:%M'),
		dh_out.strftime('%H:%M'),
		n_tab,
		t_real,
		dh_late,
		dh_early.strftime('%H:%M'),
		day_o,
		ov_tm.strftime('%H:%M'),
		wr_tm.strftime('%H:%M'),
		emp[i]['status'],
		emp[i]['hcin'],
		emp[i]['hcout'],
		emp[i]['dpt'],
		n_day,
		we_tm,
		ety,
		ttl_a.strftime('%H:%M'),
		n_ot,
		w_ot,
		ety,
		ety))
	
		else:
			wr_sf = sf_ls[0]
			dt_out = datetime.datetime.combine(dt_ls[x],hr_out[0])
			dh_out = datetime.datetime.combine(dt_ls[x],datetime.time(ch_out[0],cm_in[2]))
			t_real = n_tab
			if ch_in == 7:
				tm_in = datetime.time(ch_in, cm_in[0])
				dh_in = datetime.datetime.combine(dt_ls[x],tm_in)
				dh_late = datetime.datetime.combine(dt_ls[x],hr_off) + late_in(dt_in,dh_in)
				dh_early = dt_ls[x] + late_in(dt_out,dh_out)
				ov_tm = dt_ls[x] + o_time(dt_in,dh_in,dt_out,dh_out)
				wr_tm = dt_ls[x] + w_time(dt_in,dh_in,dt_out,dh_out)
				ttl_a = t_time(dt_ls[x],dh_in,dh_out)
				n_ot = nw_ot(dt_in,dh_in,dt_out,dh_out)
				day_o = ety
				n_day = n_tab
				we_tm = ety
				w_ot = ety
				print('{0}\t{1}\t{2}\t{3}\t{4}\t{5}\t{6}\t{7}\t{8}\t{9}\t{10}\t{11}\t{12}\t{13}\t{14}\t{15}\t{16}\t{17}\t{18}\t{19}\t{20}\t{21}\t{22}\t{23}\t{24}\t{25}\t{26}\t{27}\t{28}\t{29}'.format(emp[i]['nopeg'],
		emp[i]['akun'],
		emp[i]['nomor'],
		emp[i]['nama'],
		emp[i]['assign'],
		dt_ls[x].strftime('%Y-%m-%d'),
		wr_sf,
		dt_in.strftime('%H:%M'),
		dt_out.strftime('%H:%M'),
		dh_in.strftime('%H:%M'),
		dh_out.strftime('%H:%M'),
		n_tab,
		t_real,
		dh_late,
		dh_early.strftime('%H:%M'),
		day_o,
		ov_tm.strftime('%H:%M'),
		wr_tm.strftime('%H:%M'),
		emp[i]['status'],
		emp[i]['hcin'],
		emp[i]['hcout'],
		emp[i]['dpt'],
		n_day,
		we_tm,
		ety,
		ttl_a.strftime('%H:%M'),
		n_ot,
		w_ot,
		ety,
		ety))
		
			else:
				tm_in = datetime.time(ch_in, cm_in[1])
				dh_in = datetime.datetime.combine(dt_ls[x],tm_in)
				dh_late = datetime.datetime.combine(dt_ls[x],hr_off) + late_in(dt_in,dh_in)
				dh_early = dt_ls[x] + late_in(dt_out,dh_out)
				ov_tm = dt_ls[x] + o_time(dt_in,dh_in,dt_out,dh_out)
				wr_tm = dt_ls[x] + w_time(dt_in,dh_in,dt_out,dh_out)
				ttl_a = t_time(dt_ls[x],dh_in,dh_out)
				n_ot = nw_ot(dt_in,dh_in,dt_out,dh_out)
				day_o = ety
				n_day = n_tab
				we_tm = ety
				w_ot = ety
			
				print('{0}\t{1}\t{2}\t{3}\t{4}\t{5}\t{6}\t{7}\t{8}\t{9}\t{10}\t{11}\t{12}\t{13}\t{14}\t{15}\t{16}\t{17}\t{18}\t{19}\t{20}\t{21}\t{22}\t{23}\t{24}\t{25}\t{26}\t{27}\t{28}\t{29}'.format(emp[i]['nopeg'],
		emp[i]['akun'],
		emp[i]['nomor'],
		emp[i]['nama'],
		emp[i]['assign'],
		dt_ls[x].strftime('%Y-%m-%d'),
		wr_sf,
		dt_in.strftime('%H:%M'),
		dt_out.strftime('%H:%M'),
		dh_in.strftime('%H:%M'),
		dh_out.strftime('%H:%M'),
		n_tab,
		t_real,
		dh_late,
		dh_early.strftime('%H:%M'),
		day_o,
		ov_tm.strftime('%H:%M'),
		wr_tm.strftime('%H:%M'),
		emp[i]['status'],
		emp[i]['hcin'],
		emp[i]['hcout'],
		emp[i]['dpt'],
		n_day,
		we_tm,
		ety,
		ttl_a.strftime('%H:%M'),
		n_ot,
		w_ot,
		ety,
		ety))