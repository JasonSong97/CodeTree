# 변수 선언, 입력
cnt = 0
for _ in range(10):
	a = int(input())
	
	if a % 2 == 1:
		cnt += 1

# 출력
print(cnt)