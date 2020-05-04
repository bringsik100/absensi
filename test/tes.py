import json
from datetime import datetime as dt
from datetime import timedelta as td
def getdata(source):
	with open(source) as sorc:
		return json.load(sorc)

pegawai = getdata('data/pegawai.json')
jadwal = getdata('data/jadwal.json')
libur = list(map(lambda x:dt.strptime(x,'%Y-%m-%d'),list(getdata('data/libur.json').keys())))
judul = getdata('data/judul.json')

awal = dt(2020,1,1)
akhir = dt(2020,1,31)
delta = akhir - awal
tanggal = [awal+td(days=x) for x in range(delta.days+1)]

