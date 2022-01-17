def solution(n, lost, reserve):
    lost.sort()
    reserve.sort()

    # 여벌 체육복 있는 학생이 도난당했을 경우 빌려주지 않음. 교집합
    nlost = list(set(lost) - set(reserve))
    nreserve = list(set(reserve) - set(lost))

    tmp = []
    for i in nreserve:
        # 앞번호에게 빌려줌
        if (i-1) in nlost and i not in tmp:
            nlost.remove(i-1)
            tmp.append(i)

        # 뒷번호에게 빌려줌
        elif (i+1) in nlost and i not in tmp:
            nlost.remove(i+1)
            tmp.append(i)

    return n - len(nlost)

if __name__ == "__main__":
    print(solution(5, [2, 4], [1, 3, 5]), "5")
    print(solution(5, [2, 4], [3]), "4")
    print(solution(3, [3], [1]), "2")