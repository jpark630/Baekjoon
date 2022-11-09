T = int(input())
for i in range(T):
  H, W, N = map(int, input().split())
  r = N//H + 1
  f = N%H
  if f == 0:
    f = H
    r -= 1
  r = format(r, '02')
  print('%d%s'%(f, r))