string = list(str(input()))
for i in string:
  if i.isupper() == True:
    print(i.lower(), end='')
  else:
    print(i.upper(), end='')