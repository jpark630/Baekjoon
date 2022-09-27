b = []
for j in range(0,9):
    b.append(int(input()))
max = 0
max_index = 0
for i in range(0,9):
    if max < b[i]:
        max = b[i]
        max_index = i+1
print("%d"%max)
print("%d"%max_index)