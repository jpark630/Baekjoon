c = input()
cnt = 0
word_list = list(str(c)) #처음 받는 숫자 & 최종 숫자
temp = 0
temp_list = [] #word_list를 더한 숫자
result = []
sum = 0

while(True):
  if len(word_list) == 1:
    word_list.append(word_list[0])
    word_list[0] = str(0)
  temp = int(word_list[0])+int(word_list[1])
  temp_list = list(str(temp))
  if len(temp_list) == 1:
    temp_list.append(temp_list[0])
    temp_list[0] = str(0)
  word_list = str(word_list[1]+temp_list[1])
  cnt += 1
#  if word_list[0]=='0':
#    del word_list[0]
  if int(word_list) == int(c):
    break
print(cnt)
  