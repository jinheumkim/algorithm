def solution(a, b):
    days = [31,29,31,30,31,30,31,31,30,31,30,31]
    weeks = ["FRI","SAT","SUN","MON","TUE","WED","THU"]
    temp = 0
    if a == 1:
        temp = b % 7
    else :
        for i in range(a-1):
            temp += days[i]
        temp = (temp + b) % 7
        weeks[temp-1]
            
    return weeks[temp-1]