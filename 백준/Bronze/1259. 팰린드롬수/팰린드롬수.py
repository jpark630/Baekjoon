while(True):
  n = input()
  if n != '0':
    if n == n[::-1]:
      print('yes')
    else:
      print('no')
  else:
    break