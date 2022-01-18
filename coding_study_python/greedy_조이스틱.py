def solution(name):
    answer = 0
    min_move = []

    # 상하, 좌우로 최솟값 고려
    # 상하 최솟값 - 위로 이동 vs Z로, 아래로 이동
    for i, ch in enumerate(name):
        tmp = min(ord(ch) - ord('A'), ord('Z') - ord(ch) + 1)
        min_move.append(tmp)

    i = 0
    while True:
        answer += min_move[i]
        min_move[i] = 0

        # A일 경우 넘어감
        if sum(min_move) == 0:
            break

        # 좌우 최솟값 - 오른쪽으로만 이동 vs 왼쪽으로 돌아가 이동 
        # A가 등장할 경우 반대쪽으로 이동할 경우 있음 (다시 처음으로 돌아간 후 뒤에서 마지막 A까지 이동)
        left,right = 1,1
        while min_move[i - left] == 0:
            left += 1
        while min_move[i + right] == 0:
            right += 1
        
        answer += left if left < right else right
        i += -left if left < right else right

    return answer

if __name__ == "__main__":
    print(solution("JEROEN"), "56")
    print(solution("JAN"), "23")
    print(solution("JAZ"), "11")
    print(solution("AABAB"), "5")
    print(solution("AAABAAAA"), "4")