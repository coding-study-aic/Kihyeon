def solution(a, b):
    answer = 0
    for idx, i in enumerate(a):
        answer += i * b[idx]
    
    return answer