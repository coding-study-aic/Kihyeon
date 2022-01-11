import math

def solution(progresses, speeds):
    answer = []
    day = []
    tmp = 0
    for i in range(len(progresses)):
        day.append(math.ceil((100-progresses[i])/speeds[i]))
        print(day)

        if i > 0 and max(day) == day[i] and day.count(day[i]) == 1:
            answer.append(tmp)
            print(tmp)
            tmp = 0
        tmp += 1

    if(tmp > 0):
        answer.append(tmp)
        print(tmp)
    print(answer)
    return answer

if __name__ == "__main__":
    # progresses = [93, 30, 55]
    # speeds = [1, 30, 5]
    # # result = [2, 1]

    # progresses = [95, 90, 99, 99, 80, 99]
    # speeds = [1, 1, 1, 1, 1, 1]
    # # result = [1, 3, 2]

    # progresses = [20, 99, 93, 30, 55, 10]
    # speeds = [5, 10, 1, 1, 30, 5]
    # # result = [3, 3]

    progresses = [99,99,99]
    speeds = [1,1,1]
    # result = [3]
    solution(progresses, speeds)