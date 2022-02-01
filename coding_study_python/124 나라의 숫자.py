def solution(n):
    answer = ''
    arr = ['4','1','2',"4"]
    
    if n <= 3:
        return arr[n]
    
    while n > 3:
        answer += arr[n%3]
        if n%3 == 0:
            n -= 1
        n = n//3
        
    answer+= arr[n]

    return answer[::-1]