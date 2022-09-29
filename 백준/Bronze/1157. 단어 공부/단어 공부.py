word = list(input().upper())
temp_list = [0 for temp in range(len(word))]
word_list = []
for i in word:
  if i not in word_list:
    word_list.append(i)
  else:
    temp_index = word_list.index(i)
    temp_list[temp_index] += 1
max_index = temp_list.index(max(temp_list))
max_val = temp_list[max_index]
sum = 0
for j in temp_list:
  if max_val == j:
    sum += 1
if sum == 1:
  print(word_list[max_index])
else:
  print("?")