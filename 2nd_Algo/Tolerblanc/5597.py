submission = [False] * 30
for _ in range(28):
    submission[int(input()) - 1] = True
print(*[i + 1 for i in range(30) if not submission[i]], sep='\n')
