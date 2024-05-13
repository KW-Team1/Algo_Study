import sys
while True:
    try:
        data=list(map(int,sys.readline().split()))
        print(data[0]+data[1])
    except:
        break