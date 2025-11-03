import time
current_time = time.time()
print("Current time: ",current_time)

import time
current_time = time.ctime()
print("Current time: ",current_time)

import time
print("wait for 4 seconds.....")
current_time = time.sleep(4)
print("hello!")

import time
c_time = time.localtime()
print("Full date and time:",time.strftime("%Y-%M-%d %H:%M:%S",c_time))
print("Only date:",time.strftime("%d/%m/%Y",c_time))
print("Only time:",time.strftime("%I:%M:%p",c_time))
print("day name:",time.strftime("%A",c_time))