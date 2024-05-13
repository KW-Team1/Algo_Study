import sys
num=int(input())
data=list(map(int,sys.stdin.readline().split()))
num1=max(data)
for i in range(num):
    data[i]=data[i]/num1*100
print(sum(data)/num)