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
		this_data = json.load(srce)
	return this_data

"""fungsi untuk merubah input yang berformat string dari user menjadi datetime"""
def test_get_input(arg):
	x = input(arg )
	return dt.strptime(x,'%Y-%m-%d')

"""fungsi untuk merubah input yang berformat string dari jadwal menjadi datetime"""
def test_gethour(arg):
	return dt.strptime(arg,'%H:%M')

"""menghitung berapa lama pegawai terlambat"""
def test_late_in(hour_in,check_in,tolerance):
	if check_in > hour_in:
		if (check_in - hour_in) < tolerance:
			return td(seconds=0)
		else:
			return check_in - hour_in
	else:
		return td(seconds=0)

"""menghitung berapa lama pegawai pulang lebih awal"""
def test_early_out(hour_out,check_out,tolerance):
	if hour_out > check_out:
		if (hour_out - check_out) < tolerance:
			return td(seconds=0)
		else:
			return hour_out - check_out
	else:
		return td(seconds=0)

"""menghitung lembur"""
def test_overtime(hour_in,hour_out,check_in,check_out):
	if check_in < hour_in and check_out > hour_out:
		return (hour_in - check_in)+(check_out - hour_out)
	elif check_in < hour_in and check_out < hour_out:
		return hour_in - check_in
	elif check_in > hour_in and check_out > hour_out:
		return check_out - hour_out
	else:
		return td(seconds=0)

"""menghitung jam kerja minus telat dan pulang awal"""
def test_worktime(hour_in,hour_out,check_in,check_out):
	if check_in > hour_in:
		return hour_out - check_in
	elif check_out > hour_out:
		return check_out - hour_in
	else:
		return hour_out - hour_in

def test_totaltime(check_in,check_out):
	return (check_out - check_in)

"""menghitung jam lembur dalam desimal"""
def test_overtype(hour_in,check_in):
	if test_overtime > 0:
		return round((hour_in - check_in)/td(hours=1),2)
	else:
		return td(seconds=0)

