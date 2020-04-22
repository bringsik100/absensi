#!/usr/bin/env python3
"""
absensi
"""

__author__ = "bringsik100"
__version__ = "0.2.1"
__license__ = "CC"

import random
import datetime
import string
import json
import __main__
from openpyxl import Workbook

#FUNCTION LIST
'''
penjelasan variable 

hi = hour in, jam masuk
ho = hour out, jam keluar
ci = check in
co = check out
'''
def late_in(hi,ci):
	'''late check in'''
	'''menghitung berapa lama pegawai terlambat'''
	if ci > hi:
		return ci-hi
	else:
		return datetime.timedelta(0,0,0)

def early_out(ho,co):
	'''early check out'''
	'''menghitung berapa lama pegawai pulang lebih awal'''
	if ho > co:
		return ho-co
	else:
		return datetime.timedelta(0,0,0)

def o_time(hi,ci,ho,co):
	'''over time'''
	'''menghitung lembur'''
	if ci < hi and co > ho:
		return (hi-ci)+(co-ho)
	elif ci < hi and co < ho:
		return hi-ci
	elif ci > hi and co > ho:
		return co-ho
	else:
		return datetime.timedelta(0,0,0)

def w_time(hi,ci,ho,co):
	'''work time'''
	'''menghitung jam kerja minus telat dan pulang awal'''
	if ci>hi:
		return ho-ci
	elif co>ho:
		return co-hi
	else:
		return ho-hi

def t_time(a,ci,co):
	'''total time'''
	'''menghitung jam kerja dari awal masuk sampai keluar'''
	return a+(co-ci)

def nw_ot(hi,ci,ho,co):
	'''normal day and weekend day over time'''
	'''menghitung jam lembur dalam desimal'''
	return round((co-ci)/(ho-hi),2)
def con_up(a):
	'''container update'''
	'''update dan pengisi cl_con'''
	self.a=a
	a['nopeg'] = str(i+1)
	a['noakun'] = str(i+1)
	a['nomor'] = str(i+1)
	a['nama'] = emp[i]['nama']
	a['assign'] = ety
	a['shift'] = wr_sf
	a['date'] = dt_ls[x].strftime('%Y/%m/%d')
	a['hour_on'] = dt_in.strftime('%H:%M')
	a['hour_off'] = dt_out.strftime('%H:%M')
	a['check_in'] = dh_in.strftime('%H:%M')
	a['check_out'] = dh_out.strftime('%H:%M')
	a['normal_time'] = n_tab
	a['real_time'] = t_real
	a['late'] = dh_late
	a['early'] = dh_early
	a['day_off'] = day_o
	a['overtime'] = ov_tm
	a['worktime'] = wr_tm
	a['status'] = ety
	a['man_cin'] = ety
	a['man_cout'] = ety
	a['dept'] = emp[i]['dpt']
	a['normalday'] = n_day
	a['weekday'] = we_tm
	a['holiday'] = n_tab
	a['total_att'] = ttl_a.strftime('%H:%M')
	a['normal_ot'] = n_ot
	a['week_ot'] = w_ot
	a['holi_ot'] = ety

#VARIABLE LIST
header = []
emp = []
container = []
ety = ' ' #Auto-Assign, Status, Hari Libur, Libur Lembur is empty
n_tab = '\"1'
#date time
dt_st = datetime.date(2020,1,1)
dt_fn = datetime.date(2020,1,10)
dt_dlt = (dt_fn-dt_st)
dt_ls = [dt_st+datetime.timedelta(days=i) for i in range(dt_dlt.days+1)]
hr_in = datetime.time(8,0,0)
hr_out = [datetime.time(16,0,0),datetime.time(13,0,0)]
hr_off = datetime.time(0,0,0)
sf_ls = ['Senin-Jumat','Sabtu-Minggu']

if __name__ == "absensi":
	'''membaca header'''
	with open('\\data\\header.json','r') as head_data:
		i = json.load(head_data)
		for x in i['header']:
			header.append(x)

	'''membaca employee untuk kolom NoPeg, Akun, No., Nama, Auto-Assign, Status, Hrs C/In, Hrs C/Out, Departemen'''
	with open('\\data\\employee.json','r') as emp_data:
		i = json.load(emp_data)
		for x in range(len(i['employee'])):
			emp.append(x)

	for i in range(len(emp)):
		'''looping employee'''
		for x in range(len(dt_ls)):
			'''looping tanggal'''
			
			'''cluster container'''
			cl_con = {}
			'''randomisasi waktu in dan out'''
			ch_in = random.randint(7,9)
			cm_in = [random.randint(45,59),random.randint(0,15),random.randint(0,59)]
			ch_out = [random.randint(14,18),random.randint(13,18)]
			
			dt_in = datetime.datetime.combine(dt_ls[x],hr_in)
	
			if dt_ls[x].weekday() == 6:
				'''hari minggu'''
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
				
				con_up(cl_con)
				container.append(cl_con)
				
			elif dt_ls[x].weekday() == 5:
				'''hari rabu'''
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
					
					con_up(cl_con)
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
					
					con_up(cl_con)
					container.append(cl_con)
					
			else:
				'''hari senin sampai jumat'''
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
					
					con_up(cl_con)
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
					
					con_up(cl_con)
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
absensi()
