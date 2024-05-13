n = int(input())
orig = list(map(int, input().split()))
m = max(orig)
dest = [o/m*100 for o in orig]
print(sum(dest) / len(dest))
