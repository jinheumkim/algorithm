def solution(number):
    answer = 0
    for i in range(len(number)):
        for j in range(len(number)):
            for k in range(len(number)):
                if i<j<k:
                    if number[i]+number[j]+number[k] == 0:
                        answer += 1
                    
    return answer