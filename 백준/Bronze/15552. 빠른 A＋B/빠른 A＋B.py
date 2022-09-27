import sys

i = int(sys.stdin.readline())
a = 0
while(a<i):
    j,k= map(int, sys.stdin.readline().split())
    print(j+k)
    a += 1