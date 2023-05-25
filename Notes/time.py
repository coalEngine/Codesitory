from datetime import *
today = datetime.today()
print("Today is:", today)

for attri in today:
    ['year','month','day','hour','minute','second','microsecond']
    print(attri, ':\t', getattr(today, attri))
