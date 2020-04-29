#!/usr/bin/env python3
"""
Absensi
"""

__author__ = "bringsik100"
__version__ = "0.1.3b"
__license__ = "MIT"

"""
alur program
+ import library
+ deklarasi fungsi objek
- fungsi ambil data pegawai, jadwal, judul, liburan
- fungsi perubah input 
- fungsi tanggal
- fungsi waktu
- fungsi output
+ fungsi main()
- salam pembuka
- dict template penampung < pegawai < tanggal < waktu < data
- input pegawai
- input tanggal
- input waktu
- pilih format output
- ulangi atau selesai
"""

"""import library"""
from random import randint as ri
import datetime as dd
from datetime import datetime as dt
from datetime import timedelta as td
import string
import json
from openpyxl import Workbook
import pytest

"""fungsi ambil data pegawai, jadwal, judul, liburan"""
def test_get_data(source):
	with open(source,'r') as srce:
		return json.load(srce)

"""fungsi untuk merubah input yang berformat string menjadi datetime"""
def test_get_input(arg):
	x = input(arg)
	return dt.strptime(x,'%Y-%m-%d')

"""fungsi untuk membuat daftar tanggal"""
def test_dates(start,end):
	delta = end - start
	dates = []
	for day in range(delta.days+1):
		dates.append(start + day)
	return dates

'''menghitung berapa lama pegawai terlambat'''
def test_late_in(hour_in,check_in):
	if check_in > hour_in:
		if (check_in - hour_in) < td(minutes = 10):
			return td(seconds=0)
		else:
			return check_in - hour_in
	else:
		return td(seconds=0)

'''menghitung berapa lama pegawai pulang lebih awal'''
def test_early_out(hour_out,check_out):
	if hour_out > check_out:
		if (hour_out - check_out) < td(minutes = 5):
			return td(seconds=0)
		else:
			return hour_out - check_out
	else:
		return td(seconds=0)

'''menghitung lembur'''
def test_overtime(hour_in,hour_out,check_in,check_out):
	if check_in < hour_in and check_out > hour_out:
		return (hour_in - check_in)+(check_out - hour_out)
	elif check_in < hour_in and check_out < hour_out:
		return hour_in - check_in
	elif check_in > hour_in and check_out > hour_out:
		return check_out - hour_out
	else:
		return td(seconds=0)

'''menghitung jam kerja minus telat dan pulang awal'''
def test_worktime(hour_in,hour_out,check_in,check_out):
	if check_in > hour_in:
		return hour_out - check_in
	elif check_out > hour_out:
		return check_out - hour_in
	else:
		return hour_out - hour_in

def test_totaltime(check_in,check_out):
	return (check_out - check_in)

'''menghitung jam lembur dalam desimal'''
def test_overtype(hour_in,check_in):
	if test_overtime > 0:
		return round((hour_in - check_in)/td(hours=1),2)
	else:
		return " "

