def d(n) -> int:
    temp = 0  # 각자리수를 더하기 위한 변수 생성
    for x in list(str(n)):
      temp = temp + int(x)  # 각자리수를 더해주어 a에 대입
    return n + temp

num = list(range(1,10000))
for i in range(1,10000):
  if d(i) in num:
    num.remove(d(i))
for j in num:
  print(j)