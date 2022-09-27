hour, min = map(int, input().split())
if min >= 45:
    print("%d %d"%(hour, min-45))
else:
    if hour != 0:
        print("%d %d" %(hour-1, min+15))
    else:
        print("23 %d"%(min+15))