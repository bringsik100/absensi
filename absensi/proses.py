#!/usr/bin/env python3
"""
modul memproses input dari data

untuk sementara input data masih campur antara text dan database
"""

import json
from datetime import datetime as dt
from datetime import timedelta as td
from random import randint as ri


def get_data(source):
    """fungsi ambil data pegawai, jadwal, judul, liburan"""
    with open(source, 'r') as srce:
        return json.load(srce)

def get_input(arg):
    """fungsi untuk merubah input yang berformat string dari user menjadi datetime"""
    x_input = input(arg)
    return dt.strptime(x_input, '%Y-%m-%d')

def get_hour(arg):
    """fungsi untuk merubah input yang berformat string dari jadwal menjadi datetime"""
    x_time = dt.strptime(arg, '%H:%M')
    return td(hours=x_time.hour, minutes=x_time.minute)

def get_string(day, delta):
    """fungsi untuk merubah input yang berformat datetime menjadi string"""
    if isinstance(delta, str):
        result = " "
    else:
        x_day = day + delta
        result = x_day.strftime('%H:%M')
    return result

def get_late_in(hour_in, check_in, tolerance):
    """menghitung berapa lama pegawai terlambat"""
    if check_in > hour_in:
        if (check_in - hour_in) < tolerance:
            result = ' '
        else:
            result = check_in - hour_in
    else:
        result = ' '

    return result

def get_early_out(hour_out, check_out, tolerance):
    """menghitung berapa lama pegawai pulang lebih awal"""
    if hour_out > check_out:
        if (hour_out - check_out) < tolerance:
            result = ' '
        else:
            result = hour_out - check_out
    else:
        result = ' '
    return result

def get_overtime(hour_out, check_out):
    """menghitung lembur pegawai"""
    if check_out > hour_out:
        result = check_out - hour_out
    else:
        result = ' '

    return result

def get_worktime(hour_in, hour_out, check_in, check_out):
    """menghitung jam kerja minus telat dan pulang awal"""
    if check_in > hour_in:
        result = hour_out - check_in
    elif check_out > hour_out:
        result = check_out - hour_in
    else:
        result = hour_out - hour_in
    return result

def get_totaltime(check_in, check_out):
    """menghitung jam kerja dari jam masuk dan jam keluar"""
    return check_out - check_in

def get_overtype(hour_out, check_out):
    """menghitung jam lembur dalam desimal"""
    if check_out > hour_out:
        result = round((check_out - hour_out)/td(hours=1), 2)
    else:
        result = ' '

    return result

#ambil data dari sumber data
    employee = get_data('data/pegawai.json')
    schedule = get_data('data/jadwal.json')
    #subdata = get_data('data/judul.json')
    holiday = [dt.strptime(x, '%Y-%m-%d') for x in list(get_data('data/libur.json').keys())]

