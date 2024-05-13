n = int(input())
for _ in range(n):
    m, s = input().split()
    for c in s:
        print(c * int(m), end='')
    print()
