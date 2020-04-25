#!/usr/bin/env python3
"""
Absensi
"""

__author__ = "bringsik100"
__version__ = "0.2.2"
__license__ = "CC"

from random import randint as ri
from datetime import datetime as dt
from datetime import timedelta as td
import string
import json
from openpyxl import Workbook

#FUNCTION LIST
'''
penjelasan variable 
hi = hour in, jam masuk
ho = hour out, jam keluar
ci = check in
co = check out
'''

class countf:
	'''class utama, mungkin harus dipisah di release berikut'''
	
	def __init__(self,hi,ho,ci,co):
		self.hi = hi
		self.ho = ho
		self.ci = ci
		self.co = co
	
		for i in [self.hi,self.ho,self.ci,self.co]:
			if isinstance(i,td) == False:
				i = td(seconds = 0)
			else:
				continue
	
	def late_in(self):
		'''late check in'''
		'''menghitung berapa lama pegawai terlambat'''
		if self.ci > self.hi:
			return self.ci-self.hi
		else:
			return td(seconds=0)
	
	def early_out(self):
		'''early check out'''
		'''menghitung berapa lama pegawai pulang lebih awal'''
		if self.ho > self.co:
			return self.ho-self.co
		else:
			return td(seconds=0)
	
	def o_time(self):
		'''over time'''
		'''menghitung lembur'''
		if self.ci < self.hi and self.co > self.ho:
			return (self.hi - self.ci) + (self.co - self.ho)
		elif self.ci < self.hi and self.co < self.ho:
			return self.hi - self.ci
		elif self.ci > self.hi and self.co > self.ho:
			return co-ho
		else:
			return td(seconds=0)

	def w_time(self):
		'''work time'''
		'''menghitung jam kerja minus telat dan pulang awal'''
		if self.ci > self.hi:
			return self.ho - self.ci
		elif self.co > self.ho:
			return self.co - self.hi
		else:
			return self.ho - self.hi

	def t_time(self):
		'''total time'''
		'''menghitung jam kerja dari awal masuk sampai keluar'''
		return (self.co - self.ci)
	
	def nw_ot(self):
		'''normal day and weekend day over time'''
		'''menghitung jam lembur dalam desimal'''
		return round((self.co - self.ci) / (self.ho - self.hi),2)

def con_up(a):
	'''container update'''
	'''update dan pengisi cl_con'''
	'''ini harus ditulis ulang agar tak terlihat kacau'''
	a['nopeg'] = str(i+1)
	a['noakun'] = str(i+1)
	a['nomor'] = str(i+1)
	a['nama'] = emp[i]['nama']
	a['assign'] = ety
	a['shift'] = wr_sf
	a['date'] = today.strftime('%Y/%m/%d')
	a['hour_on'] = dt_in.strftime('%H:%M')
	a['hour_off'] = dt_out.strftime('%H:%M')
	a['check_in'] = dh_in
	a['check_out'] = dh_out
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
	a['total_att'] = (today+ttl_a).strftime('%H:%M')
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
'''variable untuk jam masuk, jam pulang, check in, cheack out, jam kerja dan lain-lain'''
dt_st = dt(2020,1,1,0,0,0) #start date
dt_fn = dt(2020,1,10,0,0,0) #end date
dt_dlt = (dt_fn-dt_st) #date interval
dt_ls = [dt_st+td(days=i) for i in range(dt_dlt.days+1)] #date list
hr_in = td(hours=8) #hour in
hr_out = [td(hours=16),td(hours=13)] #hour out. 16 PM and 13 PM
hr_0 = td(seconds=0) # td(seconds=0) hour
sf_ls = ['Senin-Jumat','Sabtu-Minggu'] #work shift list

