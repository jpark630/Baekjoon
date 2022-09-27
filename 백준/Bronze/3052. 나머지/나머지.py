rmndr = []

for i in range(10):
  temp = int(input())
  r_temp = temp%42
  if r_temp in rmndr:
    continue
  else:
    rmndr.append(r_temp)
print(len(rmndr))