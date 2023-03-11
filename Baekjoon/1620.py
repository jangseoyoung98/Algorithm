
#1. 입력 받은 값을 cnt(도감 내 갯수), problem(풀어야 하는 문제 갯수)에 담는다.
cnt, problem = map(int, input().split(' '))
dogam = {}

#2. cnt만큼 돌면서 입력받을 때마다 (숫자, 입력값) 튜플 형태로 딕셔너리에 넣는다.
for i in range(cnt):
    value = input()
    dogam[i+1] = value

valueList = list(dogam.values()) # 키들만 따로 리스트를 만들어, 추후 키값 추출이 가능하게 한다.
result = ""

#3. 숫자를 입력 받으면 -> 밸류값을 / 문자열을 입력 받으면 -> 키값을 출력한다.
for i in range(problem):
    find = input()

    if ord(find[0:1]) >= 65 and ord(find[0:1]) < 97: #문자열일 때
        result += f"\n{valueList.index(find)+1}"
    else: # 숫자일 때
        result += f"\n{dogam.get(int(find))}"

print(result)

## 시간 초과가 어디서 발생하는 건지..?


### 딕셔너리 요소 추가 : dogam[키] = '밸류'
### 딕셔너리 밸류 찾기 : dogam.get(키)
### 파이썬 특정 요소의 인덱스 추출 : .index(요소)
### 파이썬 앞글자만 가져오기 : string[start:end]
### map() -> 리스트의 요소를 한 번에 처리할 때(주로 형변환) 사용하는 함수
### 파이썬 형변환 : int형으로 -> ord() / str 형으로 -> str()

