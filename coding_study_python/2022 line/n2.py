def solution(sentences, n):
    answer = 0

    alpha = [[] for _ in range(len(sentences))]
    score = [0 for _ in range(len(sentences))]

    for idx, i in enumerate(sentences):
        score[idx] = len(i)
        for j in i:
            if j.isupper():
                score[idx] += 1
                alpha[idx].append(ord(j)-65)
                alpha[idx].append(-999)

            else:
                alpha[idx].append(ord(j)-97)
            alpha[idx] = list(set(alpha[idx]))
            if -65 in alpha[idx]:
                alpha[idx].remove(-65)

    for idx, i in enumerate(alpha[:-1]):
        answer += score[idx]
        for jdx, j in enumerate(alpha[1:]):
            if idx == jdx:
                continue
            if list(set(j) & set(i)) == set(i):
                answer += score[jdx]

    return answer