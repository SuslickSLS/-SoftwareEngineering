import datetime
import time

sec = 1
timeStart = datetime.datetime.now().time().second

while sec <= 5:
    time.sleep(1)
    print(datetime.datetime.now().time())
    sec += 1
