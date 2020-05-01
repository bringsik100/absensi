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

def get_data(source):
	"""fungsi ambil data pegawai, jadwal, judul, liburan"""
	with open(source,'r') as srce:
		return json.load(srce)


def get_input(arg):
	"""fungsi untuk merubah input yang berformat string dari user menjadi datetime"""
	x = input(arg )
	return dt.strptime(x,'%Y-%m-%d')

def get_hour(arg):
	"""fungsi untuk merubah input yang berformat string dari jadwal menjadi datetime"""
	x = dt.strptime(arg,'%H:%M')
	return td(hours = x.hour, minutes = x.minute)

def get_string(day,delta):
	"""fungsi untuk merubah input yang berformat datetime menjadi string"""
	if type(delta) == str:
		return " "
	else:
		x = day + delta
		return x.strftime('%H:%M')


def get_late_in(hour_in,check_in,tolerance):
	"""menghitung berapa lama pegawai terlambat"""
	if check_in > hour_in:
		if (check_in - hour_in) < tolerance:
			return td(seconds=0)
		else:
			return check_in - hour_in
	else:
		return ' '

def get_early_out(hour_out,check_out,tolerance):
	"""menghitung berapa lama pegawai pulang lebih awal"""
	if hour_out > check_out:
		if (hour_out - check_out) < tolerance:
			return ' '
		else:
			return hour_out - check_out
	else:
		return ' '

def get_overtime(hour_out,check_out):
	"""menghitung lembur pegawai"""
	if check_out > hour_out:
		return check_out - hour_out
	else:
		return ' '

def get_worktime(hour_in,hour_out,check_in,check_out):
	"""menghitung jam kerja minus telat dan pulang awal"""
	if check_in > hour_in:
		return hour_out - check_in
	elif check_out > hour_out:
		return check_out - hour_in
	else:
		return hour_out - hour_in

def get_totaltime(check_in,check_out):
	"""menghitung jam kerja dari jam masuk dan jam keluar"""
	return (check_out - check_in)

def get_overtype(hour_in,hour_out,check_in,check_out):
	"""menghitung jam lembur dalam desimal"""
	if check_out > hour_out:
		return round((check_out - hour_out)/td(hours = 1),2)
	else:
		return ' '

