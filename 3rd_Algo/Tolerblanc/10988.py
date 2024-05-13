import sys
input = sys.stdin.readline

string = input().strip()
print(1 if string == string[::-1] else 0)
