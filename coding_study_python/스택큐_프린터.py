from collections import deque

def solution(priorities, location):

    answer = []

    q = deque()
    for i in range(len(priorities)):
        q.append((i, priorities[i]))

    while q:
        idx, prop = q.popleft()
        # print("pop", idx, prop)
        if not q:
            answer.append(idx)
            # print(answer)
            break
        for i in range(len(q)):
            if q[i][1] > prop:
                q.append((idx, prop))
                # print("push", idx, prop)
                # print(q)
                break
            else:
                if i == len(q) - 1:
                    answer.append(idx)
                    # print(answer)
                else:
                    continue
            # print(q)

    return answer.index(location)+1

if __name__ == "__main__":
    # priorities = [2, 1, 3, 2]
    # location = 2
    # # return = 1

    # priorities = [9,9,9,9,9]
    # location = 0
    # # return = 1

    priorities = [3]
    location = 0
    # return = 1
    
    print(solution(priorities, location))