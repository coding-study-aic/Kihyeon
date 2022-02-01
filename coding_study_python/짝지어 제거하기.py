## 스택 사용
def solution(s):
    ls = []

    for i in s:
        if not ls:
            ls.append(i)
            continue
        
        if ls[-1] == i:
            ls.pop()
        else:
            ls.append(i)

    if ls:
        return 0
    else:
        return 1

if __name__ == "__main__":
    print(solution("baabaa"))
    print(solution("aaa"))
