#1. 갯수 T를 입력 받는다.
T = int(input())
nList = []
answer= ""

#2. T만큼 돌리면서 n을 입력 받는다. (n1, n2, ... nT)
for _ in range(T):
    n = int(input())
    nList.append(n)

#3. 리스트에 들어간 n들에 대해 약수&소수 판별한다.
# 1) 입력 받은 n의 약수를 구한다. -> n/2부터 시작해서, 양쪽으로 퍼지기 
# -> 여기서 for문을 돌리면 안 될 거 같다..
# -> 번갈아서 /2 한 약수가 짝수-짝수 / 홀수-홀수로 나뉜다.
## -> 짝수-짝수인 경우 바로 건너 뛰기

for n in nList:
    temp = n // 2
    isPrime = False
    
    if n % 2 == 0: # 짝수라면 -> prime1과 2는 동일한 값
        # prime1, prime2 = temp, temp -> 가능..?
        prime1 = temp
        prime2 = temp
    else: # 홀수라면 -> prime1은 그대로, 2는 +1 한 값
        prime1 = temp
        prime2 = temp + 1   

for i in (temp, 2, -2):
    # 2) 그 약수가 소수인지 판단한다.
    # -> 변수 true/false 조건을 걸어 다룬다.
    prime1 = n - i
    prime2 = i
    for j in range(2, temp-1):
        if temp % j == 0:
            break
        else:
            isPrime = True
    # 3) 발견한 소수를 문자열에 저장한다.
    if isPrime == True:
        answer += f"{prime1} {prime2}\n"




#3. 다 끝난 문자열을 출력한다.
print(answer)




