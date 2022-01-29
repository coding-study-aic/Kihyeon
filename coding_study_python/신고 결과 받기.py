def solution(id_list, report, k):
    answer = [0] * len(id_list)    
    cnt = {x : 0 for x in id_list}
    reported = []
    report = set(report)

    for i in report:
        cnt[i.split()[1]] += 1
        
    for i in cnt.items():
        if i[1] >= k:
            reported.append(i[0])
    
    for i in report:
        if i.split()[1] in reported:
            answer[id_list.index(i.split()[0])] += 1
    return answer