time = input()
time = time.split(' ')

hour = int(time[0])
minute = int(time[1])

if minute < 45:
    if hour == 0:
        hour = 24
    hour -= 1
    temp = minute - 45
    minute = 60 + temp
else:
    minute -= 45

print(hour, minute)