import sys

sys.stdin = open("/Users/gimgihyeon/Desktop/coding_test/coding_study_git/Kihyeon/coding_study_python/swea/보급로/input.txt", "r")

T = int(input())
direction = [(1,0), (-1,0), (0,1), (0,-1)]
for test_case in range(1, T+1):
    N = int(input())
    road = []
    for n in range(N):
        road.append(list(map(int, input())))

    visit = [[9999 for _ in range(N)] for _ in range(N)]
    q=[]
    q.append((0,0,0))
    visit[0][0] = 0

    min_time = 2000
    
    while len(q) > 0:
        x,y,t = q.pop(0)

        if x == N-1 and y == N-1:
            if t < min_time:
                min_time = t
            continue

        for nx,ny in direction:
            nx +=x
            ny +=y
            

            if nx >=0 and nx < N and ny >= 0 and ny < N:
                nt = t+road[nx][ny]
                if nt < visit[nx][ny]:
                    q.append((nx,ny,nt))
                    visit[nx][ny] = nt

    print('#{} {}'.format(test_case, min_time))

