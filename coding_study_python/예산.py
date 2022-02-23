def solution(d, budget):
    answer = 0
    d.sort()
    sum = 0
    for i in d:
        sum += i
        if sum <= budget:
            answer += 1

    return answer

# buget과 비교하여 더 크면 그 값을 빼나가는 방법도 있음.
def solution(d, budget):
    d.sort()
    while budget < sum(d):
        d.pop()
    return len(d)