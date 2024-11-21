# 변수 선언 및 입력
inp = input()
arr = inp.split()
n = int(arr[0])
m = int(arr[1])

# n * n 크기의 별을 출력합니다.
for _ in range(n):
	for _ in range(m):
		print("*", end=" ")
	print()