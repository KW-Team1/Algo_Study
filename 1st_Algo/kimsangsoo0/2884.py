clock=input('')
hour=int(clock.split(' ')[0])
minute=int(clock.split(' ')[1])
if(minute<45):
    hour=hour-1
    minute=minute+15
    if(hour<0):
        hour=23

else:
    minute=minute-45

print(f'{hour} {minute}')
