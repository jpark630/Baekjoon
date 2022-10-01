num = int(input())
rslt = list(map(int, input().split(' ')))
M = max(rslt)
new_rslt = []
for i in rslt:
  new_rslt.append(float(i/M*100))
total = sum(new_rslt)
print(total/num)