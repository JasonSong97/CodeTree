# 변수 선언, 입력
inp = input()
arr = inp.split()
h = int(arr[0])
w = int(arr[1])

# 키(cm)에서 키(m)로 단위 환산을 한 뒤 
# 체질량지수 계산 식에 넣어야 함에 유의합니다.
bmi = w * 100 * 100 // (h * h)

# 출력
print(bmi)
if bmi >= 25:
	print("Obesity")