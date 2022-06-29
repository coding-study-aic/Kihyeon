'''
예제 입력 1 
1 0 0 0 0 0 2 2 1
0 0 3 0 0 0 0 1 4
예제 출력 1 
Yes
예제 입력 2 
0 0 0 0 0 0 0 1 0
1 0 0 0 0 0 0 4 0
예제 출력 2 
No
'''

answer = ""
A = list(map(int, input().split()))
B = list(map(int, input().split()))

for i in range(1,10):
    if sum(A[:i]) > sum(B[:i-1]):
        answer = "Yes"
        break
    answer = "No"

print(answer)