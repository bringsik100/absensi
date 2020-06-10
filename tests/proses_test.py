#!/usr/bin/env python3
"""
Proses
"""

import json
from datetime import datetime as dt
from datetime import timedelta as td
from random import randint as ri
import json
import pytest

def test_get_data(source):
	"""fungsi ambil data pegawai, jadwal, judul, liburan"""
	with open(source,'r') as srce:
		return json.load(srce)

def test_get_input(arg):
	"""fungsi untuk merubah input yang berformat string dari user menjadi datetime"""
	x = input(arg )
	return dt.strptime(x,'%Y-%m-%d')

def test_get_hour(arg):
	"""fungsi untuk merubah input yang berformat string dari jadwal menjadi datetime"""
	x = dt.strptime(arg,'%H:%M')
	return td(hours = x.hour, minutes = x.minute)

def test_get_string(day,delta):
	"""fungsi untuk merubah input yang berformat datetime menjadi string"""
	if type(delta) == str:
		return " "
	else:
		x = day + delta
		return x.strftime('%H:%M')

def test_get_late_in(hour_in,check_in,tolerance):
	"""menghitung berapa lama pegawai terlambat"""
	if check_in > hour_in:
		if (check_in - hour_in) < tolerance:
			return ' '
		else:
			return check_in - hour_in
	else:
		return ' '

def test_get_early_out(hour_out,check_out,tolerance):
	"""menghitung berapa lama pegawai pulang lebih awal"""
	if hour_out > check_out:
		if (hour_out - check_out) < tolerance:
			return ' '
		else:
			return hour_out - check_out
	else:
		return ' '

def test_get_overtime(hour_out,check_out):
	"""menghitung lembur pegawai"""
	if check_out > hour_out:
		return check_out - hour_out
	else:
		return ' '

def test_get_worktime(hour_in,hour_out,check_in,check_out):
	"""menghitung jam kerja minus telat dan pulang awal"""
	if check_in > hour_in:
		return hour_out - check_in
	elif check_out > hour_out:
		return check_out - hour_in
	else:
		return hour_out - hour_in

def test_get_totaltime(check_in,check_out):
	"""menghitung jam kerja dari jam masuk dan jam keluar"""
	return (check_out - check_in)

def test_get_overtype(hour_out,check_out):
	"""menghitung jam lembur dalam desimal"""
	if check_out > hour_out:
		return round((check_out - hour_out)/td(hours = 1),2)
	else:
		return ' '

