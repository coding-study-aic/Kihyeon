from collections import Counter
def solution(nums):
    cnt = dict(Counter(nums))
    
    if len(cnt) >= len(nums)//2:
        return len(nums)//2
    else:
        return len(cnt)

# 더 간단 
def solution(nums):
    return min(len(set(nums)), len(nums)//2)