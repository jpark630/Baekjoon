c = int(input())
for i in range(c):
  temp, result = input().split()
  for k in result:
    for j in range(int(temp)):
        print(k, end='')
  print()