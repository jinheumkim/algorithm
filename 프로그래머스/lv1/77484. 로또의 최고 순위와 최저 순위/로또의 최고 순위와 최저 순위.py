def solution(lottos, win_nums):
    same_num = (set(lottos) & set(win_nums))
    same_num = list(same_num)
    rank = [6,6,5,4,3,2,1]
    cnt_0 = lottos.count(0)
    answer = (rank[len(same_num)+ cnt_0] , rank[len(same_num)])
    if same_num == 0:
        answer == [1,6]
    return answer
