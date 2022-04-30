def solution(abilities, k):
    answer = 0
    abilities.sort(reverse = True)

    if len(abilities)%2 != 0:
        answer += abilities[-1]
        k -= 1

    for i in range((len(abilities))//2):
        if k > 0:
            answer += abilities[i*2]
        else:
            answer += abilities[i*2+1]

    return answer