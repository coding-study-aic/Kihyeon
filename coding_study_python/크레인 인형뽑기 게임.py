def solution(board, moves):
    answer = 0
    bucket = []
    board_change = list(map(list, zip(*board)))
    for i in board_change:
        while 0 in i:
            i.remove(0)

    for i in moves:
        if board_change[i-1]:
            bucket.append(board_change[i-1].pop(0))
            
        if len(bucket) >= 2 and bucket[-2] == bucket[-1]:
            bucket.pop()
            bucket.pop()
            answer += 2
            
    return answer