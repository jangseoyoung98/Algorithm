# Algorithm to print two integers
# input : 2 integers (with blank)
# output : print 2 integers (with newline)

# 공백을 기준으로 2개의 정수를 입력 받아 변수에 저장한다.
# ★ split() 함수 -> 문자열을 나눠 리스트로 만듦
a = input().split(' ')
# 저장된 정수값을 줄 바꿈을 통해 출력한다.
print(a[0]+"\n"+a[1])
