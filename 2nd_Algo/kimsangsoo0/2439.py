num=int(input())
star=[]
star1='*'
for i in range(num):
    star1='*'*(i+1)
    star.append(star1.rjust(num))
    print(star[i])