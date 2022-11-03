sno = list(range(1,31))
while(True):
  try:
    temp = int(input())
    sno.remove(temp)
  except EOFError:
    break
for i in sno:
  print(i)