time = input()
duration = int(input())

time = time.split(' ')
hour = int(time[0])
minute = int(time[1])

minute = (hour * 60) + minute
end_time = minute + duration
end_hour = end_time / 60
end_minute = end_time % 60

if end_hour >= 24:
    end_hour = end_hour - 24
    
print(int(end_hour), end_minute)