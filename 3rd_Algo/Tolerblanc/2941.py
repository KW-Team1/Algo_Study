import sys
input = sys.stdin.readline
print(len(input().rstrip().replace('c=', '*').replace('c-', '*').replace('dz=', '*').replace('d-',
      '*').replace('lj', '*').replace('nj', '*').replace('s=', '*').replace('z=', '*')))
