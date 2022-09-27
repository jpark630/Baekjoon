a = input()
b = input()
a = int(a)
b = int(b)
b_1 = b%10
b //= 10
print(a*b_1)
b_2 = b%10
b //= 10
print(a*b_2)
b_3 = b%10
print(a*b_3)
print((a*b_3)*100+(a*b_2)*10+(a*b_1))