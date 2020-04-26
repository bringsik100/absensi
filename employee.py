import json

class test_emplo:
	emp_list = []
	def __init__(self,**kwargs):
		self.nopeg = nopeg
		self.akun = akun
		self.nomor = nomor
		self.nama = nama
		self.dept = dept

		return emp_list.append(self.nopeg, self.akun, self.nomor, self.nama, self.dept)

	def test_emp_rd(self):
		with open('data/employee.json','r') as e_file:
			return test_emp_list.append(list(json.read(e_file)))

	def test_emp_pr(self):
		print(test_emp_list)

	def test_emp_wr(self):
		json.dump(emp_list)

	def test_emp_up(self,*args,**kwargs):
		self.args = args
		self.kwargs = kwargs
		for i in emp_list:
			for x in i:
				if x == self.args:
					x.kwargs = self.kwargs
