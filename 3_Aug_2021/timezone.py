import pytz
from datetime import datetime
standard_time=pytz.utc
time_zone=pytz.timezone("Asia/Kolkata")
time_zone1=pytz.timezone("Africa/Asmera")
time_zone2=pytz.timezone("Africa/Cairo")

print(datetime.now(standard_time))
print(datetime.now(time_zone))
print(datetime.now(time_zone1))
print(datetime.now(time_zone).strftime("%Y : %m : %d - %H :%M :%S"))
print(datetime.now(time_zone1).strftime("%Y : %m : %d - %H :%M :%S"))
print(datetime.now(time_zone2).strftime("%Y : %m : %d - %H :%M :%S"))
