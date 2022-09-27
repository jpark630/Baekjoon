a = int(input())
for i in range(0,a):
    sum = 0
    b = input()
    add = 1
    for j in range(0,len(b)):
        if b[j] == "O":
            sum += add
            add += 1
        else: add = 1
    print(sum)