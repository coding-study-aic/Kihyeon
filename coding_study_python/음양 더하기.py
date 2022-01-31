def solution(absolutes, signs):
    answer = 0

    for i in range(len(absolutes)):
        if signs[i] == False:
            answer -= absolutes[i]
            print(answer)
        else:
            answer += absolutes[i]
    
    return answer