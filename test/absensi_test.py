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
import csv
from openpyxl import Workbook
#import pytest

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
	x = dt.strptime(arg,'%H:%M')
	return td(hours = x.hour, minutes = x.minute)

def test_getstring(day,delta):
	x = day + delta
	return x.strftime('%H:%M')

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
def test_overtype(hour_in,hour_out,check_in,check_out):
	if check_in < hour_in and check_out > hour_out:
		return round(((hour_in - check_in)+(check_out - hour_out))/td(hours = 1),2)
	elif check_in < hour_in and check_out < hour_out:
		return round((hour_in - check_in)/td(hours = 1),2)
	elif check_in > hour_in and check_out > hour_out:
		return round((check_out - hour_out)/td(hours = 1),2)
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
			data = subdata
			"""fungsi untuk mengisi waktu"""
			if thisday in holiday:
				"""hari libur"""
				thisday_schedule = schedule["0"]["name"]
				hour_in = test_gethour(schedule["0"]['hour start'])
				hour_out = test_gethour(schedule["0"]['hour end'])
				check_in = td(seconds = 0)
				check_out = td(seconds = 0)
				late_in = test_late_in(hour_in,check_in,test_gethour(schedule["0"]['late in']))
				early_out = test_early_out(hour_out,check_out,test_gethour(schedule["0"]['early out']))
				overtime = test_overtime(hour_in,hour_out,check_in,check_out)
				worktime = test_worktime(hour_in,hour_out,check_in,check_out)
				totaltime = test_totaltime(check_in,check_out)
				overtype = test_overtype(hour_in,hour_out,check_in,check_out)
				
				"""isi data tanggal dan data pegawai"""
				data["NoPeg"] = employee[str(x)]['nopeg']
				data["No. Akun"] = employee[str(x)]['akun']
				data["No."] = employee[str(x)]['nomor']
				data["Nama"] = employee[str(x)]['nama']
				data["Auto-Assign"] = '0'
				data["Tanggal"] = thisday.strftime('%Y-%m-%d')
				data["Jam Kerja"] = schedule["0"]["name"]
				data["Awal tugas"] = schedule["0"]['hour start']
				data["Akhir tugas"] = schedule["0"]['hour end']
				data["Masuk"] = test_getstring(thisday,check_in)
				data["Keluar"] = test_getstring(thisday,check_out)
				data["Normal"] = ' '
				data["Waktu real"] = '1'
				data["Telat"] = test_getstring(thisday,late_in)
				data["Plg Awal"] = test_getstring(thisday,early_out)
				if check_in == td(seconds = 0) or late_in > test_gethour(schedule["0"]["checkin max"]) or check_out < test_gethour(schedule["0"]["checkin max"]):
					data["Bolos"] = 'True'
				else : 
					data["Bolos"] = ' '	
				data["Waktu Lembur"] = test_getstring(thisday,overtime)
				data["Waktu Kerja"] = test_getstring(thisday,worktime)
				data["Lama Hadir"] = test_getstring(thisday,totaltime)
				data["Status"] = ' '
				data["Hrs C/In"] = ' '
				data["Hrs C/Out"] = ' '
				data["Departemen"] = employee[str(x)]['dpt']
				data["NDays"] = ' '
				data["Akhir Pekan"] = ' '
				data["Hari Libur"] = ' '
				data["NDays_OT"] = ' '
				data["Lembur A.Pekan"] = ' '
				data["Libur Lembur"] = str(overtype)
				buffer.append(data)
			else:
			
				if thisday.weekday == 6:
					"""hari minggu """
					thisday_schedule = schedule["2"]["name"]
					hour_in = test_gethour(schedule["2"]['hour start'])
					hour_out = test_gethour(schedule["2"]['hour end'])
					check_in = td(seconds = 0)
					check_out = td(seconds = 0)
					late_in = test_late_in(hour_in,check_in,test_gethour(schedule["2"]['late in']))
					early_out = test_early_out(hour_out,check_out,test_gethour(schedule["2"]['early out']))
					overtime = test_overtime(hour_in,hour_out,check_in,check_out)
					worktime = test_worktime(hour_in,hour_out,check_in,check_out)
					totaltime = test_totaltime(check_in,check_out)
					overtype = test_overtype(hour_in,hour_out,check_in,check_out)
					
					data["NoPeg"] = employee[str(x)]['nopeg']
					data["No. Akun"] = employee[str(x)]['akun']
					data["No."] = employee[str(x)]['nomor']
					data["Nama"] = employee[str(x)]['nama']
					data["Auto-Assign"] = '0'
					data["Tanggal"] = thisday.strftime('%Y-%m-%d')
					data["Jam Kerja"] = schedule["2"]["name"]
					data["Awal tugas"] = schedule["2"]['hour start']
					data["Akhir tugas"] = schedule["2"]['hour end']
					data["Masuk"] = test_getstring(thisday,check_in)
					data["Keluar"] = test_getstring(thisday,check_out)
					data["Normal"] = ' '
					data["Waktu real"] = '1'
					data["Telat"] = test_getstring(thisday,late_in)
					data["Plg Awal"] = test_getstring(thisday,early_out)
					if check_in == td(seconds = 0) or late_in > test_gethour(schedule["2"]["checkin max"]) or check_out < test_gethour(schedule["0"]["checkin max"]):
						data["Bolos"] = 'True'
					else : 
						data["Bolos"] = ' '	
					data["Waktu Lembur"] = test_getstring(thisday,overtime)
					data["Waktu Kerja"] = test_getstring(thisday,worktime)
					data["Lama Hadir"] = test_getstring(thisday,totaltime)
					data["Status"] = ' '
					data["Hrs C/In"] = ' '
					data["Hrs C/Out"] = ' '
					data["Departemen"] = employee[str(x)]['dpt']
					data["NDays"] = ' '
					data["Akhir Pekan"] = ' '
					data["Hari Libur"] = ' '
					data["NDays_OT"] = ' '
					data["Lembur A.Pekan"] = ' '
					data["Libur Lembur"] = str(overtype)
					buffer.append(data)
		
				elif thisday.weekday == 5:
					"""hari sabtu """
					thisday_schedule = data["Jam Kerja"] = schedule["2"]["name"]
					hour_in = test_gethour(schedule["2"]['hour start'])
					hour_out = test_gethour(schedule["2"]['hour end'])
					check_in = td(hours = ri(7,8))
					if check_in == td(hours=8):
						check_in + td(minutes = ri(0,15),seconds = ri(0,59))
					else:
						check_in + td(minutes = ri(0,59),seconds = ri(0,59))
					check_out = td(hours = ri(15,18), minutes = ri(0,59),seconds = ri(0,59))
					late_in = test_late_in(hour_in,check_in,test_gethour(schedule["2"]['late in']))
					early_out = test_early_out(hour_out,check_out,test_gethour(schedule["2"]['early out']))
					overtime = test_overtime(hour_in,hour_out,check_in,check_out)
					worktime = test_worktime(hour_in,hour_out,check_in,check_out)
					totaltime = test_totaltime(check_in,check_out)
					overtype = test_overtype(hour_in,hour_out,check_in,check_out)
					
					data["NoPeg"] = employee[str(x)]['nopeg']
					data["No. Akun"] = employee[str(x)]['akun']
					data["No."] = employee[str(x)]['nomor']
					data["Nama"] = employee[str(x)]['nama']
					data["Auto-Assign"] = '0'
					data["Tanggal"] = thisday.strftime('%Y-%m-%d')
					data["Jam Kerja"] = schedule["2"]["name"]
					data["Awal tugas"] = schedule["2"]['hour start']
					data["Akhir tugas"] = schedule["2"]['hour end']
					data["Masuk"] = test_getstring(thisday,check_in)
					data["Keluar"] = test_getstring(thisday,check_out)
					data["Normal"] = ' '
					data["Waktu real"] = '1'
					data["Telat"] = test_getstring(thisday,late_in)
					data["Plg Awal"] = test_getstring(thisday,early_out)
					if check_in == td(seconds = 0) or late_in > test_gethour(schedule["2"]["checkin max"]) or check_out < test_gethour(schedule["0"]["checkin max"]):
						data["Bolos"] = 'True'
					else : 
						data["Bolos"] = ' '	
					data["Waktu Lembur"] = test_getstring(thisday,overtime)
					data["Waktu Kerja"] = test_getstring(thisday,worktime)
					data["Lama Hadir"] = test_getstring(thisday,totaltime)
					data["Status"] = ' '
					data["Hrs C/In"] = ' '
					data["Hrs C/Out"] = ' '
					data["Departemen"] = employee[str(x)]['dpt']
					data["NDays"] = ' '
					data["Akhir Pekan"] = ' '
					data["Hari Libur"] = ' '
					data["NDays_OT"] = ' '
					data["Lembur A.Pekan"] = str(overtype)
					data["Libur Lembur"] = ' '
					buffer.append(data)
				else:
					"""hari senin sarmpai jumat"""
					thisday_schedule = data["Jam Kerja"] = schedule["1"]["name"]
					hour_in = test_gethour(schedule["1"]['hour start'])
					hour_out = test_gethour(schedule["1"]['hour end'])
					check_in = td(hours = ri(7,8))
					if check_in == td(hours=8):
						check_in + td(minutes = ri(0,15),seconds = ri(0,59))
					else:
						check_in + td(minutes = ri(0,59),seconds = ri(0,59))
					check_out = td(hours = ri(15,18), minutes = ri(0,59),seconds = ri(0,59))
					late_in = test_late_in(hour_in,check_in,test_gethour(schedule["1"]['late in']))
					early_out = test_early_out(hour_out,check_out,test_gethour(schedule["1"]['early out']))
					overtime = test_overtime(hour_in,hour_out,check_in,check_out)
					worktime = test_worktime(hour_in,hour_out,check_in,check_out)
					totaltime = test_totaltime(check_in,check_out)
					overtype = test_overtype(hour_in,hour_out,check_in,check_out)
					
					data["NoPeg"] = employee[str(x)]['nopeg']
					data["No. Akun"] = employee[str(x)]['akun']
					data["No."] = employee[str(x)]['nomor']
					data["Nama"] = employee[str(x)]['nama']
					data["Auto-Assign"] = ' '
					data["Tanggal"] = thisday.strftime('%Y-%m-%d')
					data["Jam Kerja"] = schedule["1"]["name"]
					data["Awal tugas"] = schedule["1"]['hour start']
					data["Akhir tugas"] = schedule["1"]['hour end']
					data["Masuk"] = test_getstring(thisday,check_in)
					data["Keluar"] = test_getstring(thisday,check_out)
					data["Normal"] = ' '
					data["Waktu real"] = '1'
					data["Telat"] = test_getstring(thisday,late_in)
					data["Plg Awal"] = test_getstring(thisday,early_out)
					if check_in == td(seconds = 0) or late_in > test_gethour(schedule["1"]["checkin max"]) or check_out < test_gethour(schedule["0"]["checkin max"]):
						data["Bolos"] = 'True'
					else : 
						data["Bolos"] = ' '	
					data["Waktu Lembur"] = test_getstring(thisday,overtime)
					data["Waktu Kerja"] = test_getstring(thisday,worktime)
					data["Lama Hadir"] = test_getstring(thisday,totaltime)
					data["Status"] = ' '
					data["Hrs C/In"] = ' '
					data["Hrs C/Out"] = ' '
					data["Departemen"] = employee[str(x)]['dpt']
					data["NDays"] = ' '
					data["Akhir Pekan"] = ' '
					data["Hari Libur"] = ' '
					data["NDays_OT"] = str(overtype)
					data["Lembur A.Pekan"] = ' '
					data["Libur Lembur"] = ' '
					buffer.append(data)
			
			"""mengisi data ke buffer"""
			
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
	sheet = book.active
	sheet.title = file_title
	"""daftar kolom untuk excell ouput"""
	column = list(string.ascii_uppercase)+['AA','AB','AC']
	"""header untuk mengisi baris pertama"""
	for i in range(len(header)):
		sheet.cell(column=i+1,row=1, value=header[i])

	"""isi sheet dari buffer"""
	for x in range(len(buffer)):
		z=list(buffer[x].values())
		for y in range(len(column)):
			sheet.cell(column=y+1,row=x+2,value=(z[y]))

	"""save ke excell"""
	book.save('{}.xlsx'.format(file_title))
	book.close()

