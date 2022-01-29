def solution(lottos, win_nums):
    answer = []
    rank = [6,5,4,3,2]
    cnt = 0
    zero = lottos.count(0)
    
    for i in lottos:
        if i in win_nums:
            cnt += 1

    
    if cnt+zero in rank:
        answer.append(rank.index(cnt+zero)+1)
    else:
        answer.append(6)
    if cnt in rank:
        answer.append(rank.index(cnt)+1)
    else:
        answer.append(6)
    
    return answer

### 더 간편 
def solution(lottos, win_nums):
    answer = 0
    rank = [6,6,5,4,3,2,1]
    zero = lottos.count(0)
    for i in lottos:
        if i in win_nums:
            answer += 1
    
    return rank[answer + zero], rank[answer]