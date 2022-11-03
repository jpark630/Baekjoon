n = int(input())
temp_list = list(map(int, input().split()))
find = int(input())
temp = 0
for i in temp_list:
  if i == find:
    temp += 1
  else:
    continue
print(temp)