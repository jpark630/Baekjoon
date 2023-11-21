l = []
for i in range(5):
  m = int(input())
  l.append(m)
print(int(sum(l)/5))
l.sort()
print(l[2])