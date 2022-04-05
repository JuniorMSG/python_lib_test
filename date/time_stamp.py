from datetime import datetime
import pandas as pd
now = datetime.now() # current date and time

timestamp = 1528797322
date_time = datetime.fromtimestamp(timestamp)


1649137387.8027775
timestamp = 1602, 9209, 2133, 6509
timestamp = 28954450421609

from time import localtime, strftime

def Unix_Epoch_Converter():
    #1970-01-01 seconds
	t=int(input('>> Please input Unix or Epoch timestamp: '))
	t_len=len(str(t))
	if t_len == 10: local=localtime(t)
	elif t_len == 13: local=localtime((t/1000))
	elif t_len == 16: local=localtime((t/1000000))
	time_format='%Y-%m-%d %H:%M:%S'
	result= strftime(time_format, local)
	print("   "+ t + "  =>  " + result)

"""

time.time()

time_temp = int("1567341580254759"[0:10])
time_format='%Y-%m-%d %H:%M:%S'
datetime.fromtimestamp(1649128269).isoformat()
datetime.now().isoformat()






int("203688239294566"[0:10]) - 1535286448


2036882392 - time_stamp
1535286448 - 2018-08-26T12:27:28.000Z

= 501595944

50159594494556

현재시간 1649139583

2094700192 -  time_stamp 
1649037065 - 
445663127

11375061699990

temp = (209470019278598 - 44566312778598) / 1000000

temp = (209470019278598 - 44600000000000) / 100000
datetime.fromtimestamp(temp).isoformat()
486 8328 9703 9556
5 7817 7998 4032
"""


date_time = datetime.fromtimestamp(timestamp)
print(date_time)

print("year:", year)

month = now.strftime("%m")
print("month:", month)

day = now.strftime("%d")
print("day:", day)

time = now.strftime("%H:%M:%S")
print("time:", time)

date_time = now.strftime("%m/%d/%Y, %H:%M:%S")
print("date and time:", date_time)