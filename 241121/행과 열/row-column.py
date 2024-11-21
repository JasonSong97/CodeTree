# 변수 선언 및 입력
inp = input()
arr = inp.split()
a = int(arr[0])
b = int(arr[1])
	
# n칸의 정사각형에 i * j를 출력합니다.
for i in range(1, a + 1):
	for j in range(1, b + 1):
		print(i * j, end=" ")
	print()