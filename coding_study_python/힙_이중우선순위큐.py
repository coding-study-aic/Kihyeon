import heapq

def solution(operations):
    answer = []
    heap = []

    # 명령어확인 & 명령어 실행
    for i in operations:
        if i[0] == "I":
            heapq.heappush(heap, int(i[2:]))
        elif i[0] == "D":
            if i[2:] == "1" and heap:
                del heap[-1]
            elif i[2:] == "-1" and heap:
                heapq.heappop(heap)

    heap.sort()
    # 최댓값, 최소값 구하기
    if heap:
        answer.append(heap[-1])
        answer.append(heap[0])
    else:
        return [0,0]

    return answer

if __name__ == "__main__":
    print(solution(["I 16","D 1"]), "[0,0]")
    print(solution(["I 7","I 5","I -5","D -1"]), "[7,5]")
    print(solution(["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]), "[333, -45]")