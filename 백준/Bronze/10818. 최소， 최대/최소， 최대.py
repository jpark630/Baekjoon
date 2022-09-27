a = int(input())
b = list(map(int, input().split()))
max = b[0]
min = b[0]
for i in range(1,a):
    if max < b[i]:
        max = b[i]
    if min > b[i]:
        min = b[i]
print("%d %d"%(min, max))