# 변수 선언, 입력
inp = input()
arr = inp.split()
a = int(arr[0])
b = int(arr[1])

# 출력
for i in range(b, a - 1, -1):
	print(i, end=" ")