"""fungsi untuk memproses pegawai tanggal waktu dan input ke buffer"""
def test_process(start,end,buffer):
	"""start = tanggal mulai"""
	"""end = tanggal akhir """
	"""buffer berfungsi sebagai penampung data"""
	
	"""ambil library yang dibutuhkan"""
	employee = test_get_data('data/pegawai.json')
	schedule = test_get_data('data/jadwal.json')
	subdata = test_get_data('data/judul.json')
	holiday = list(test_get_data('data/libur.json'))
	
	"""daftar tanggal"""
	delta = end - start
	
	"""looping pegawai"""
	for x in range(len(employee)):
		x = x + 1
		"""looping tanggal"""
		for day in range(delta.days+1):
			
			"""tentukan tangal"""
			thisday = start + td(days = day)
			"""isi data tanggal dan data pegawai"""
			data = subdata
			data["Tanggal"] = thisday.strftime('%Y-%m-%d')
			data["NoPeg"] = employee[str(x)]['nopeg']
			data["No. Akun"] = employee[str(x)]['akun']
			data["No."] = employee[str(x)]['nomor']
			data["Nama"] = employee[str(x)]['nama']
			data["Auto-Assign"] = '0'
			data["Status"] = ' '
			data["Hrs C/In"] = ' '
			data["Hrs C/Out"] = ' '
			data["Departemen"] = employee[str(x)]['dpt']
			data["Waktu real"] = '1'
			
			"""fungsi untuk mengisi waktu"""
			if thisday in holiday:
				"""hari libur"""
				thisday_schedule = data["Jam Kerja"] = schedule["0"]["name"]
				hour_in = data["Awal tugas"] = test_gethour(schedule["0"]['hour start'])
				hour_out = data["Akhir tugas"] = test_gethour(schedule["0"]['hour end'])
				check_in = data["Masuk"] = td(seconds = 0)
				check_out = data["Keluar"] = td(seconds = 0)
				late_in = data["Telat"] = test_late_in(hour_in,check_in,test_gethour(schedule["0"]['late in']))
				early_out = data["Plg Awal"] = test_early_out(hour_out,check_out,test_gethour(schedule["0"]['early out']))
				overtime = data["Waktu Lembur"] = test_overtime(hour_in,hour_out,check_in,check_out)
				worktime = data["Waktu Kerja"] = test_worktime(hour_in,hour_out,check_in,check_out)
				totaltime = data["Lama Hadir"] = test_totaltime(check_in,check_out)
				data["Libur Lembur"] = test_overtype(hour_in,check_in)
				data["NDays"] = '0'
				data["Akhir Pekan"] = '0'
				data["Hari Libur"] = '0'
				data["NDays_OT"] = '0'
				data["Lembur A.Pekan"] = '0'
				if check_in == td(seconds = 0) or late_in > test_gethour(schedule["0"]["checkin max"]) or check_out < test_gethour(schedule["0"]["checkin max"]):
					data["Bolos"] = '1'
				else : 
					data["Bolos"] = '0'	
			else:
				if thisday.weekday == 6:
					"""hari minggu """
					thisday_schedule = data["Jam Kerja"] = schedule[2]["name"]
					hour_in = data["Awal tugas"] = test_gethour(schedule[2]['hour start'])
					hour_out = data["Akhir tugas"] = test_gethour(schedule[2]['hour end'])
					check_in = data["Masuk"] = check_in = td(hours = ri(7,8))
					check_in = data["Masuk"] = td(seconds = 0)
					check_out = data["Keluar"] = td(seconds = 0)
					check_out = data["Keluar"] = td(hours = ri(15,18), minutes = ri(0,59),seconds = ri(0,59))
					late_in = data["Telat"] = test_late_in(hour_in,check_in,test_gethour(schedule[2]['late in']))
					early_out = data["Plg Awal"] = test_early_out(hour_out,check_out,test_gethour(schedule[2]['early out']))
					overtime = data["Waktu Lembur"] = test_overtime(hour_in,hour_out,check_in,check_out)
					worktime = data["Waktu Kerja"] = test_worktime(hour_in,hour_out,check_in,check_out)
					totaltime = data["Lama Hadir"] = test_totaltime(check_in,check_out)
					data["Libur Lembur"] = '0'
					data["NDays"] = '0'
					data["Akhir Pekan"] = '0'
					data["Hari Libur"] = '0'
					data["NDays_OT"] = '0'
					data["Lembur A.Pekan"] = test_overtype(hour_in,check_in)
					if check_in == td(seconds = 0) or late_in > test_gethour(schedule[1]["checkin max"]) or check_out < test_gethour(schedule[1]["checkin max"]):
						data["Bolos"] = '1'
					else : 
						data["Bolos"] = '0'	
		
				elif thisday.weekday == 5:
					"""hari sabtu """
					thisday_schedule = data["Jam Kerja"] = schedule[2]["name"]
					hour_in = data["Awal tugas"] = test_gethour(schedule[2]['hour start'])
					hour_out = data["Akhir tugas"] = test_gethour(schedule[2]['hour end'])
					check_in = data["Masuk"] = check_in = td(hours = ri(7,8))
					check_in = data["Masuk"] = td(seconds = 0)
					check_out = data["Keluar"] = td(seconds = 0)
					check_out = data["Keluar"] = td(hours = ri(15,18), minutes = ri(0,59),seconds = ri(0,59))
					late_in = data["Telat"] = test_late_in(hour_in,check_in,test_gethour(schedule[2]['late in']))
					early_out = data["Plg Awal"] = test_early_out(hour_out,check_out,test_gethour(schedule[2]['early out']))
					overtime = data["Waktu Lembur"] = test_overtime(hour_in,hour_out,check_in,check_out)
					worktime = data["Waktu Kerja"] = test_worktime(hour_in,hour_out,check_in,check_out)
					totaltime = data["Lama Hadir"] = test_totaltime(check_in,check_out)
					data["Libur Lembur"] = '0'
					data["NDays"] = '0'
					data["Akhir Pekan"] = '0'
					data["Hari Libur"] = '0'
					data["NDays_OT"] = '0'
					data["Lembur A.Pekan"] = test_overtype(hour_in,check_in)
					if check_in == td(seconds = 0) or late_in > test_gethour(schedule[2]["checkin max"]) or check_out < test_gethour(schedule[2]["checkin max"]):
						data["Bolos"] = '1'
					else : 
						data["Bolos"] = '0'	
				else:
					"""hari senin sampai jumat"""
					thisday_schedule = data["Jam Kerja"] = schedule[1]["name"]
					hour_in = data["Awal tugas"] = test_gethour(schedule[1]['hour start'])
					hour_out = data["Akhir tugas"] = test_gethour(schedule[1]['hour end'])
					check_in = data["Masuk"] = check_in = td(hours = ri(7,8))
					check_in = data["Masuk"] = td(hours = ri(7,8))
					if check_in.hours == 8:
						check_in + td(minutes = ri(0,15),seconds = ri(0,59))
					else:
						check_in + td(minutes = ri(0,59),seconds = ri(0,59))
					check_out = data["Keluar"] = td(hours = ri(15,18), minutes = ri(0,59),seconds = ri(0,59))
					late_in = data["Telat"] = test_late_in(hour_in,check_in,test_gethour(schedule[1]['late in']))
					early_out = data["Plg Awal"] = test_early_out(hour_out,check_out,test_gethour(schedule[1]['early out']))
					overtime = data["Waktu Lembur"] = test_overtime(hour_in,hour_out,check_in,check_out)
					worktime = data["Waktu Kerja"] = test_worktime(hour_in,hour_out,check_in,check_out)
					totaltime = data["Lama Hadir"] = test_totaltime(check_in,check_out)
					data["Libur Lembur"] = '0'
					data["NDays"] = '0'
					data["Akhir Pekan"] = '0'
					data["Hari Libur"] = '0'
					data["NDays_OT"] = '0'
					data["Lembur A.Pekan"] = test_overtype(hour_in,check_in)
					if check_in == td(seconds = 0) or late_in > test_gethour(schedule[1]["checkin max"]) or check_out < test_gethour(schedule[1]["checkin max"]):
						data["Bolos"] = '1'
					else : 
						data["Bolos"] = '0'	
			
			"""mengisi data ke buffer"""
			buffer.append(data)
	return buffer

