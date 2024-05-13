import sys
num=[]
for i in range(1,31):
    num.append(i)
for j in range(28):
    data=int(sys.stdin.readline())
    num.remove(data)
print(min(num))
print(max(num))