def test_process(start,end,buffer):
	"""fungsi untuk memproses pegawai tanggal waktu dan input ke buffer"""
	"""start = tanggal mulai"""
	"""end = tanggal akhir """
	"""buffer berfungsi sebagai penampung data"""
	
	"""ambil library yang dibutuhkan"""
	employee = test_get_data('data/pegawai.json')
	schedule = test_get_data('data/jadwal.json')
	subdata = test_get_data('data/judul.json')
	holiday = list(map(lambda x:dt.strptime(x,'%Y-%m-%d'),list(test_get_data('data/libur.json').keys())))
	
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
			
			if not thisday in holiday:
				if thisday.weekday() == 6:
					"""hari minggu """
					thisday_schedule = schedule["2"]
					hour_in = test_get_hour(thisday_schedule['hour start'])
					hour_out = test_get_hour(thisday_schedule['hour end'])
					check_in = ' '
					check_out = ' '
					late_in = ' '
					early_out = ' '
					overtime = ' '
					worktime = ' '
					totaltime = ' '
					overtype = ' '
				
					data["6"] = thisday_schedule["name"] #nama jadwal
					data["7"] = thisday_schedule['hour start'] #jadwal masuk
					data["8"] = thisday_schedule['hour end'] #jadwal keluar
					data["9"] = ' ' #jam masuk
					data["10"] = ' ' #jam keluar
					data["11"] = ' ' #jam normal
				
					data["13"] = ' ' #terlambat
					data["14"] = ' ' #pulang cepat
					try:
						if isinstance(check_in,td) == False:
							data["15"] = 'True' #bolos
						elif check_in == td(seconds = 0):
							data["15"] = 'True' #bolos
						elif late_in > test_get_hour(thisday_schedule["checkin max"]):
							data["15"] = 'True' #bolos
						elif check_out < test_get_hour(thisday_schedule["checkin max"]):
							data["15"] = 'True' #bolos
						else : 
							data["15"] = ' ' #bolos
					except Exception:
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
			
				elif thisday.weekday() == 5:
					"""hari sabtu """
					thisday_schedule = schedule["2"]
					hour_in = test_get_hour(thisday_schedule['hour start'])
					hour_out = test_get_hour(thisday_schedule['hour end'])
					hour = ri(7,8)
					if hour == 8:
						minute = ri(0,15)
						second = ri(0,59)
					else:
						minute = ri(0,59)
						second = ri(0,59)
					check_in = td(hours = hour, minutes = minute, seconds = second)
					check_out = td(hours = ri(15,18), minutes = ri(0,59),seconds = ri(0,59))
					late_in = test_get_late_in(hour_in,check_in,test_get_hour(thisday_schedule['late in']))
					early_out = test_get_early_out(hour_out,check_out,test_get_hour(thisday_schedule['early out']))
					overtime = test_get_overtime(hour_out,check_out)
					worktime = test_get_worktime(hour_in,hour_out,check_in,check_out)
					totaltime = test_get_totaltime(check_in,check_out)
					overtype = test_get_overtype(hour_out,check_out)
				
					data["6"] = thisday_schedule["name"] #nama jadwal
					data["7"] = thisday_schedule['hour start'] #jadwal masuk
					data["8"] = thisday_schedule['hour end'] #jadwal keluar
					data["9"] = test_get_string(thisday,check_in) #jam masuk
					data["10"] = test_get_string(thisday,check_out) #jam keluar
					data["11"] = '1' #jam normal
					data["13"] = test_get_string(thisday,late_in) #terlambat
					data["14"] = test_get_string(thisday,early_out) #pulang cepat
					try:
						if isinstance(check_in,td) == False:
							data["15"] = 'True' #bolos
						elif check_in == td(seconds = 0):
							data["15"] = 'True' #bolos
						elif late_in > test_get_hour(thisday_schedule["checkin max"]):
							data["15"] = 'True' #bolos
						elif check_out < test_get_hour(thisday_schedule["checkin max"]):
							data["15"] = 'True' #bolos
						else : 
							data["15"] = ' ' #bolos
					except Exception:
						data["15"] = ' ' #bolos
					data["16"] = test_get_string(thisday,overtime) #lembur
					data["17"] = test_get_string(thisday,worktime) #jam kerja
					data["18"] = test_get_string(thisday,totaltime) #waktu kerja
					data["23"] = ' ' #normal days
					data["24"] = '1' #akhir pekan
					data["25"] = ' ' #hari libur
					data["26"] = ' ' # lembur hari normal
					data["27"] = str(overtype) #lembur akhir pekan
					data["28"] = ' ' #lembur hari libur
			
				else:
					"""hari senin sarmpai jumat"""
					thisday_schedule = schedule["1"]
					hour_in = test_get_hour(thisday_schedule['hour start'])
					hour_out = test_get_hour(thisday_schedule['hour end'])
					hour = ri(7,8)
					if hour == 8:
						minute = ri(0,15)
						second = ri(0,59)
					else:
						minute = ri(0,59)
						second = ri(0,59)
					check_in = td(hours = hour, minutes = minute, seconds = second)
					check_out = td(hours = ri(15,18), minutes = ri(0,59),seconds = ri(0,59))
					late_in = test_get_late_in(hour_in,check_in,test_get_hour(thisday_schedule['late in']))
					early_out = test_get_early_out(hour_out,check_out,test_get_hour(thisday_schedule['early out']))
					overtime = test_get_overtime(hour_out,check_out)
					worktime = test_get_worktime(hour_in,hour_out,check_in,check_out)
					totaltime = test_get_totaltime(check_in,check_out)
					overtype = test_get_overtype(hour_out,check_out)
			
					data["6"] = schedule["1"]["name"] #nama jadwal
					data["7"] = schedule["1"]['hour start'] #jadwal masuk
					data["8"] = schedule["1"]['hour end'] #jadwal keluar
					data["9"] = test_get_string(thisday,check_in) #jam masuk
					data["10"] = test_get_string(thisday,check_out) #jam keluar
					data["11"] = '1' #jam normal
					data["13"] = test_get_string(thisday,late_in) #terlambat
					data["14"] = test_get_string(thisday,early_out) #pulang cepat
					try:
						if isinstance(check_in,td) == False:
							data["15"] = 'True' #bolos
						elif check_in == td(seconds = 0):
							data["15"] = 'True' #bolos
						elif late_in > test_get_hour(thisday_schedule["checkin max"]):
							data["15"] = 'True' #bolos
						elif check_out < test_get_hour(thisday_schedule["checkin max"]):
							data["15"] = 'True' #bolos
						else : 
							data["15"] = ' ' #bolos
					except Exception:
						data["15"] = ' ' #bolos
					data["16"] = test_get_string(thisday,overtime) #lembur
					data["17"] = test_get_string(thisday,worktime) #jam kerja
					data["18"] = test_get_string(thisday,totaltime) #waktu kerja
					data["23"] = '1' #normal days
					data["24"] = ' ' #akhir pekan
					data["25"] = ' ' #hari libur
					data["26"] = str(overtype) # lembur hari normal
					data["27"] = ' ' #lembur akhir pekan
					data["28"] = ' ' #lembur hari libur
			else:
				"""hari libur"""
				thisday_schedule = schedule["0"]
				hour_in = test_get_hour(thisday_schedule['hour start'])
				hour_out = test_get_hour(thisday_schedule['hour end'])
				check_in = ' '
				check_out = ' '
				late_in = ' '
				early_out = ' '
				overtime = ' '
				worktime = ' '
				totaltime = ' '
				overtype = ' '
				
				data["6"] = thisday_schedule["name"] #nama jadwal
				data["7"] = thisday_schedule['hour start'] #jadwal masuk
				data["8"] = thisday_schedule['hour end'] #jadwal keluar
				data["9"] = test_get_string(thisday,check_in) #jam masuk
				data["10"] = test_get_string(thisday,check_out) #jam keluar
				data["11"] = ' ' #jam normal
				
				data["13"] = test_get_string(thisday,late_in) #terlambat
				data["14"] = test_get_string(thisday,early_out) #pulang cepat
				if isinstance(check_in,td) == False:
					data["15"] = 'True' #bolos
				elif check_in == td(seconds = 0):
					data["15"] = 'True' #bolos
				elif late_in > test_get_hour(thisday_schedule["checkin max"]):
					data["15"] = 'True' #bolos
				elif check_out < test_get_hour(thisday_schedule["checkin max"]):
					data["15"] = 'True' #bolos
				else : 
					data["15"] = ' ' #bolos
				data["16"] = test_get_string(thisday,overtime) #lembur
				data["17"] = test_get_string(thisday,worktime) #jam kerja
				data["18"] = test_get_string(thisday,totaltime) #waktu kerja
				data["23"] = ' ' #normal days
				data["24"] = ' ' #akhir pekan
				data["25"] = '1' #hari libur
				data["26"] = ' ' # lembur hari normal
				data["27"] = ' ' #lembur akhir pekan
				data["28"] = str(overtype) #lembur hari libur
			"""mengisi data ke buffer"""
			buffer.append(data)

def test_main():
	print("not ready yet")

if __name__ == '__main__':
	test_main()
