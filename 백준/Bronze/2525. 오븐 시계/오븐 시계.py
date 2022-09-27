hour,min = map(int, input().split())
dur = int(input())
if (min+dur) < 60:
    print("%d %d"%(hour, min+dur))
else:
    if (min+dur)//60+hour <= 23:
        print("%d %d"%((min+dur)//60+hour, (min+dur)%60))
    else: print("%d %d"%(hour+(min+dur)//60-24,(min+dur)%60))

