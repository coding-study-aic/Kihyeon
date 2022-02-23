def solution(bridge_length, weight, truck_weights):
    answer = 0

    bridge = list(0 for _ in range(bridge_length))
    complete = []
    truck_len = len(truck_weights)

    while len(complete) < truck_len:
        answer += 1
        tmp = bridge.pop(0)
        if tmp != 0:
            complete.append(tmp)
        if truck_weights and sum(bridge) + truck_weights[0] <= weight:
            bridge.append(truck_weights.pop(0))
        else:
            bridge.append(0)

    return answer

from collections import deque
def solution2(bridge_length, weight, truck_weights):
    answer = 0

    bridge = deque(0 for _ in range(bridge_length))
    complete = []
    truck_len = len(truck_weights)

    while len(complete) < truck_len:
        answer += 1
        tmp = bridge.popleft()
        if tmp != 0:
            complete.append(tmp)
        if truck_weights and sum(bridge) + truck_weights[0] <= weight:
            bridge.append(truck_weights.pop(0))
        else:
            bridge.append(0)

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
    
    print(solution2(bridge_length, weight, truck_weights))