#Checks if main program has been run in last 23hours
#is to run on boot

#imports
from datetime import *
import time
import instagram

#get from file last time program was run
with open('time_check.txt', 'r') as the_file:
    last_time = datetime.strptime(the_file.readline(), '%Y-%m-%d %H:%M:%S.%f')

#get time difference between now and last time program was run
current_time = datetime.now()
tdelta = current_time - last_time

#if longer than 23hours: run main program
if tdelta > timedelta(seconds = 82800):
    print("run")
    instagram.main()
    
#else wait until 23hours have passed since last run, then run program
else:
    print("wait")
    time.sleep(82800 - tdelta.seconds)
    print("run")
    instagram.main()
