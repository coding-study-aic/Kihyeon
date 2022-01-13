from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0

    waitq = deque(truck_weights)
    # bridge = [0] * bridge_length
    bridgeq = deque(0 for _ in range(bridge_length))
    completeq = deque()

    while len(completeq) < len(truck_weights):
        answer += 1
        tmp = bridgeq.popleft()
        if tmp != 0:
            completeq.append(tmp)
        if waitq and sum(bridgeq) + waitq[0] <= weight:
            bridgeq.append(waitq.popleft())
        else:
            bridgeq.append(0)

    return answer

if __name__ == "__main__":
    bridge_length = 2
    weight = 10
    truck_weights = [7,4,5,6]
    # return = 8

    # bridge_length = 100
    # weight = 100
    # truck_weights = [10]
    # # return = 101

    # bridge_length = 100
    # weight = 100
    # truck_weights = [10,10,10,10,10,10,10,10,10,10]	
    # # return = 110

    bridge_length = 5
    weight = 5
    truck_weights = [2, 2, 2, 2, 1, 1, 1, 1, 1]
    # return = 19
    
    print(solution(bridge_length, weight, truck_weights))