if __name__ == '__main__':
	'''main program'''
	
	'''membaca header'''
	with open('data/header.json','r') as head_data:
		i = json.load(head_data)
		for x in i['header']:
			header.append(x)

	'''membaca employee untuk kolom NoPeg, Akun, No., Nama, Auto-Assign, Status, Hrs C/In, Hrs C/Out, Departemen'''
	with open('data/employee.json','r') as emp_data:
		i = json.load(emp_data)
		emp=list(i['employee'])

	for i in range(len(emp)):
		'''looping employee'''
		for x in range(len(dt_ls)):
			'''looping tanggal'''
			
			'''cluster container'''
			cl_con = {}
			today = dt_ls[x]
			'''randomisasi waktu in dan out'''
			ch_in = td(hours=ri(7,9))
			cm_in = [td(minutes=ri(45,59))
					,td(minutes=ri(0,15))
					,td(minutes=ri(0,59))]
			ch_out = [td(minutes=ri(14,18))
					,td(minutes=ri(13,18))]
			dt_in = today+hr_in
	
			if today.weekday() == 6:
				'''hari minggu'''
				wr_sf = sf_ls[1]
				dt_out = today+hr_out[1]
				dh_in = td(seconds=0)
				dh_out = td(seconds=0)
				t_real = ety
				dh_late = ety
				dh_early = ety
				day_o = n_tab
				ov_tm = ety
				wr_tm = ety
				n_day = ety
				we_tm = ety
				ttl_a = td(seconds=0)
				n_ot = ety
				w_ot = ety
				
				con_up(cl_con)
				container.append(cl_con)
				
			elif today.weekday() == 5:
				'''hari rabu'''
				wr_sf = sf_ls[1]
				dt_out = today+hr_out[1]
				dh_out = today+ch_out[1]+cm_in[2]
				t_real = n_tab
				if ch_in == 7:
					dh_in = today + ch_in + cm_in[0]
					#countf mulai disini 
					rs = countf(dt_in,dt_out,dh_in,dh_out) 
					dh_late = today + rs.late_in()
					dh_early = today + rs.early_out()
					ov_tm = today + rs.o_time()
					wr_tm = today + rs.w_time()
					ttl_a = rs.t_time()
					w_ot = rs.nw_ot()
					day_o = ety
					n_day = ety
					we_tm = n_tab
					n_ot = ety
					
					con_up(cl_con)
					container.append(cl_con)
					
				else:
					dh_in = today + ch_in + cm_in[1]
					#countf mulai disini
					rs = countf(dt_in,dt_out,dh_in,dh_out) 
					dh_late = today + rs.late_in()
					dh_early = today + rs.early_out()
					ov_tm = today + rs.o_time()
					wr_tm = today + rs.w_time()
					ttl_a = rs.t_time()
					w_ot = rs.nw_ot()
					day_o = ety
					n_day = ety
					we_tm = n_tab
					n_ot = ety
					
					con_up(cl_con)
					container.append(cl_con)
					
			else:
				'''hari senin sampai jumat'''
				wr_sf = sf_ls[0]
				dt_out = today + hr_out[0]
				dh_out = today + ch_out[0] + cm_in[2]
				t_real = n_tab
				if ch_in == 7:
					dh_in = today + ch_in + cm_in[0]
					#countf mulai disini
					rs = countf(dt_in,dt_out,dh_in,dh_out) 
					dh_late = today + rs.late_in()
					dh_early = today + rs.early_out()
					ov_tm = today + rs.o_time()
					wr_tm = today + rs.w_time()
					ttl_a = rs.t_time()
					w_ot = rs.nw_ot()
					day_o = ety
					n_day = ety
					we_tm = n_tab
					n_ot = ety
					
					con_up(cl_con)
					container.append(cl_con)
					
				else:
					dh_in = today + ch_in + cm_in[1]
					#countf mulai disini
					rs = countf(dt_in,dt_out,dh_in,dh_out)
					dh_late = today + rs.late_in()
					dh_early = today + rs.early_out()
					ov_tm = today + rs.o_time()
					wr_tm = today + rs.w_time()
					ttl_a = rs.t_time()
					w_ot = rs.nw_ot()
					day_o = ety
					n_day = ety
					we_tm = n_tab
					n_ot = ety
					
					con_up(cl_con)
					container.append(cl_con)
	
	'''proses output ke excell'''
	column = list(string.ascii_uppercase)+['AA','AB','AC']
	wb = Workbook()
	ws = wb.active
	ws.title = 'Absensi'
	
	#manuliskan data ke excell
	for i in range(len(header)):
		ws.cell(column=i+1,row=1, value=header[i])
	
	for x in range(len(container)):
		z=list(container[x].values())
		for y in range(len(column)):
			ws.cell(column=y+1,row=x+2,value=(z[y]))
	
	wb.save('testing.xlsx')
	wb.close
absensi()