def test_json(file_title,buffer):
	"""output ke json"""
	with open('{}.json'.format(file_title),'w') as jsonfile:
		json.dumps(buffer)

def test_csv(file_title,buffer):
	"""output ke csv"""
	with open(f'{file_title}.csv', 'w', newline='') as csvfile:
		x = csv.writer(csvfile, delimiter=',',quotechar='"')
		for i in buffer:
			x.writerow(i)

def test_txt(file_title,buffer):
	"""output ke text"""
	with open('{}.txt'.format(file_title), 'w') as txtfile:
			txtfile.write(json.dumps(buffer))

"""salam pembuka"""
print("""
SELAMAT DATANG DI ABTOMATIS
MODUL PENGISI ABSENSI OTOMATIS
""")

def main():

	print("""
	metode pengisian :
	masukkan tanggal awal dan akhir dengan format YYYY-MM-DD dimana 
	YYYY = 4 angka tahun
	MM = 2 angka bulan 
	DD = 2 angka tanggal
	""")
	
	"""tanya tanggal awal dan akhir otomatis"""
	awal = test_get_input(' masukkan tanggal awal absensi: ') 
	akhir = test_get_input(' masukkan tanggal akhir absensi: ')
	hasil = []
	
	"""tanya tanggal awal dan akhir lewat input (nonaktif)
	awal = test_get_input(' masukkan tanggal awal absensi: ')
	akhir = test_get_input(' masukkan tanggal akhir absensi: ')
	""" 
	
	"""main proses"""
	test_process(awal,akhir,hasil)
	
			

	def test_output():
		print("""
		pilih format output dari 5 opsi
		 0 = layar
		 1 = excel
		 2 = JSON
		 3 = csv
		 4 = text
		""")
		opsi = input (" opsi : ")
		if int(opsi) == 0:
			test_print(hasil)
		
		elif int(opsi) == 1:
			judul_opsi = input("beri judul : " )
			if judul_opsi == None:
				judul_blank = dt.today.strftime('%Y-%m-%d-%H.%M.%s')
				test_excell(judul_blank,hasil)
			else:
				test_excell(judul_opsi,hasil)
		
		elif int(opsi) == 2:
			judul_opsi = input("beri judul : " )
			if judul_opsi == None:
				judul_blank = dt.today.strftime('%Y-%m-%d-%H.%M.%s')
				test_json(judul_blank,hasil)
			else:
				test_json(judul_opsi,hasil)
		
		elif int(opsi) == 3:
			judul_opsi = input("beri judul : " )
			if judul_opsi == None:
				judul_blank = dt.today.strftime('%Y-%m-%d-%H.%M.%s')
				test_csv(judul_blank,hasil)
			else:
				test_csv(judul_opsi,hasil)
		
		elif int(opsi) == 4:
			judul_opsi = input("beri judul : " )
			if judul_opsi == None:
				judul_blank = dt.today.strftime('%Y-%m-%d-%H.%M.%s')
				test_txt(judul_blank,hasil)
			else:
				test_txt(judul_opsi,hasil)
		else:
			print("\n"+"pilihan anda tidak ada dalm daftar \n\n ulangi lagi?")
			answer = input("jawab Y atau N: ")
			if answer.lower() == 'y':
				return test_output()
			else:
				pass
	
	test_output()
	
	print("\n"+"ulangi proses ?")
	answer = input("\n"+"jawab Y atau N: ")
	if answer.lower() == 'y':
		return main()
	else:
		pass

if __name__=='__main__':
	main()
