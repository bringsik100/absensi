from random import randint as ri
import datetime as dt


a=dt.date(2020,1,1)
b=dt.datetime(2020,1,1,8,0,0)
c=dt.datetime(2020,1,1,16,0,0)

def o_time(hi,ci,ho,co):
	if ci < hi and co > ho:
		return (hi-ci)+(co-ho)
	elif ci < hi and co < ho:
		return hi-ci
	elif ci > hi and co > ho:
		return co-ho
	else:
		return dt.timedelta(0,0,0)

for i in range(1,100):
	d=dt.datetime(2020,1,1,ri(7,9),ri(0,59),ri(0,59))
	e=dt.datetime(2020,1,1,ri(15,18),ri(0,59),ri(0,59))
	f=a+o_time(b,d,c,e)
	print("{0} overtime = {1}".format(str(i),f.strftime('%H:%M')))