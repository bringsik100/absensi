#!/usr/bin/env python3
"""
Proses
"""

from random import randint as ri
from datetime import datetime as dt
from datetime import timedelta as td
import pytest
from test.jadwal_test import test_rules as ts
from test.output_test import test_out_put as o_put

class test_datecount:

	def __init__(self,date_start,date_end):
		self.date_start = date_start
		self.date_end = date_end
		self.date_delta = self.date_end - self.date_start
		self.dates = []
		for i in range(self.date_delta.days + 1):
			self.dates.append(self.date_start+td(days=i))

	def test_misc(self):
		self.shifts = ts.test_shift_sorc()
		self.header = o_put.test_header()

class test_timecount():

	def __init__(self,hour_in,hour_out,check_in,check_out):
		self.hour_in = hour_in
		self.hour_out = hour_out
		self.check_in = check_in
		self.check_out = check_out
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
		if self.test_o_time > 0:
			return round((self.hour_in - self.check_in)/td(hours=1),2)
		else:
			return " "

if __name__=='__main__':
	main()
