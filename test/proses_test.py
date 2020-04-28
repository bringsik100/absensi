'''
fungsi untuk create, read, write, edit, dan delete item dalam employee.json
'''
import json

'''fungsi untuk membaca pegawai.json'''
with open('test/data/pegawai.json','r') as srce:
	sumber = json.load(srce)
	return sumber

def test_print():
		print(sumber)
		
class test_masuk:
	'''fungsi untuk memasukkan data ke pegawai.json'''
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
	
	def test_print_all(self):
		''' menampilkan data source dan buffer ke layar'''
		print(sumber + self.buffer)
	
	def test_print_buff(self):
		''' menampilkan data buffer ke layar'''
		print(self.buffer)
		
	def test_write(self):
		'''menulis isi source dan buffer ke pegawai.json'''
		with open('data/pegawai.json','w') as srce:
			x = json.dumps(sumber + self.buffer)
			srce.write(x)

if __name__ == '__main__':
	main()
