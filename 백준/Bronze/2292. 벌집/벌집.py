n = int(input())
b4 = n-1
i = 0
temp = 0
temp_list = [0]
while(True):
  if n == 1:
    print(1)
    break
  i += 1
  temp += i
  temp_list.append(temp)
#  print((temp_list[i-1]*6),b4,(temp_list[i]*6))
  if (temp_list[i-1]*6)<=b4<=(temp_list[i]*6):
    print(i+1)
    break