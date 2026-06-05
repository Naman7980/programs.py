import time
# currenttime = time.strftime("%H:%M:%S")
currenttime = int(time.strftime("%H"))

if 4 <= currenttime < 12:
    print("good morning sir")

elif 12 <= currenttime < 17:
    print("good afternoon sir")

elif 17 <= currenttime < 20:
    print("good evening sir")    

else:
    print("good night sir")   