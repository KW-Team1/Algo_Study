import sys
num=[]
for i in range(10):
    data=int(sys.stdin.readline())
    num.append(data%42)
num=set(num)
print(len(num))