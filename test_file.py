import time


now_time = int(time.time())
timeArray = time.localtime(now_time)
date = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
print(type(date))

name = date[:13] + ':00_热搜.csv'

print(name)
