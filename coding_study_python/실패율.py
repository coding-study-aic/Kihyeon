def solution(N, stages):
    answer = []
    stage_dic = {i : 0 for i in range(1,N+1)}
    
    for i in range(1,N+1):
        # 스테이지에 도달한 플레이어 수
        players = 0
        # 클리어하지 못한 플레이어 수
        fail = 0
        
        for stage in stages:
            if i <= stage:
                players += 1
            if i == stage:
                fail += 1
        
        if players != 0:
            stage_dic[i] = fail/players
        else:
            stage_dic[i] = 0
        
    sorted_dict = sorted(stage_dic.items(), key = lambda item: item[1], reverse = True)
    
    for i in sorted_dict:
        answer.append(i[0])

    return answer

# 실패율 : 스테이지에 도달했으나 아직 클리어하지 못한 플레이어의 수 / 스테이지에 도달한 플레이어 수