from datetime import datetime
import pytz


print('read', datetime.today().strftime("%Y%m%d%H%M%S"))    # YYYYmmddHHMMSS 형태의 시간 출력
print('read', datetime.today().strftime("%Y%m%d"))    # YYYYmmddHHMMSS 형태의 시간 출력
print('read', datetime.today().strftime("%Y/%m/%d %H:%M:%S"))  # YYYY/mm/dd HH:MM:SS 형태의 시간 출력

now = datetime.now()
print(now)

current_time = now.strftime("%H:%M:%S")
print(current_time)

current_time = datetime.now().time()
print(current_time)

current_time = datetime.now()
print(current_time)
print(f'Year : {current_time.year}')
print(f'Month : {current_time.month}')
print(f'Day : {current_time.day}')
print(f'Hour : {current_time.hour}')
print(f'Minute : {current_time.minute}')
print(f'Second : {current_time.second}')

from datetime import datetime
tz = pytz.timezone('America/New_York')
cur_time = datetime.now(tz)
simple_cur_time = cur_time.strftime("%H:%M:%S")






print(f'NY time: {cur_time}')
print(f'NY time: {simple_cur_time}')