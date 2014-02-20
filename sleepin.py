#sleepin.py 

def sleep_in(weekday, vacay):
	if (weekday == True) and (vacay == False):
		print "You have to get up!"
		return False
	else:
		print "Sleep away"
		return True

sleep_in(False, True)
sleep_in(False, False)
sleep_in(True, True)
sleep_in(True, False)  