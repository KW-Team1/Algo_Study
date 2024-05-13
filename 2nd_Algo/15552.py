import sys

num = int(sys.stdin.readline().rstrip())

a = []
b = []
for _ in range(num):
    line = list(map(int, sys.stdin.readline().split()))
    a.append(line[0])
    b.append(line[1])

for i in range(num):
    print(a[i] + b[i])