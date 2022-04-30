def solution(logs):
    answer = 0

    for i in logs:
        # 로그 길이가 100이 넘는 경우 
        if len(i) > 100:
            answer += 1
            continue

        arr = i.split(' ')
        # 로그 형식에 맞지 않는 경우 
        if 'team_name' not in arr or 'application_name' not in arr or 'error_level' not in arr or 'message' not in arr: 
            answer += 1
            continue

        # 내용에 공백이 있는 경우
        if len(arr) != 12:
            answer += 1
            continue

        # 메시지 내용에 숫자나 특수문자가 있는 경우
        if not arr[11].isalpha():
            answer += 1
            continue

    return answer