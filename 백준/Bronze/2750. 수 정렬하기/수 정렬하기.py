n = int(input())
res = []
empty_list = []

for i in range(n):
    temp = int(input())  # 입력을 숫자로 변환
    empty_list.append(temp)

for j in range(n):
    for k in range(j + 1, n):  # j+1부터 시작하여 불필요한 비교 줄이기
        if empty_list[k] < empty_list[j]:
            empty_list[j], empty_list[k] = empty_list[k], empty_list[j]  # Pythonic한 스왑

for a in empty_list:
    print(a)
