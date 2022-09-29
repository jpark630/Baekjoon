test_list = list(map(int,input().split(' ')))
flag = 0
flag1= 0
i = 1
while i < len(test_list):
    if(test_list[i] < test_list[i - 1]):
        flag = 1
    if(test_list[i]>test_list[i-1]):
      flag1 = 1
    i += 1
if (flag == 0) :
    print ("ascending")
elif (flag1 == 0) :
    print ("descending")
else:
  print("mixed")