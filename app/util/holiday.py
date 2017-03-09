from datetime import datetime

def easter_sunday(year):
	y = year
	a = y % 19
	b = y / 100
	c = y % 100
	d = b / 4
	e = b % 4
	g = (8 * b + 13) / 25
	h = (19 * a + b - d - g + 15) % 30
	j = c / 4
	k = c % 4
	m = (a + 11 * h) / 319
	r = (2 * e + 2 * j - k - h + m + 32) % 7
	n = (h - m + r + 90) / 25 # mes
	p = (h - m + r + n + 19) % 32 # dia

	dt = datetime(year, n, p)
	return dt

def dt_converter(dt):
	if isinstance(dt, datetime):
		return dt.strftime('%d/%m/%Y')