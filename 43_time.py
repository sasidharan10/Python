import time

print("Prints no of seconds from  1970 :",time.time())
time.sleep(1)  # delays 1 second
print("Local time :",time.ctime())
time.sleep(1)  # delays 1 second
print("Local time :",time.asctime())