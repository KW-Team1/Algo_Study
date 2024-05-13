import sys
num=int(input())
for i in range(num):
    data=list(map(int, sys.stdin.readline().split()))
    print(data[0]+data[1])