"""fungsi untuk mengisi waktu"""
def test_times(date,holidays):
	"""holidays harus berupa list"""
	if date in holidays:
		"""hari libur"""
		schedule = "holiday"
		hour_in = td(seconds = 0)
		hour_out = td(seconds = 0)
		check_in = td(seconds = 0)
		check_out = td(seconds = 0)
		test_late_in(hour_in,check_in)
		test_early_out(hour_in,check_in)
		test_overtime(hour_in,hour_out,check_in,check_out)
		test_worktime(hour_in,hour_out,check_in,check_out)
		test_totaltime(check_in,check_out)
		test_overtype(hour_in,check_in)
		normal = 0
		
	else:
		if date.weekday == 6:
			"""hari minggu """
			schedule = "sunday"
			hour_in = td(seconds = 0)
			hour_out = td(seconds = 0)
			check_in = td(seconds = 0)
			check_out = td(seconds = 0)
			test_late_in(hour_in,check_in)
			test_early_out(hour_in,check_in)
			test_overtime(hour_in,hour_out,check_in,check_out)
			test_worktime(hour_in,hour_out,check_in,check_out)
			test_totaltime(check_in,check_out)
			test_overtype(hour_in,check_in)
			normal = 0
		
		elif date.weekday == 5:
			"""hari sabtu """
			schedule = "saturday"
			hour_in = td(hours = 8)
			hour_out = td(hours = 13)
			check_in = td(hours = ri(7,8))
			if check_in.hours == 8:
				check_in + td(minutes = ri(0,15),seconds = ri(0,59))
			else:
				check_in + td(minutes = ri(0,59),seconds = ri(0,59))
			check_out = td(hours = ri(15,18), minutes = ri(0,59),seconds = ri(0,59))
			test_late_in(hour_in,check_in)
			test_early_out(hour_in,check_in)
			test_overtime(hour_in,hour_out,check_in,check_out)
			test_worktime(hour_in,hour_out,check_in,check_out)
			test_totaltime(check_in,check_out)
			test_overtype(hour_in,check_in)
			normal = 1
		
		else:
			"""senin s/d jumat"""
			schedule = "normal day"
			hour_in = td(hours = 8)
			hour_out = td(hours = 16)
			check_in = td(hours = ri(7,8))
			if check_in.hours == 8:
				check_in + td(minutes = ri(0,15),seconds = ri(0,59))
			else:
				check_in + td(minutes = ri(0,59),seconds = ri(0,59))
			check_out = td(hours = ri(15,18), minutes = ri(0,59),seconds = ri(0,59))
			test_late_in(hour_in,check_in)
			test_early_out(hour_in,check_in)
			test_overtime(hour_in,hour_out,check_in,check_out)
			test_worktime(hour_in,hour_out,check_in,check_out)
			test_totaltime(check_in,check_out)
			test_overtype(hour_in,check_in)

"""fungsi ouput dengan 4 pilihan : layar, excell,  """
class test_out_put:
	'''fungsi untuk output'''
	def __init__(self,buffer):
		'''buffer data dari main skrip'''
		self.buffer = buffer

	def test_print(self):
		'''output ke layar'''
		for i in self.buffer:
			print(i)

	def test_header(self):
		'''membaca data header dari judul.json'''
		with open('data/judul.json','r') as head_data:
			return list(json.load(head_data).keys())

	def test_excell(self,title):
		'''output ke excell'''
		self.book = Workbook()
		self.sheet = self.book.active
		self.sheet.title = 'Absensi'
		'''daftar kolom untuk excell ouput'''
		self.column = list(string.ascii_uppercase)+['AA','AB','AC']
		'''header untuk mengisi baris pertama'''
		for i in range(len(self.test_header)):
			self.sheet.cell(column=i+1,row=1, value=header[i])

		'''isi sheet dari buffer'''
		for x in range(len(self.buffer)):
			z=list(self.buffer[x].values())
			for y in range(len(column)):
				self.sheet.cell(column=y+1,row=x+2,value=(z[y]))

		'''save ke excell'''
		wb.save('{}.xlsx'.format(self.sheet.title))

	def test_json(self,title):
		'''output ke json'''
		self.title = title
		with open('{}.json'.format(self.title),'w') as outj:
			json.dump(self.buffer)

		def test_csv(self,title):
			'''output ke csv'''
			self.title = title
			with open('{}.csv'.format(self.title), 'w', dialect='excell', newline='') as csvfile:
				x = csv.writer(csvfile, delimiter=',',quotechar='"')
				for i in self.buffer:
					for g in i:
						x.writerow(g)


"""salam pembuka"""
print("""
SELAMAT DATANG DI ABTOMATIS
MODUL PENGISI ABSENSI OTOMATIS
""")

