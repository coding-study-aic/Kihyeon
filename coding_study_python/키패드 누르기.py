import math

def solution(numbers, hand):
    answer = ''
    L = [1,4,7,10]
    R = [3,6,9,12]
    tmpL = 10
    tmpR = 12
    
    for i in numbers:
        if i == 0:
            i = 11
        if i in L:
            answer+= "L"
            tmpL = i
        elif i in R:
            answer+= "R"
            tmpR = i
             
        else:
            if tmpR not in R:
                diffR = math.ceil(tmpR/3) - math.ceil(i/3)
                diffR = (-1 * diffR) if diffR < 0 else diffR
            if tmpL not in L:
                diffL = math.ceil(tmpL/3) - math.ceil(i/3)
                diffL = (-1 * diffL) if diffL < 0 else diffL
            if tmpL in L:
                diffL = math.ceil(tmpL/3) - math.ceil(i/3)
                diffL = (-1 * diffL) if diffL < 0 else diffL
                diffL += 1
            if tmpR in R:
                diffR = math.ceil(tmpR/3) - math.ceil(i/3)
                diffR = (-1 * diffR) if diffR < 0 else diffR
                diffR += 1
            
            if diffL < diffR:
                answer += "L"
                tmpL = i
            elif diffL > diffR:
                answer += "R"
                tmpR = i
            else:
                if hand == "right":
                    answer += "R"
                    tmpR = i
                else:
                    answer += "L"
                    tmpL = i
    
    return answer