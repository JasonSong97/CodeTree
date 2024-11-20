# 변수 선언, 입력
temp = int(input())

# 출력
if temp < 0:
	print("ice");
elif temp >= 100:
	print("vapor");
else:
	print("water");