def main():
	"""template data"""
	template = {
	"NoPeg": " ",
	"No. Akun": " ",
	"No.": " ",
	"Nama": " ",
	"Auto-Assign": " ",
	"Tanggal": " ",
	"Jam Kerja": " ",
	"Awal tugas": " ",
	"Akhir tugas": " ",
	"Masuk": " ",
	"Keluar": " ",
	"Normal": " ",
	"Waktu real": " ",
	"Telat": " ",
	"Plg Awal": " ",
	"Bolos": " ",
	"Waktu Lembur": " ",
	"Waktu Kerja": " ",
	"Status": " ",
	"Hrs C/In": " ",
	"Hrs C/Out": " ",
	"Departemen": " ",
	"NDays": " ",
	"Akhir Pekan": " ",
	"Hari Libur": " ",
	"Lama Hadir": " ",
	"NDays_OT": " ",
	"Lembur A.Pekan": " ",
	"Libur Lembur": " "}

	"""mengambil data pegawai,jadwal,judul,libur"""
	pegawai = test_get_data('data/pegawai.json')
	jadwal = test_get_data('data/jadwal.json')
	judul = test_get_data('data/judul.json')
	liburan = test_get_data('data/libur.json')

	print("""
	metode pengisian :
	masukkan tanggal awal dan akhir dengan format YYYY-MM-DD dimana 
	YYYY = 4 angka tahun
	MM = 2 angka bulan 
	DD = 2 angka tanggal
	""")
	
	'''tanya tanggal awal dan akhir otomatis'''
	awal = dt(2020,10,10,0) #getd(' masukkan tanggal awal absensi: ')
	akhir = dt(2020,10,20,0) #getd(' masukkan tanggal akhir absensi: ')
	
	'''tanya tanggal awal dan akhir lewat input (nonaktif)
	awal = test_get_input(' masukkan tanggal awal absensi: ')
	akhir = test_get_input(' masukkan tanggal akhir absensi: ')
	'''
	buffer = []
	"""pengisian data ke dalam buffer"""
	"""looping pegawai"""
	for item in range(len(pegawai)):
		data = template
		data["NoPeg"] = pegawai[item]['nopeg']
		data["No. Akun"] = pegawai[item]['akun']
		data["No."] = pegawai[item]['nomor']
		data["Nama"] = pegawai[item]['nama']
		data["Auto-Assign"] = '0'
		data["Status"] = ' '
		data["Hrs C/In"] = ' '
		data["Hrs C/Out"] = ' '
		data["Departemen"] = pegawai[item]['dept']
		data["NDays"] = '1'
		data["Waktu real"] = '1'
		"""looping tanggal"""
		tanggal = test_dates(awal,akhir)
		"""pengisian waktu"""
		for hari in tanggal:
			waktu = test_times(hari,libur)
			data["Tanggal"] = hari
			data["Jam Kerja"] = waktu.schedule
			data["Awal tugas"] = waktu.hour_in
			data["Akhir tugas"] = waktu.hour_out
			data["Masuk"] = waktu.check_in
			data["Keluar"] = waktu.check_out
			data["Telat"] = waktu.test_late_in
			data["Plg Awal"] = waktu.test_early_out
			if waktu.check_in == 0:
				data["Bolos"] = 'True'
			else: 
				data["Bolos"] = ' '
			data["Waktu Lembur"] = waktu.test_overtime
			data["Waktu Kerja"] = waktu.test_worktime
			if hari.weekday == 5 or hari.weekday == 6:
				data["Akhir Pekan"] = '1'
				data["Lembur A.Pekan"] = waktu.test_overtype
			else :
				data["Akhir Pekan"] = ' '
				data["NDays_OT"] = waktu.test_overtype
			if waktu.schedule == 'holiday':
				data["Hari Libur"] = '1'
			else:
				data["Hari Libur"] = '0'
			data["Lama Hadir"] = waktu.test_totaltime
			data["Libur Lembur"] = '0'
		buffer.append(data)
		print(buffer)

if __name__=='__main__':
	main()
