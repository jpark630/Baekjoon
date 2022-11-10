L = int(input())
temp_list = list(input())
sum = 0
for i in range(len(temp_list)):
  sum += (ord(temp_list[i])-96)*(31**i)
print(sum%1234567891)