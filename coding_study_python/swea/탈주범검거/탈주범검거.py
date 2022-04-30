# 표준 입력 예제
'''
a = int(input())                        정수형 변수 1개 입력 받는 예제
b, c = map(int, input().split())        정수형 변수 2개 입력 받는 예제 
d = float(input())                      실수형 변수 1개 입력 받는 예제
e, f, g = map(float, input().split())   실수형 변수 3개 입력 받는 예제
h = input()                             문자열 변수 1개 입력 받는 예제
'''

# 표준 출력 예제
'''
a, b = 6, 3
c, d, e = 1.0, 2.5, 3.4
f = "ABC"
print(a)                                정수형 변수 1개 출력하는 예제
print(b, end = " ")                     줄바꿈 하지 않고 정수형 변수와 공백을 출력하는 예제
print(c, d, e)                          실수형 변수 3개 출력하는 예제
print(f)                                문자열 1개 출력하는 예제
'''

import sys

sys.stdin = open("/Users/gimgihyeon/Desktop/coding_test/coding_study_git/Kihyeon/coding_study_python/swea/탈주범검거/sample_input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N,M,R,C,L = map(int, input().split())
    answer = 0

    # 이렇게 한줄로 표현도 가능.
    # under = [list(map(int(), input().split())) for _ in range(N)
    under = []
    for n in range(N):
        under.append(list(map(int, input().split())))

    visit = [[0 for _ in range(M)] for _ in range(N)]
    q = []
    q.append((R, C, 1))
    visit[R][C] = 1
    answer += 1

    direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    tunnel = [[], [0, 1, 2, 3], [0, 1], [2, 3], [0, 3], [1, 3], [1, 2], [0, 2]]
    temp = [1, 0, 3, 2] # i  0 : 1, i 1 : 0, i 2 : 3, i 3 : 2
    

    while len(q) > 0:
        x, y, time = q.pop(0)
        if time == L:
            continue
        t = under[x][y] # 1~7 (0~6)
        for i in tunnel[t]:
            dx, dy = direction[i]
            nx = x + dx
            ny = y + dy
            if 0 <= nx < N and 0 <= ny < M and not visit[nx][ny]:
                nt = under[nx][ny]
                if temp[i] in tunnel[nt]:
                    q.append((nx, ny, time + 1))
                    visit[nx][ny] = time+1
                    answer += 1
    
    # for i in range(N):
    #     for j in range(M):
    #         print(visit[i][j], end = '')
    #     print()
    print('#{} {}'.format(test_case, answer))

    # def DFS(x, y):
    #     if END(x, y):
    #         return?

    #     if visitable(x, y):
    #         DFS(x + , y +)

    #     return