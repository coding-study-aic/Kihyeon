def solution(req_id, req_info):
    answer = []

    req = list(zip(req_id, req_info))
    sell = []
    buy = []
    for i in req:
        if i[1][0] == 1:
            sell.append(i)
        else:
            buy.append(i)

    sell = sorted(sell, key = lambda x:x[1][-1])
    buy = sorted(buy, key = lambda x:x[1][-1], reverse = True)

    person = []
    for i in buy:
        cnt = i[1][1]
        lose = 0
        get = 0
        for j in sell:
            tmp = []
            if cnt >= j[1][1]:
                tmp.append(j[0])
                tmp.append(str(j[1][1] * -1))
                tmp.append('+'+(str(j[1][2] * j[1][1])))
                answer.append(' '.join(tmp))
                lose += j[1][2] * j[1][1]
                get += j[1][1]
                cnt -= j[1][1]
            else: 
                break
        tmp = []

        if i[0] in person:
            break
        else: 
            person.append(i[0])
            tmp.append(i[0])

        if get != 0:
            tmp.append('+'+str(get))
        else:
            tmp.append(str(get))
        if lose != 0:
            tmp.append('-'+str(lose))
        else:
            tmp.append(str(lose))
        answer.append(' '.join(tmp))




    answer = list(set(answer))
    answer = sorted(answer, key = lambda x:x[0])
    return answer