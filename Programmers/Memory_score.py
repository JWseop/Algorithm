# https://school.programmers.co.kr/learn/courses/30/lessons/176963
# Lv.1
# 문제: 추억점수

def solution(name, yearning, photo):
    name_dict={name_:yearning_ for yearning_, name_ in zip(yearning, name)}
    answer = []
    for i in range(0,len(photo)):
        result=0
        for j in range(0,len(photo[i])):
            if(photo[i][j] in name_dict):
                result=name_dict[photo[i][j]]+result
        answer.append(result)
    return answer