"""fungsi ouput dengan 5 pilihan : layar, excell, JSON, csv, text"""

def test_print(buffer):
	"""output ke layar"""
	for i in buffer:
		print(i)


def test_excell(file_title,buffer):
	"""output ke excell"""
	
	"""membaca data header dari judul.json"""
	with open('data/judul.json','r') as head_data:
		header = list(json.load(head_data).keys())
	
	book = Workbook()
	sheet = self.book.active
	sheet.title = file_title
	"""daftar kolom untuk excell ouput"""
	self.column = list(string.ascii_uppercase)+['AA','AB','AC']
	"""header untuk mengisi baris pertama"""
	for i in range(len(header)):
		self.sheet.cell(column=i+1,row=1, value=header[i])

	"""isi sheet dari buffer"""
	for x in range(len(buffer)):
		z=list(self.buffer[x].values())
		for y in range(len(column)):
			self.sheet.cell(column=y+1,row=x+2,value=(z[y]))

	"""save ke excell"""
	wb.save('{}.xlsx'.format(file_title))
	wb.close()

def test_json(file_title,buffer):
	"""output ke json"""
	with open('{}.json'.format(file_title),'w') as jsonfile:
		json.dump(buffer)

def test_csv(file_title,buffer):
	"""output ke csv"""
	with open('{}.csv'.format(file_title), 'w', dialect='excell', newline='') as csvfile:
		x = csv.writer(csvfile, delimiter=',',quotechar='"')
		for i in buffer:
			x.writerow(i)

def test_txt(file_title,buffer):
	"""output ke text"""
	with open('{}.txt'.format(file_title), 'w') as txtfile:
		txtfile.write(buffer)

def test_option(file_title,func,buffer):
	if file_title == None:
		file_title = dt.today().strftime('%Y-%m-%d.%H.%M.%s')
		
	func(file_title,buffer)

"""salam pembuka"""
print("""
SELAMAT DATANG DI ABTOMATIS
MODUL PENGISI ABSENSI OTOMATIS
""")

def main():
	"""mengambil data pegawai,jadwal,judul,libur"""
	pegawai = test_get_data('data/pegawai.json')
	jadwal = test_get_data('data/jadwal.json')
	judul = test_get_data('data/judul.json')
	libur = test_get_data('data/libur.json')

	print("""
	metode pengisian :
	masukkan tanggal awal dan akhir dengan format YYYY-MM-DD dimana 
	YYYY = 4 angka tahun
	MM = 2 angka bulan 
	DD = 2 angka tanggal
	""")
	
	"""tanya tanggal awal dan akhir otomatis"""
	awal = dt(2020,10,10,0) #getd(' masukkan tanggal awal absensi: ') 
	akhir = dt(2020,10,20,0) #getd(' masukkan tanggal akhir absensi: ')
	hasil = []
	
	"""tanya tanggal awal dan akhir lewat input (nonaktif)
	awal = test_get_input(' masukkan tanggal awal absensi: ')
	akhir = test_get_input(' masukkan tanggal akhir absensi: ')
	""" 
	
	"""main proses"""
	test_process(awal,akhir,hasil)
	
			
	print("""
	pilih format output dari 5 opsi
	0 = layar
	1 = excel
	2 = JSON
	3 = csv
	4 = text
	""")
	def test_output():
		opsi = input (" opsi : ")
		if opsi == 0:
			test_print()
		elif opsi == 1:
			judul_opsi = input("beri judul : " )
			test_option(judul_opsi,test_excell(),hasil)
		elif opsi == 2:
			judul_opsi = input("beri judul : " )
			test_option(judul_opsi,test_json(),hasil)
		elif opsi == 3:
			judul_opsi = input("beri judul : " )
			test_option(judul_opsi,test_csv(),hasil)
		elif opsi == 4:
			judul_opsi = input("beri judul : " )
			test_option(judul_opsi,test_txt(),hasil)
		else:
			print("pilihan anda tidak ada dalm daftar \n ulangi lagi?")
			answer = input("jawab Y atau N: ")
			if answer.lower() == 'y':
				return test_output()
			else:
				pass
	
	print("ulangi proses ?")
	answer = input("jawab Y atau N: ")
	if answer.lower() == 'y':
		return main()
	else:
		pass

if __name__=='__main__':
	main()
