import time
current_hour = int(time.strftime('%H'))

print("Current hour is: ", current_hour)
if 5 <= current_hour < 12:
    print("Good Morning!")
elif 12 <= current_hour < 17:
    print("Good Afternoon!")
else:
    print("Good Evening!")