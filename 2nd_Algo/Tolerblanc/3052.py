import sys

input = sys.stdin.readline

s = []
for _ in range(10):
    num = int(input())
    s.append(num % 42)
print(len(set(s)))
