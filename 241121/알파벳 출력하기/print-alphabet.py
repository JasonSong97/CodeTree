# 변수 선언 및 입력
n = int(input())
cnt = 'A'
	
# 알파벳을 삼각형 모양으로 출력합니다.
for i in range(n):
	for _ in range(i + 1):
		print(cnt, end="")
		cnt = chr(ord(cnt) + 1)
		if ord(cnt) > ord('Z'):
			cnt = 'A'
	print()