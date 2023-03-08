# 정수 n개의 합을 구하는 함수 작성하기
# input : a (리스트)
# output : int (a에 담긴 정수의 총합)
# conditions
# 1) 0 <= a[i] <= 1,000,000
# 2) 1 <= n <= 3,000,000

# 첫 번째 시도
def solve(a):
    ans = 0
    for i in a:
        ans += i
    return ans

# 두 번째 시도 -> sum() 내장 함수 사용
def solve(a):
    return sum(a)




