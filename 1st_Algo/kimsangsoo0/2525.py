clock1=input("")
time=int(input(''))
n_hour=int(clock1.split(' ')[0])
n_minute=int(clock1.split(' ')[1])


if(n_minute+time%60>=60):
    n_minute=(n_minute+time%60)%60
    n_hour=n_hour+time//60+1
    if(n_hour>=24):
        n_hour=n_hour-24
else:
    n_minute=n_minute+time%60
    n_hour=n_hour+time//60
    if(n_hour>=24):
        n_hour=n_hour-24

print(f'{n_hour} {n_minute}')
