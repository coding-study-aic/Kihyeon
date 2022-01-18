def solution(name):
    answer = 0

    # A : 65, Z : 90
    # 이름의 글자 수 만큼 A로 채움 
    res = [65 for _ in range(len(name))]
    check = [False for _ in range(len(name))]
    i = 0
    a = 0
    al = []
    aid = []

    for idx in range(len(name)):
        if name[idx] == 'A':
            for j in name[idx:]:
                if j == 'A':
                    # answer -= 1
                    a += 1
                else:
                    break
        aid.append(idx)
        al.append(a)
        a = 0

    a = max(al)
    print(a, al, aid)
            
    if a > 0:
        answer -= a
    # if a > 1:
    #     answer +=1
    
    # for ci in range(a):
    #     check[aid[al.index(a)] + ci] = True

    print(check)    
    while not all(check):
        if check[i] == False:
            check[i] = True
            print(name[i], ord(name[i]), res[i], answer)

            # 알파벳이 Z에 더 가까울 경우 아래로 내리기 때문
            if ord(name[i]) != res[i] and ord(name[i]) > 77:
                res[i] = 91

            # 만약에 알파벳이 다르다면 횟수 1 추가, res 알파벳 1 증가.
            while ord(name[i]) != res[i]:
                # 만약 Z에 더 가깝다면 아래로
                if ord(name[i]) <= 77:
                    res[i] += 1
                else:
                    res[i] -= 1
                answer += 1
                
        if not all(check):
            answer += 1
            i += 1

    return answer

if __name__ == "__main__":
    print(solution("JEROEN"), "56")
    print(solution("JAN"), "23")
    print(solution("JAZ"), "11")
    print(solution("AABAB"), "5")
    print(solution("AAABAAAA"), "4")