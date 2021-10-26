import datetime

n = datetime.datetime.now()
p=n.strftime("Date = %d-%m-%Y, Time = %H:%M:%S")

print(p)