def d(c):
  temp = list(map(int, list(str(c))))
  sub = 0
  #temp
  if len(temp) == 1:
    return 1
  elif len(temp) == 2:
    return 1
  else:
    sub = temp[0] - temp[1]
    for j in range(1, len(temp)-1):
      if temp[j] - temp[j+1] == sub:
        continue
      else:
        return 0
  return 1
lim = int(input())
cnt = 0
array = []
if lim == 1:
  print(1)
else:
  for i in range(1, lim+1):
    if d(i)==1:
      cnt += 1
      array.append(i)
    else:
      continue
  print(cnt)