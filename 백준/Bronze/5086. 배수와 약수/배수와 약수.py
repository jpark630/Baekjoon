while(True):
  m,n = map(int, input().split())
  if m == 0:
    break
  if m>n and m%n == 0:
    print("multiple")
  elif m<n and n%m == 0:
    print("factor")
  else:
    print("neither")