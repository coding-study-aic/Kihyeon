def solution(jobs):
    jobs.sort()
    cnt = len(jobs)
    start, time = jobs.pop(0)
    answer = time
    # 현재 태스크가 종료될 시간 
    end = start + time

    while jobs:
        jobs.sort()
        # 종료 시간 안에 요청된 태스크들 
        ls = []
        for i, j in jobs:
            if i <= end:
                ls.append([i,j])

        # 만약 있다면 종료시간 안에 요청된 태스크 중에서 길이 가장 짧은 것 수횅
        if ls:
            ls.sort(key = lambda x : x[1])
            end += ls[0][1]
            answer += end - ls[0][0]
            jobs.remove(ls[0])
        else:
            answer += jobs.pop(0)[1]

    return answer//cnt

if __name__ == "__main__":
    jobs = [[0, 3], [1, 9], [2, 6]]
    # return = 9
    
    # jobs =  [[24, 10], [28, 39], [43, 20], [37, 5], [47, 22], [20, 47], [15, 34], [15, 2], [35, 43], [26, 1]]
    # # return = 72

    # jobs = [[0, 5], [2, 10], [10000, 2]]
    # # return = 6

    # jobs = [[1, 9], [1, 4], [1, 5], [1, 7], [1, 3]] 
    # # # return = 13

    # print(solution(jobs))
    print(solution([[0, 9], [1, 1], [1, 1], [1, 1], [1, 1]]))
    # print(solution([[0, 10], [2, 10], [9, 10], [15, 2]]), 14)
    # print(solution([[0, 10], [2, 12], [9, 19], [15, 17]]), 25)
    # print(solution([[0, 3], [1, 9], [2, 6]]), 9)
    # print(solution([[0, 1]]), 1)
    # print(solution([[1000, 1000]]), 1000)
    # print(solution([[0, 1], [0, 1], [0, 1]]), 2)
    # print(solution([[0, 1], [0, 1], [0, 1], [0, 1]]), 2)
    # print(solution([[0, 1], [1000, 1000]]), 500)
    # print(solution([[100, 100], [1000, 1000]]), 500)
    # print(solution([[10, 10], [30, 10], [50, 2], [51, 2]]), 6)
    # print(solution([[0, 3], [1, 9], [2, 6], [30, 3]]), 7)
    print(solution([[0, 10], [4, 10], [5, 11], [15, 2]]), 15)
    print(solution(	[[0, 10]]), 10)
    print(solution([[0, 10], [2, 3], [9, 3]]), 9)
    print(solution([[0, 3], [4, 3], [10, 3]]), 3)