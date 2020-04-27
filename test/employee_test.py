'''
fungsi untuk create, read, write, edit, dan delete item dalam employee.json
'''
import json

class test_source_emp:
	'''fungsi untuk membaca employee.json'''
	def __init__(self):
		'''membaca input'''
		with open('data/employee.json','r') as srce:
			self.source = json.load(srce)
		return self.source
		
	def test_source_pr(self):
		print(self.source)
		
class test_insert_emp:
	'''fungsi untuk memasukkan data ke employee.json'''
	def __init__(self,**kwargs):
		'''input dari user'''
		self.nopeg = nopeg
		self.akun = akun
		self.nomor = nomor
		self.nama = nama
		self.dept = dept
		self.buffer = {}
		
		'''data ditampung di buffer dan ditampilkan di layar'''
		return self.buffer.update(self.nopeg, self.akun, self.nomor, self.nama, self.dept)
		print(self.buffer)
	
	def test_insert_pra(self):
		''' menampilkan data source dan buffer ke layar'''
		print(test_source_emp.source + self.buffer)
	
	def test_insert_prb(self):
		''' menampilkan data buffer ke layar'''
		print(self.buffer)
		
	def test_insert_wr(self):
		'''menulis isi source dan buffer ke employee.json'''
		with open('data/employee.json','w') as srce:
			x = json.dumps(test_source_emp.source + self.buffer)
			srce.write(x)

if __name__ == '__main__':
	main()