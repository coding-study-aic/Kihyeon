import itertools

def solution(orders, course):
    answer = []
    
    for i in course:
        combis= []
        for menu in orders:
            combis.append(list(itertools.combinations(sorted(list(menu)), i)))
        
        cnt_arr = []
        arr = []
        for idx, com in enumerate(combis):
            if idx == len(combis)-1:
                break
            
            for c in com:
                tmp = idx
                cnt = 0
                while tmp < len(combis):
                    if c in combis[tmp]:
                        cnt += 1
                    tmp += 1
                cnt_arr.append(cnt)
                arr.append(c)

        for t in range(len(arr)):
            if cnt_arr[t] >= 2 and cnt_arr[t] == max(cnt_arr):
                answer.append(''.join(arr[t]))
                    
                    
    answer = sorted(list(set(answer)))
            
    
    return answer


## 간단한 풀이 방법
import collections
import itertools

def solution(orders, course):
    result = []

    for course_size in course:
        order_combinations = []
        for order in orders:
            order_combinations += itertools.combinations(sorted(order), course_size)

        most_ordered = collections.Counter(order_combinations).most_common()
        result += [ k for k, v in most_ordered if v > 1 and v == most_ordered[0][1] ]

    return [ ''.join(v) for v in sorted(result) ]