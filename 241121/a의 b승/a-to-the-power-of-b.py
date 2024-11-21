# 변수 선언 및 입력
inp = input()
arr = inp.split()
a = int(arr[0])
b = int(arr[1])
prod = 1

# a를 b번 곱합니다.
for _ in range(b):
	prod *= a

# 출력
print(prod)