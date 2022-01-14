from collections import deque

def solution(prices):
    answer = []
    pricesq = deque(prices)

    while pricesq:
        cur = pricesq.popleft()
        cnt = 0
        for i in pricesq:
            cnt += 1
            if cur > i:
                break
        answer.append(cnt)

    return answer

if __name__ == "__main__":
    prices = [1, 2, 3, 2, 3]
    # return = [4, 3, 1, 1, 0]
    
    print(solution(prices))
