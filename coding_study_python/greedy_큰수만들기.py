def solution(number, k):
    answer = []

    for i in number:
        if not answer:
            answer.append(i)
            continue

        while 1:
            if k <= 0 or not answer:
                break
            if answer[-1] < i:
                answer.pop(-1)
                k -= 1
            else: break
        answer.append(i)
    
    if k > 0:
        answer = answer[:-k]
    return ''.join(answer)

if __name__ == "__main__":
    print(solution("1924", 2), "94")
    print(solution("1231234", 3), "3234")
    print(solution("4177252841", 4), "775841")
    print(solution("919911", 2), "9991")
    print(solution("21", 1), "2")