def process(start,end,buffer):
	"""fungsi untuk memproses pegawai tanggal waktu dan input ke buffer"""
	"""start = tanggal mulai"""
	"""end = tanggal akhir """
	"""buffer berfungsi sebagai penampung data"""
	
	"""ambil library yang dibutuhkan"""
	employee = get_data('data/pegawai.json')
	schedule = get_data('data/jadwal.json')
	subdata = get_data('data/judul.json')
	holiday = list(get_data('data/libur.json'))
	
	"""daftar tanggal"""
	delta = end - start
	
	"""looping pegawai"""
	for x in range(len(employee)):
		x = x + 1 #variabel untuk data pegawai
		"""looping tanggal"""
		for day in range(delta.days+1):
			"""fungsi untuk mengisi waktu"""
			data = {}
			thisday = start + td(days = day)
			
			data["0"] = employee[str(x)]['nopeg'] #nomor pegawai
			data["1"] = employee[str(x)]['akun'] #nomor akun
			data["2"] = employee[str(x)]['nomor'] #nomor induk
			data["3"] = employee[str(x)]['nama'] #nama pegawai
			data["4"] = ' ' #masuk otomatis (biarkan kosong)
			data["5"] = thisday.strftime('%Y-%m-%d') #tanggal
			data["12"] = '1' #waktu real
			data["19"] = ' ' #status
			data["20"] = ' ' #harus check in
			data["21"] = ' ' #harus check out
			data["22"] = employee[str(x)]['dpt'] #departemen
			
			if thisday in holiday is True:
				"""hari libur"""
				thisday_schedule = schedule["0"]["name"]
				hour_in = get_hour(schedule["0"]['hour start'])
				hour_out = get_hour(schedule["0"]['hour end'])
				check_in = ' '
				check_out = ' '
				late_in = ' '
				early_out = ' '
				overtime = ' '
				worktime = ' '
				totaltime = ' '
				overtype = ' '
				
				data["6"] = schedule["0"]["name"] #nama jadwal
				data["7"] = schedule["0"]['hour start'] #jadwal masuk
				data["8"] = schedule["0"]['hour end'] #jadwal keluar
				data["9"] = get_string(thisday,check_in) #jam masuk
				data["10"] = get_string(thisday,check_out) #jam keluar
				data["11"] = ' ' #jam normal
				
				data["13"] = get_string(thisday,late_in) #terlambat
				data["14"] = get_string(thisday,early_out) #pulang cepat
				if check_in == td(seconds = 0) or late_in > get_hour(schedule["1"]["checkin max"]) or check_out < get_hour(schedule["0"]["checkin max"]):
					data["15"] = 'True' #bolos
				else : 
					data["15"] = ' ' #bolos
				data["16"] = get_string(thisday,overtime) #lembur
				data["17"] = get_string(thisday,worktime) #jam kerja
				data["18"] = get_string(thisday,totaltime) #waktu kerja
				data["23"] = ' ' #normal days
				data["24"] = ' ' #akhir pekan
				data["25"] = '1' #hari libur
				data["26"] = ' ' # lembur hari normal
				data["27"] = ' ' #lembur akhir pekan
				data["28"] = str(overtype) #lembur hari libur
			
			else:
				if thisday.weekday == 6:
					"""hari minggu """
					thisday_schedule = schedule["2"]["name"]
					hour_in = get_hour(schedule["2"]['hour start'])
					hour_out = get_hour(schedule["2"]['hour end'])
					check_in = ' '
					check_out = ' '
					late_in = ' '
					early_out = ' '
					overtime = ' '
					worktime = ' '
					totaltime = ' '
					overtype = ' '
				
					data["6"] = schedule["2"]["name"] #nama jadwal
					data["7"] = schedule["2"]['hour start'] #jadwal masuk
					data["8"] = schedule["2"]['hour end'] #jadwal keluar
					data["9"] = ' ' #jam masuk
					data["10"] = ' ' #jam keluar
					data["11"] = ' ' #jam normal
				
					data["13"] = ' ' #terlambat
					data["14"] = ' ' #pulang cepat
					if check_in == td(seconds = 0) or late_in > get_hour(schedule["1"]["checkin max"]) or check_out < get_hour(schedule["0"]["checkin max"]):
						data["15"] = 'True' #bolos
					else : 
						data["15"] = ' ' #bolos
					data["16"] = ' ' #lembur
					data["17"] = ' ' #jam kerja
					data["18"] = ' ' #waktu kerja
					data["23"] = ' ' #normal days
					data["24"] = '1' #akhir pekan
					data["25"] = ' ' #hari libur
					data["26"] = ' ' # lembur hari normal
					data["27"] = str(overtype) #lembur akhir pekan
					data["28"] = ' ' #lembur hari libur
			
				elif thisday.weekday == 5:
					"""hari sabtu """
					thisday_schedule = schedule["2"]["name"]
					hour_in = get_hour(schedule["2"]['hour start'])
					hour_out = get_hour(schedule["2"]['hour end'])
					hour = ri(7,8)
					if hour == 8:
						minute = ri(0,15)
						second = ri(0,59)
					else:
						minute = ri(0,59)
						second = ri(0,59)
					check_in = td(hours = hour, minutes = minute, seconds = second)
					check_out = td(hours = ri(15,18), minutes = ri(0,59),seconds = ri(0,59))
					late_in = get_late_in(hour_in,check_in,get_hour(schedule["2"]['late in']))
					early_out = get_early_out(hour_out,check_out,get_hour(schedule["2"]['early out']))
					overtime = get_overtime(hour_out,check_out)
					worktime = get_worktime(hour_in,hour_out,check_in,check_out)
					totaltime = get_totaltime(check_in,check_out)
					overtype = get_overtype(hour_out,check_out)
					
					data["6"] = schedule["2"]["name"] #nama jadwal
					data["7"] = schedule["2"]['hour start'] #jadwal masuk
					data["8"] = schedule["2"]['hour end'] #jadwal keluar
					data["9"] = get_string(thisday,check_in) #jam masuk
					data["10"] = get_string(thisday,check_out) #jam keluar
					data["11"] = '1' #jam normal
					data["13"] = get_string(thisday,late_in) #terlambat
					data["14"] = get_string(thisday,early_out) #pulang cepat
					if check_in == td(seconds = 0) or late_in > get_hour(schedule["2"]["checkin max"]) or check_out < get_hour(schedule["0"]["checkin max"]):
						data["15"] = 'True' #bolos
					else : 
						data["15"] = ' ' #bolos
					data["16"] = get_string(thisday,overtime) #lembur
					data["17"] = get_string(thisday,worktime) #jam kerja
					data["18"] = get_string(thisday,totaltime) #waktu kerja
					data["23"] = ' ' #normal days
					data["24"] = '1' #akhir pekan
					data["25"] = ' ' #hari libur
					data["26"] = ' ' # lembur hari normal
					data["27"] = str(overtype) #lembur akhir pekan
					data["28"] = ' ' #lembur hari libur
			
				else:
					"""hari senin sarmpai jumat"""
					thisday_schedule = schedule["1"]["name"]
					hour_in = get_hour(schedule["1"]['hour start'])
					hour_out = get_hour(schedule["1"]['hour end'])
					hour = ri(7,8)
					if hour == 8:
						minute = ri(0,15)
						second = ri(0,59)
					else:
						minute = ri(0,59)
						second = ri(0,59)
					check_in = td(hours = hour, minutes = minute, seconds = second)
					check_out = td(hours = ri(15,18), minutes = ri(0,59),seconds = ri(0,59))
					late_in = get_late_in(hour_in,check_in,get_hour(schedule["1"]['late in']))
					early_out = get_early_out(hour_out,check_out,get_hour(schedule["1"]['early out']))
					overtime = get_overtime(hour_out,check_out)
					worktime = get_worktime(hour_in,hour_out,check_in,check_out)
					totaltime = get_totaltime(check_in,check_out)
					overtype = get_overtype(hour_in,hour_out,check_in,check_out)
				
					data["6"] = schedule["1"]["name"] #nama jadwal
					data["7"] = schedule["1"]['hour start'] #jadwal masuk
					data["8"] = schedule["1"]['hour end'] #jadwal keluar
					data["9"] = get_string(thisday,check_in) #jam masuk
					data["10"] = get_string(thisday,check_out) #jam keluar
					data["11"] = '1' #jam normal
					data["13"] = get_string(thisday,late_in) #terlambat
					data["14"] = get_string(thisday,early_out) #pulang cepat
					try:
						if check_in == td(seconds = 0) or late_in > get_hour(schedule["2"]["checkin max"]) or check_out < get_hour(schedule["0"]["checkin max"]):
							data["15"] = 'True' #bolos
						else : 
							data["15"] = ' ' #bolos
					except TypeError:
						data["15"] = ' ' #bolos
					data["16"] = get_string(thisday,overtime) #lembur
					data["17"] = get_string(thisday,worktime) #jam kerja
					data["18"] = get_string(thisday,totaltime) #waktu kerja
					data["23"] = '1' #normal days
					data["24"] = ' ' #akhir pekan
					data["25"] = ' ' #hari libur
					data["26"] = str(overtype) # lembur hari normal
					data["27"] = ' ' #lembur akhir pekan
					data["28"] = ' ' #lembur hari libur
			
			"""mengisi data ke buffer"""
			buffer.append(data)

