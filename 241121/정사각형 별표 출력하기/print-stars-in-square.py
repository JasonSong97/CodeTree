# 변수 선언 및 입력
n = int(input())

# n * n 크기의 별을 출력합니다.
for _ in range(n):
	for _ in range(n):
		print("*", end="")
	print()