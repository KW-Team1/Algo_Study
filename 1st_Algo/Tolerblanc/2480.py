from collections import Counter
import sys
input = sys.stdin.readline

dice = sorted(Counter(map(int, input().split())).most_common(),
              key=lambda x: (-x[1], -x[0]))
if len(dice) == 1:
    print(10000 + dice[0][0] * 1000)
elif len(dice) == 2:
    print(1000 + dice[0][0] * 100)
else:
    print(dice[0][0] * 100)