"""fungsi ouput dengan 5 pilihan : layar, excell, JSON, csv, text"""

def pt_screen(buffer):
	"""output ke layar"""
	print(buffer)
		

def pt_excell(file_title,buffer):
	"""output ke excell"""

	"""membaca data header dari judul.json"""
	with open('data/judul.json','r') as head_data:
		header = list(json.load(head_data).keys())

	book = Workbook()
	sheet = book.active
	sheet.title = file_title

	"""header untuk mengisi baris pertama"""
	for i in range(len(header)):
		sheet.cell(column=i+1,row=1, value=header[i])

	"""isi sheet dari buffer"""
	for rows in range(len(buffer)):
		for cols in range(len((buffer[rows]))):
			sheet.cell(column=cols+1,row=rows+2,value=buffer[rows][str(cols)])
		
	"""save ke excell"""
	book.save('{}.xlsx'.format(file_title))
	book.close()

def pt_json(file_title,buffer):
	"""output ke json"""
	with open('{}.json'.format(file_title),'w') as jsonfile:
		json.dumps(buffer)

def pt_csv(file_title,buffer):
	"""output ke csv"""
	with open(f'{file_title}.csv', 'w', newline='') as csvfile:
		x = csv.writer(csvfile, delimiter=',',quotechar='"')
		for i in buffer:
			x.writerow(i)

