from playgame import go_a_game

r = {}


# 当平局时，则不做任何处理，直接返回用户分数
def score_cal_tie(score):
    return score


# 当赢的时候，则对列表内的用户增加对应分数
def score_cal_win(result, score):
    for k_s, v in score.items():
        for i in range(len(result)):
            k_r = result[i]
            if k_r in k_s:
                score[k_s] = score[k_s] + 50
    return score
    pass


# 当输的时候，则对列表内的用户减少对应分数
def score_cal_loss(result, score):
    for k_s, v in score.items():
        for i in range(len(result)):
            k_r = result[i]
            if k_r in k_s:
                score[k_s] = score[k_s] - 50
    return score
    pass


if __name__ == '__main__':
    score_cal_tie(go_a_game.s)
    score_cal_win(r, go_a_game.s)
    score_cal_loss(r, go_a_game.s)
