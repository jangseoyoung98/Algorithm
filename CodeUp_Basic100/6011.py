# Algorithm to print real number
# input : one real number(double type) -> val 'temp'
# output : one real number (which is changed to double type)

# 실수를 입력 받아 변수에 저장한다.
temp = input()
# 변수의 값을 실수로 변환한다. -> ★ input을 통해 받은 값은 '문자열'이다!
temp = float(temp)
# 변수에 담긴 실수값을 출력한다.
print(temp)