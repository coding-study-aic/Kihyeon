import itertools

def isPrime(num):
    if num == 1 or num == 0:
        return False
    
    for i in range(2, num//2 +1):
        if num % i == 0:
            return False
    
    return True

def solution(nums):
    answer = 0
    sum_combi = []
    
    combi = list(set(itertools.combinations(nums, 3)))
    sum_combi = [sum(tup) for tup in combi]
    
    for i in sum_combi:
        if isPrime(i):
            answer += 1
            
    return answer