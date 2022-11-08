n = int(input())
temp = 0 
for i in range(n+1):
  list_i = list(map(int, str(i)))
  if i + sum(list_i) == n:
    temp += 1
    print(i)
    break
if temp == 0:
  print(0)