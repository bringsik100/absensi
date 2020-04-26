import json
from datetime import datetime as dt
from datetime import timedelta as dt

class test_shift_rule:

	def __init__(self,name,**kwargs):
		self.name = name
		self.weekdays = weekdays
		self.hour_start = hour_start
		self.hour_end = hour_end
		self.late_tol = late_tol
		self.early_tol = early_tol
		self.chin_min = chin_min
		self.chin_max = chin_max
		self.chout_min = chout_min
		self.chout_max = chout_max
		shift_con=[]
		shift_con.append(list(self.name,self.weekdays,self.hour_start,self.hour_end,self.late_tol,self.early_tol,self.chin_min,self.chin_max,self.chout_min,self.chout_max))

	def test_shift_read(self,inp):
		
		self.inp = inp

		if isinistance(self.inp,json) == False:
			return print(f'{self.inp} is not a JSON file')
		else:
			pass
		with open(inp,'r') as buff:
			shift_con = list(json.read(buff))
			return shift_con

	def test_shift_print(self):
		print(shift_con)

	def test_shift_write(self,inp):
		self.inp = inp
		with open(inp,'w') as buff:
			x = json.dump(shift_con)
			buff.write(x)