def pt_txt(file_title,buffer):
	"""output ke text"""
	with open('{}.txt'.format(file_title), 'w') as txtfile:
			txtfile.write(json.dumps(buffer))

"""salam pembuka"""
print("""
SELAMAT DATANG DI ABTOMATIS
MODUL PENGISI ABSENSI OTOMATIS
""")

def main():
	"""fungsi utama, semua data diproses disini"""
	
	print("""
	metode pengisian :
	masukkan tanggal awal dan akhir dengan format YYYY-MM-DD dimana 
	YYYY = 4 angka tahun
	MM = 2 angka bulan 
	DD = 2 angka tanggal
	""")
	
	"""tanya tanggal awal dan akhir otomatis"""
	awal = get_input(' masukkan tanggal awal absensi: ') 
	akhir = get_input(' masukkan tanggal akhir absensi: ')
	hasil = []
	
	"""main proses"""
	process(awal,akhir,hasil)
	

	def output():
		"""memproses data dari penampung untuk di cetak ke layar atau berkas"""
		
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
			"""cetek ke layar"""
			pt_screen(hasil)
		
		elif int(opsi) == 1:
			"""cetak ke excell"""
			judul_opsi = input("beri judul : " )
			if judul_opsi == None:
				judul_blank = dt.today.strftime('%Y-%m-%d-%H.%M.%s')
				pt_excell(judul_blank,hasil)
			else:
				pt_excell(judul_opsi,hasil)
		
		elif int(opsi) == 2:
			"""cetak ke JSON"""
			judul_opsi = input("beri judul : " )
			if judul_opsi == None:
				judul_blank = dt.today.strftime('%Y-%m-%d-%H.%M.%s')
				pt_json(judul_blank,hasil)
			else:
				pt_json(judul_opsi,hasil)
		
		elif int(opsi) == 3:
			"""cetak ke csv"""
			judul_opsi = input("beri judul : " )
			if judul_opsi == None:
				judul_blank = dt.today.strftime('%Y-%m-%d-%H.%M.%s')
				pt_csv(judul_blank,hasil)
			else:
				pt_csv(judul_opsi,hasil)
		
		elif int(opsi) == 4:
			"""cetak ke text"""
			judul_opsi = input("beri judul : " )
			if judul_opsi == None:
				judul_blank = dt.today.strftime('%Y-%m-%d-%H.%M.%s')
				pt_txt(judul_blank,hasil)
			else:
				pt_txt(judul_opsi,hasil)
		else:
			"""opsi diluar batas"""
			print("\n"+"pilihan anda tidak ada dalm daftar \n\n ulangi lagi?")
			
			answer = input("\n\njawab Y atau N: ")
			if answer.lower() == 'y':
				return output()
			else:
				pass
	
	output()
	
	print("\n\nulangi proses ?")
	answer = input("\n\njawab Y atau N: ")
	if answer.lower() == 'y':
		return main()
	else:
		pass

if __name__=='__main__':
	main()
