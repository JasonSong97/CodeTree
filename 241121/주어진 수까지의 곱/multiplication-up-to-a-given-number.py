# 변수 선언 및 입력
inp = input()
arr = inp.split()
a = int(arr[0])
b = int(arr[1])
prod = 1

# a부터 b까지의 수들을 곱합니다.
for i in range(a, b + 1):
    prod *= i

# 출력
print(prod)