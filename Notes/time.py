from datetime import *
today = datetime.today()
print("Today is:", today)

for attri in \
['year','month','day','hour','minute','second','microsecond']:
    print(attri, ':\t', getattr(today, attri))

print('Time: ', today.hour, ':', today.minute, sep="")
day = today.strftime('%A')
month = today.strftime('%B')

print("Date:", day, month, today.day)
