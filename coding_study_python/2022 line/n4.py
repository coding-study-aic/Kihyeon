def solution(arr, brr):
    answer = 0

    tmp = arr[:1] + arr[1:]
    for idx, i in enumerate(arr):
        if tmp[idx] < brr[idx]:
            if idx+1 < len(tmp):
                tmp[idx+1] -= brr[idx] - tmp[idx]
                tmp[idx] = brr[idx]
                answer += 1

        elif tmp[idx] > brr[idx]:
            if idx+1 < len(tmp):
                tmp[idx+1] += tmp[idx] - brr[idx]
                tmp[idx] = brr[idx]
                answer += 1

    return answer