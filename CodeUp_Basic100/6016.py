# Algorithm to print 2 characters with opposite order received
# input : 2 characters (with blank)
# output : 2 characters with opposite order

# 2개의 문자를 받아 변수에 담는다.
# a = input()
# # 입력받은 문자열을 공백을 기준으로 나눠 변수에 담는다. 
# a = a.split()
a, b = input().split()
# 2 문자의 순서를 바꿔 출력한다.
# print(a[1], a[0])
print(b, a)