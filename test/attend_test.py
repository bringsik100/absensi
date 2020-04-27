#!/usr/bin/env python3
"""
Attend
"""

from random import randint as ri
from datetime import datetime as dt
from datetime import timedelta as td
import pytest
from test.shift_test import test_shift_rule as ts
from test.output_test import test_out_put as o_put

class test_countf():
	
	def __init__(self,*args):
		self.hour_in = hi
		self.hour_out = ho
		self.check_in = ci
		self.check_out = co
		for i in [self.hour_in,self.hour_out,self.check_in,self.check_out]:
			if isinstance(i,td) == False:
				i = td(seconds=0)
			else:
				continue
	
	def test_late_in(self):
		'''late check in'''
		'''menghitung berapa lama pegawai terlambat'''
		if self.check_in > self.hour_in:
			return self.check_in - self.hour_in
		else:
			return td(seconds=0)
	def test_early_out(self):
		'''early check out'''
		'''menghitung berapa lama pegawai pulang lebih awal'''
		if self.hour_out > self.check_out:
			return self.hour_out - self.check_out
		else:
			return td(seconds=0)
	
	def test_o_time(self):
		'''over time'''
		'''menghitung lembur'''
		if self.check_in < self.hour_in and self.check_out > self.hour_out:
			return (self.hour_in - self.check_in)+(self.check_out - self.hour_out)
		elif self.check_in < self.hour_in and self.check_out < self.hour_out:
			return self.hour_in - self.check_in
		elif self.check_in > self.hour_in and self.check_out > self.hour_out:
			return self.check_out - self.hour_out
		else:
			return td(seconds=0)
	
	def test_w_time(self):
		'''work time'''
		'''menghitung jam kerja minus telat dan pulang awal'''
		if self.check_in > self.hour_in:
			return self.hour_out - self.check_in
		elif self.check_out > self.hour_out:
			return self.check_out - self.hour_in
		else:
			return self.hour_out - self.hour_in

	def test_t_time(self):
		'''total time'''
		'''menghitung jam kerja dari awal masuk sampai keluar'''
		return (self.check_out - self.check_in)

	def test_nw_ot(self):
		'''normal day and weekend day over time'''
		'''menghitung jam lembur dalam desimal'''
		if self.test_o_time > 0 
			return round((self.hour_in - self.check_in)/td(hours=1),2)
		else:
			return " "

class test_var:
	
	def __init__(self):
		self.date_start = ''
		self.date_end = ''
		self.date_delta = ''
		self.dates = []
	
	def test_time(self):
		self.hour_in =''
		self.hour_outur_out = ''
		self.hour_outur_off = ''
		
	def test_misc(self):
		self.shifts = ts.test_shift_sorc()
		self.header = o_put.test_header()

if __name__=='__main__':
	main()
