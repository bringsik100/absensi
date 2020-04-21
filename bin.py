def late_in(hi,ci):
	if ci > hi:
		return ci-hi
	else:
		return datetime.timedelta(0,0,0)
def early_out(ho,co):
	if ho > co:
		return ho-co
	else:
		return datetime.timedelta(0,0,0)
def o_time(hi,ci,ho,co):
	if ci < hi and co > ho:
		return (hi-ci)+(co-ho)
	elif ci < hi and co < ho:
		return hi-ci
	elif ci > hi and co > ho:
		return co-ho
	else:
		return datetime.timedelta(0,0,0)
def w_time(hi,ci,ho,co):
	if ci>hi:
		return ho-ci
	elif co>ho:
		return co-hi
	else:
		return ho-hi
def t_time(a,ci,co):
	return a+(co-ci)
def nw_ot(hi,ci,ho,co):
	return round((co-ci)/(ho-hi),2)