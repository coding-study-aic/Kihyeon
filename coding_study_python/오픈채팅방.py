def solution(record):
    answer = []
    user = {}
    status = []

    for idx, i in enumerate(record):
        arr = i.split()
        if arr[0] == "Leave":
            status.append([arr[1],"나갔습니다."])
        elif arr[0] == "Enter":
            status.append([arr[1],"들어왔습니다."])
            user[arr[1]] = arr[2]
        if arr[0] == "Change":
            user[arr[1]] = arr[2]
            
    for i in status:
        answer.append(user[i[0]] + "님이 "+ i[1])
    return answer