def process(start, end, buffer):
    """fungsi untuk memproses pegawai tanggal waktu dan input ke buffer"""
    #start = tanggal mulai
    #end = tanggal akhir
    #buffer berfungsi sebagai penampung data

    #daftar tanggal
    delta = end - start

    #looping pegawai
    for y in employee:
        #looping tanggal
        for day in range(delta.days+1):
            #fungsi untuk mengisi waktu
            data = {}
            thisday = start + td(days=day)

            data["0"] = employee[y]['nopeg'] #nomor pegawai
            data["1"] = employee[y]['akun'] #nomor akun
            data["2"] = employee[y]['nomor'] #nomor induk
            data["3"] = employee[y]['nama'] #nama pegawai
            data["4"] = ' ' #masuk otomatis (biarkan kosong)
            data["5"] = thisday.strftime('%Y-%m-%d') #tanggal
            data["12"] = '1' #waktu real
            data["19"] = ' ' #status
            data["20"] = ' ' #harus check in
            data["21"] = ' ' #harus check out
            data["22"] = employee[y]['dpt'] #departemen

            if not thisday in holiday:
                if thisday.weekday() == 6:
                    #hari minggu
                    thisday_schedule = schedule["2"]
                    hour_in = get_hour(thisday_schedule['hour start'])
                    hour_out = get_hour(thisday_schedule['hour end'])
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
                        if not isinstance(check_in, td):
                            data["15"] = 'True' #bolos
                        elif check_in == td(seconds=0):
                            data["15"] = 'True' #bolos
                        elif late_in > get_hour(thisday_schedule["checkin max"]):
                            data["15"] = 'True' #bolos
                        elif check_out < get_hour(thisday_schedule["checkin max"]):
                            data["15"] = 'True' #bolos
                        else:
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
                    #hari sabtu
                    thisday_schedule = schedule["2"]
                    hour_in = get_hour(thisday_schedule['hour start'])
                    hour_out = get_hour(thisday_schedule['hour end'])
                    hour = ri(7, 8)
                    if hour == 8:
                        minute = ri(0, 15)
                        second = ri(0, 59)
                    else:
                        minute = ri(0, 59)
                        second = ri(0, 59)
                    check_in = td(hours=hour, minutes=minute, seconds=second)
                    check_out = td(hours=ri(15, 18), minutes=ri(0, 59), seconds=ri(0, 59))
                    late_in = get_late_in(hour_in, check_in, get_hour(thisday_schedule['late in']))
                    early_out = get_early_out(hour_out, check_out, get_hour(thisday_schedule['early out']))
                    overtime = get_overtime(hour_out, check_out)
                    worktime = get_worktime(hour_in, hour_out, check_in, check_out)
                    totaltime = get_totaltime(check_in, check_out)
                    overtype = get_overtype(hour_out, check_out)

                    data["6"] = thisday_schedule["name"] #nama jadwal
                    data["7"] = thisday_schedule['hour start'] #jadwal masuk
                    data["8"] = thisday_schedule['hour end'] #jadwal keluar
                    data["9"] = get_string(thisday, check_in) #jam masuk
                    data["10"] = get_string(thisday, check_out) #jam keluar
                    data["11"] = '1' #jam normal
                    data["13"] = get_string(thisday, late_in) #terlambat
                    data["14"] = get_string(thisday, early_out) #pulang cepat
                    try:
                        if not isinstance(check_in, td):
                            data["15"] = 'True' #bolos
                        elif check_in == td(seconds=0):
                            data["15"] = 'True' #bolos
                        elif late_in > get_hour(thisday_schedule["checkin max"]):
                            data["15"] = 'True' #bolos
                        elif check_out < get_hour(thisday_schedule["checkin max"]):
                            data["15"] = 'True' #bolos
                        else:
                            data["15"] = ' ' #bolos
                    except Exception:
                        data["15"] = ' ' #bolos
                    data["16"] = get_string(thisday, overtime) #lembur
                    data["17"] = get_string(thisday, worktime) #jam kerja
                    data["18"] = get_string(thisday, totaltime) #waktu kerja
                    data["23"] = ' ' #normal days
                    data["24"] = '1' #akhir pekan
                    data["25"] = ' ' #hari libur
                    data["26"] = ' ' # lembur hari normal
                    data["27"] = str(overtype) #lembur akhir pekan
                    data["28"] = ' ' #lembur hari libur

                else:
                    #hari senin sarmpai jumat
                    thisday_schedule = schedule["1"]
                    hour_in = get_hour(thisday_schedule['hour start'])
                    hour_out = get_hour(thisday_schedule['hour end'])
                    hour = ri(7, 8)
                    if hour == 8:
                        minute = ri(0, 15)
                        second = ri(0, 59)
                    else:
                        minute = ri(0, 59)
                        second = ri(0, 59)
                    check_in = td(hours=hour, minutes=minute, seconds=second)
                    check_out = td(hours=ri(15, 18), minutes=ri(0, 59), seconds=ri(0, 59))
                    late_in = get_late_in(hour_in, check_in, get_hour(thisday_schedule['late in']))
                    early_out = get_early_out(hour_out, check_out, get_hour(thisday_schedule['early out']))
                    overtime = get_overtime(hour_out, check_out)
                    worktime = get_worktime(hour_in, hour_out, check_in, check_out)
                    totaltime = get_totaltime(check_in, check_out)
                    overtype = get_overtype(hour_out, check_out)

                    data["6"] = schedule["1"]["name"] #nama jadwal
                    data["7"] = schedule["1"]['hour start'] #jadwal masuk
                    data["8"] = schedule["1"]['hour end'] #jadwal keluar
                    data["9"] = get_string(thisday, check_in) #jam masuk
                    data["10"] = get_string(thisday, check_out) #jam keluar
                    data["11"] = '1' #jam normal
                    data["13"] = get_string(thisday, late_in) #terlambat
                    data["14"] = get_string(thisday, early_out) #pulang cepat
                    try:
                        if not isinstance(check_in, td):
                            data["15"] = 'True' #bolos
                        elif check_in == td(seconds=0):
                            data["15"] = 'True' #bolos
                        elif late_in > get_hour(thisday_schedule["checkin max"]):
                            data["15"] = 'True' #bolos
                        elif check_out < get_hour(thisday_schedule["checkin max"]):
                            data["15"] = 'True' #bolos
                        else:
                            data["15"] = ' ' #bolos
                    except Exception:
                        data["15"] = ' ' #bolos
                    data["16"] = get_string(thisday, overtime) #lembur
                    data["17"] = get_string(thisday, worktime) #jam kerja
                    data["18"] = get_string(thisday, totaltime) #waktu kerja
                    data["23"] = '1' #normal days
                    data["24"] = ' ' #akhir pekan
                    data["25"] = ' ' #hari libur
                    data["26"] = str(overtype) # lembur hari normal
                    data["27"] = ' ' #lembur akhir pekan
                    data["28"] = ' ' #lembur hari libur
            else:
                #hari libur
                thisday_schedule = schedule["0"]
                hour_in = get_hour(thisday_schedule['hour start'])
                hour_out = get_hour(thisday_schedule['hour end'])
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
                data["9"] = get_string(thisday, check_in) #jam masuk
                data["10"] = get_string(thisday, check_out) #jam keluar
                data["11"] = ' ' #jam normal

                data["13"] = get_string(thisday, late_in) #terlambat
                data["14"] = get_string(thisday, early_out) #pulang cepat
                if not isinstance(check_in, td):
                    data["15"] = 'True' #bolos
                elif check_in == td(seconds=0):
                    data["15"] = 'True' #bolos
                elif late_in > get_hour(thisday_schedule["checkin max"]):
                    data["15"] = 'True' #bolos
                elif check_out < get_hour(thisday_schedule["checkin max"]):
                    data["15"] = 'True' #bolos
                else:
                    data["15"] = ' ' #bolos
                data["16"] = get_string(thisday, overtime) #lembur
                data["17"] = get_string(thisday, worktime) #jam kerja
                data["18"] = get_string(thisday, totaltime) #waktu kerja
                data["23"] = ' ' #normal days
                data["24"] = ' ' #akhir pekan
                data["25"] = '1' #hari libur
                data["26"] = ' ' # lembur hari normal
                data["27"] = ' ' #lembur akhir pekan
                data["28"] = str(overtype) #lembur hari libur
            #mengisi data ke buffer
            buffer.append(data)

def main():
    """main modul"""
    print("not ready yet")

if __name__ == '__main__':
    main()
