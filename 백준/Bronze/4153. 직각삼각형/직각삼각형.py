while(True):
  sum = 0
  a, b, c = map(int, input().split(' '))
  length = [a, b, c]
  if a == 0 & b == 0 & c == 0:
    break;
  else:
    temp = max(length)
    length.remove(temp)
    for i in length:
      sum += i**2
    if temp**2 == sum:
      print('right')
    else:
      print('wrong')