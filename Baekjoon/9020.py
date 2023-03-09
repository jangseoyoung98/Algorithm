# 백준 9020번: 골드바흐의 추측
# Algorithm to 입력으로 들어온 짝수를 골드바흐의 파티션으로 출력한다.
# input : 테스트 케이스 갯수 T / 짝수인 정수 n
# output : 정수 n에 대한 골드바흐의 파티션 -> 소수는 작은 것부터, 여러 파티션 중에서는 둘 차이가 작은 것

# 0. T를 변수에 담아, T만큼 for문을 돌린다.
T = int(input())
n = int(input())
for i in range(T):
    # 1. n/2가 짝수라면 - n/2-1과 n/2+1
    #    n/2가 홀수라면 - n/2와 n/2
    if n % 2 == 0 : 
        left = n // 2 - 1
        right = n // 2 + 1
    else:
        left = right = n // 2
    
    # 2. 양 끝 단이 소수인지 검사해서 맞으면 바로 출력하고 / 아니면 -2와 +2씩 한다. (1보다 크고, n보다 작을 때까지)
    while(left >= 1 and right < n):
        isDec = 1
        for i in range(2, left // 2 + 1):
            if left % i == 0:
                isDec = 0
                break
            if right % i == 0:
                isDec = 0
                break
        
        if(isDec):
            print(left, right)
            break
        
        left -= 2
        right += 2


