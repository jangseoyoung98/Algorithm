#1. 사용자로부터 N과 M을 입력 받아 변수에 저장한다.
n, m = map(int, input().split(' '))
dogam = []
answer = ""

#2. N번 만큼 돌면서, 포켓몬의 이름을 입력 받아 각 포켓몬을 딕셔너리 형태로 리스트에 저장한다.
for i in range(1, n + 1):
    pocketmon = input()

    # (조건) 포켓몬의 이름은 2~20자 + 첫 글자 혹은 마지막 글자만 대문자를 제한으로 한다.
    if len(pocketmon) < 2 or len(pocketmon) > 20:
        print("이름 다시 입력!\n")
        i -= 1
        continue
    elif not pocketmon[1:len(pocketmon)-2].islower():
        print("이름 다시 입력!\n")
        i -= 1
        continue

    dogam.append({'num': i, 'name':pocketmon})

#3. M번 만큼 돌면서, 문제를 입력 받고, 해당 문제의 결과를 찾아 리스트로 저장한다.
for i in range(m):
    qna = input()
    # 알파벳 입력 받으면 -> 번호
    if(ord(qna[0:1]) >= 65 and ord(qna[0:1]) <= 122):
        # 해당 포켓몬의 번호를 찾아서
        # index = dogam.index({'name':qna})
        ret = next((item for item in dogam if item['name'] == qna), None)
        # answer에 넣는다.
        answer += f"{ret['num']}\n"

    # 숫자를 입력 받으면 -> 이름
    else:
        # 해당 포켓몬의 이름을 찾아서
        # index = dogam.index({'num':int(qna)})
        ret = next((item for item in dogam if item['num'] == int(qna)), None)
        # answer에 넣는다.
        answer += f"{ret['name']}\n"
    
#4. answer을 한 번에 출력한다.
print(answer)