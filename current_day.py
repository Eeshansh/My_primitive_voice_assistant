from Speak import Speak1
import datetime

def tellDay():
	day = datetime.datetime.today().weekday() + 1
	
	Day_dict = {1: 'Monday', 2: 'Tuesday', 3: 'Wednesday',
				4: 'Thursday', 5: 'Friday', 6: 'Saturday',
				7: 'Sunday'}
	
	if day in Day_dict.keys():
		day_of_the_week = Day_dict[day]
		Speak1("Today is " + day_of_the_week)
