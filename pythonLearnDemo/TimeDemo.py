import time
import datetime
import pytz

print(time.time()) # s秒
print(time.localtime(11134422244))
print(time.gmtime())
print(time.strftime("%Y-%m-%d:%H"))
print(time.strptime("2020-02-14","%Y-%m-%d"))

print(datetime.time)
print(datetime.MAXYEAR)
t1=datetime.date(1998,10,10)
print(t1)

print(t1.replace(year=2010,month=10,day=10))

# pytz 时区
print(pytz.timezone('Africa/Accra'))
print(pytz.all_timezones)