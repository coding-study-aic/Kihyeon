import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    while scoville[0] < K:
        if len(scoville) > 1:
            fir = heapq.heappop(scoville)
            sec = heapq.heappop(scoville)
            heapq.heappush(scoville, fir+sec*2)
            answer += 1
        else:
            return -1

    return answer

if __name__ == "__main__":
    scoville = [1, 2, 3, 9, 10, 12]
    K = 7
    # return = 2

    # scoville = [1]
    # K = 1
    # # return = 2
    
    print(solution(scoville, K))