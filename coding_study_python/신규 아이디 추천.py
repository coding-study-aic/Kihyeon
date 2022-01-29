def solution(new_id):
    answer = ''
    possi = ['-', '_', '.']
    tmp = 0

    # step 1
    new_id = list(new_id.lower())
    
    for idx, i in enumerate(new_id):
        # step 2
        if not i.isalnum() and i not in possi:
            continue
        else:
            answer += i
        
    # step 3
    while ".." in answer:
        answer = answer.replace("..", ".")

    # step 4
    answer = answer.strip('.')

    # step 5
    if answer == '':
        return "aaa"
    # step 6
    if len(list(answer)) >= 16:
        answer = answer[:15]
        answer = answer.strip('.')

    # step 7
    while len(answer) <= 2 :
        answer += answer[-1]

    return ''.join(answer)


# 정규식 사용
import re

def solution(new_id):
    st = new_id
    st = st.lower()
    st = re.sub('[^a-z0-9\-_.]', '', st)
    st = re.sub('\.+', '.', st)
    st = re.sub('^[.]|[.]$', '', st)
    st = 'a' if len(st) == 0 else st[:15]
    st = re.sub('^[.]|[.]$', '', st)
    st = st if len(st) > 2 else st + st[-1] * (3-len(st))
    return st

if __name__ == "__main__":
    print(solution("...!@BaT#*..y.abcdefghijklm"))
    print(solution("z-+.^."))
    print(solution("=.="))
    print(solution("123_.def"))
    print(solution("abcdefghijklmn.p"))