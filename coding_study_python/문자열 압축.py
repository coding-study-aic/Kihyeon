def solution(s):
    ans = []
    
    if len(s) == 1:
        return 1
    
    for i in range(1, len(s)//2+1):
        idx = 0
        answer = 0
        check = False
        tmp = 0
        
        while idx <len(s):
            if s[idx:idx+i] == s[idx+i:idx+i+i]:
                tmp += 1
                if check:
                    idx += i
                else:
                    answer += len(s[idx:idx+i])
                    idx += i
                    check = True
                    
            else:
                if check:
                    idx += i
                    if tmp+1 >= 10:
                        answer += 2
                    else:
                        answer += 1
                    check = False
                    tmp = 0
                else:
                    answer += len(s[idx:idx+i])
                    idx += i
                    tmp = 0
                    
        ans.append(answer)
    return min(ans)