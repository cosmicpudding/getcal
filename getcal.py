import os
import sys
from astropy.io import ascii
import datetime
from visfunc import *

def get_cal():

	# Get LST
	lon = 6.60334
	utc_now = str(datetime.datetime.utcnow())
	currdate = utc_now.split()[0]
	currtime = utc_now.split()[1]
	utdec = str2dec(currtime)
	jd = juliandate(currdate,currtime)
	gst = ut2gst(jd,utdec)
	lst = gst2lst(gst,lon)
	print ('LST:',dec2str(lst))

	# Return calibrator based on LST
	if lst < 3:
		bestcal = '3C48'
		ra,dec = '01:37:41.2994','33:09:35.134'
	elif lst < 10:
		bestcal = '3C147' 
		ra,dec = '05:42:36.1379','49:51:07.234'
	elif lst < 19.5:
		bestcal = '3C286'
		ra,dec = '13:31:08.2879','30:30:32.958'
	else:
		bestcal = '3C48'
		ra,dec = '01:37:41.2994','33:09:35.134'

	return (bestcal,ra,dec)

chosen = get_cal()
print(chosen)


