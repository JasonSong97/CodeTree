# 변수 선언 및 입력
n = int(input())
	
# 숫자로 이루어진 삼각형을 출력합니다.
for i in range(n):
	for j in range(i + 1):
		print(j + 1, end=" ")
	print()