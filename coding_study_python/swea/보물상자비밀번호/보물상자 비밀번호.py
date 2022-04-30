import sys

sys.stdin = open("/Users/gimgihyeon/Desktop/coding_test/coding_study_git/Kihyeon/coding_study_python/swea/보물상자비밀번호/sample_input.txt", "r")

T = int(input())

for test_case in range(1, T+1):
    N, K = list(map(int, input().split())) # [12, 10]
    numbers = list(input())
    n = N // 4

    pw = set()

    for r in range(n):
        numbers = list(numbers[-1]) + numbers[:-1]
        
        tmp = 0
        for i in range(1,5):
            arr = numbers[tmp:n*i] # numbers[(N // 4) * i:(N // 4) * (i + 1)]
            tmp = n*i
            ten = 0

            # 이렇게 쓰면 진수 변환 간단히 가능.
            # pw.add(int(''.join(arr), 16))

            for idx, j in enumerate(reversed(arr)): 
                if j>='A' and j<='Z':
                    ten += (16**idx) * (ord(j)-ord('A')+10)
                else: 
                    ten += (16**idx) * int(j)

            pw.add(ten) # update([1,3,5])
    
    
    listpw = list(pw)
    listpw.sort(reverse=True)

    print('#{} {}'.format(test_case, listpw[K-1]))