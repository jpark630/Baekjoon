x, y, w, h = map(int, input().split(' '))
test = [x, y, w-x, h-y]
print(min(test))