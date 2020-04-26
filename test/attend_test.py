#!/usr/bin/env python3
"""
Attend
"""

from random import randint as ri
from datetime import datetime as dt
from datetime import timedelta as td
import pytest

class test_countf():
	
	def __init__(self,*args):
		self.hi = hi
		self.ho = ho
		self.ci = ci
		self.co = co
		for i in [self.hi,self.ho,self.ci,self.co]:
			if isinstance(i,td) == False:
				i = td(seconds=0)
			else:
				continue
	
	def test_late_in(self):
		'''late check in'''
		'''menghitung berapa lama pegawai terlambat'''
		if self.ci > self.hi:
			return self.ci - self.hi
		else:
			return td(seconds=0)
	def test_early_out(self):
		'''early check out'''
		'''menghitung berapa lama pegawai pulang lebih awal'''
		if self.ho > self.co:
			return self.ho - self.co
		else:
			return td(seconds=0)
	
	def test_o_time(self):
		'''over time'''
		'''menghitung lembur'''
		if self.ci < self.hi and self.co > self.ho:
			return (self.hi - self.ci)+(self.co - self.ho)
		elif self.ci < self.hi and self.co < self.ho:
			return self.hi - self.ci
		elif self.ci > self.hi and self.co > self.ho:
			return self.co - self.ho
		else:
			return td(seconds=0)
	
	def test_w_time(self):
		'''work time'''
		'''menghitung jam kerja minus telat dan pulang awal'''
		if self.ci > self.hi:
			return self.ho - self.ci
		elif self.co > self.ho:
			return self.co - self.hi
		else:
			return self.ho - self.hi

	def test_t_time(self):
		'''total time'''
		'''menghitung jam kerja dari awal masuk sampai keluar'''
		return (self.co - self.ci)

	def test_nw_ot(self):
		'''normal day and weekend day over time'''
		'''menghitung jam lembur dalam desimal'''
		if self.ci < self.hi and self.co > self.ho:
			return round(((self.hi - self.ci)+(self.co - self.ho))/td(hours=1),2)
		elif self.ci < self.hi and self.co < self.ho:
			return round((self.hi - self.ci)/td(hours=1),2)
		elif self.ci > self.hi and self.co > self.ho:
			return round((self.co - self.ho)/td(hours=1),2)
		else:
			return " "
if __name__=='__main__':
	main()
