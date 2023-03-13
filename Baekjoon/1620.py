from sys import stdin

def input():
    return stdin.readline().rstrip() # readline()에 디폴트로 포함되는 개행문자 제거 -> rstrip


#1. 사용자로부터 N과 M을 입력 받아 변수에 저장한다.
n, m = map(int, input().split(' '))
dogamId = {} 
dogamName = {}
answer = ""

#2. N번 만큼 돌면서, 포켓몬의 이름을 입력 받아 할당 id와 이름을 각각 dogamName과 dogamID에 추가한다.
for i in range(n):
    poketmon = input()

    # (조건) 포켓몬의 이름은 2~20자 + 첫 글자 혹은 마지막 글자만 대문자를 제한으로 한다.
    if len(poketmon) < 2 or len(poketmon) > 20:
        print("이름 다시 입력!\n")
        i -= 1
        continue
    elif not poketmon[1:len(poketmon)-2].islower():
        print("이름 다시 입력!\n")
        i -= 1
        continue

    dogamId[poketmon] = i+1
    dogamName[i+1] = poketmon


#3. M번 만큼 돌면서, 문제를 입력 받고, 해당 문제의 결과를 찾아 리스트로 저장한다.
for _ in range(m):
    qna = input()
    # 숫자를 입력 받으면 -> 이름
    if qna.isdigit():
        answer += f"{dogamName[int(qna)]}\n"

    # 알파벳 입력 받으면 -> 번호
    else:
        answer += f"{dogamId[qna]}\n"
    
#4. answer을 한 번에 출력한다.
print(answer)