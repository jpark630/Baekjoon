total_cost = int(input())
number = int(input())
total_sum = 0
n = 0
while(n < number):
  cost, num = map(int, input().split())
  total_sum += cost*num
  n += 1

if(total_cost == total_sum):
  print('Yes')
else:
  print('No')