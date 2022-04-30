def solution(num_teams, remote_tasks, office_tasks, employees):
    answer = []

    team = [[] for _ in range(num_teams)]
    emp = [[] for _ in range(num_teams)]

    for idx, i in enumerate(employees):
        arr = i.split()
        emp[int(arr[0])-1].append(idx+1)

        for j in arr[1:]:
            if j in office_tasks:
                team[int(arr[0])-1].append(idx+1)
                break

    for idx, i in enumerate(team):
        if i == []:
            team[idx].append(emp[idx][0])


    team = sum(team, [])
    for i in range(1,len(employees)+1):
        if i not in team:
            answer.append(i)

    return answer