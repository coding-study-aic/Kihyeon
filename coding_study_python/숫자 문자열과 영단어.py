def solution(s):
    answer = ""
    num = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    
    for idx, i in enumerate(num):
        if s.find(i) != -1:
            s = s.replace(i, str(idx))
    
    return int(s)