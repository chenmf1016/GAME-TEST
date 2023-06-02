from playgame import go_a_game

shout = {'com1': 0, 'player': 1, 'com2': 0, 'com3': 1}


# 游戏进行次数及玩家输赢次数统计
def times_calculate():
    all_times = 0
    tie_times = 0
    user_win_times = 0
    user_loss_times = 0
    while True:
        player, score, r, shout = go_a_game.play_one_round(go_a_game.p, go_a_game.score)
        shout_to_name = number_to_name_shout(shout)
        new_score = play_score(score)
        all_times = all_times + 1
        if len(player) > 1:
            if r[0] == 0:
                tie_times = tie_times + 1
                print('第' + str(all_times) + '轮平局，结果如下：')
                shuchu_jieguo_tie(new_score, shout_to_name)
            elif 'player' in r:
                user_win_times = user_win_times + 1
                print('第' + str(all_times) + '轮玩家胜，结果如下：')
                shuchu_jieguo_win_loss(new_score, shout_to_name, r)
            else:
                user_loss_times = user_loss_times + 1
                print('第' + str(all_times) + '轮玩家输，结果如下：')
                shuchu_jieguo_win_loss(new_score, shout_to_name, r)
        else:
            print('=========游戏结束=========')
            if r[0] == 0:
                tie_times = tie_times + 1
            elif 'player' in r:
                user_win_times = user_win_times + 1
            else:
                user_loss_times = user_loss_times + 1
            for k, v in new_score.items():
                print('获胜玩家：' + k)
                print('总分：' + str(v))
            break
    return all_times, tie_times, user_win_times, user_loss_times


# 游戏输赢概率计算
def prob_calculate():
    all_times, tie_times, user_win_times, user_loss_times = times_calculate()
    print('=========本次战绩=========')
    print('此次游戏总共玩的次数：', all_times)
    player_win_prob = user_win_times / all_times
    tie_prob = tie_times / all_times
    print('平局次数：', tie_times)
    print('玩家获胜次数：', user_win_times)
    print('玩家获胜的概率：', player_win_prob)
    print('打平的概率：', tie_prob)


# 将玩家所喊的数字转化为文字
def number_to_name_shout(shout):
    for k, v in shout.items():
        if v == 0:
            shout[k] = '鸡'
            # print(shout[k])
        elif v == 1:
            shout[k] = '老虎'
        elif v == 2:
            shout[k] = '棒子'
    return shout


# 将玩家及分数字典重新组合，输出一个玩家+分数集
def play_score(score):
    play_and_score = {}
    for k, v in score.items():
        if 'com1' in k:
            play_and_score.update({'com1': v})
        elif 'com2' in k:
            play_and_score.update({'com2': v})
        elif 'com3' in k:
            play_and_score.update({'com3': v})
        elif 'player' in k:
            play_and_score.update({'player': v})
    return play_and_score


# 输出每一轮平局游戏的结果
def shuchu_jieguo_tie(play_name, shout):
    for p_k, p_v in play_name.items():
        for s_k, s_v in shout.items():
            if p_k == s_k:
                print(str(p_k) + '(' + str(play_name[p_k]) + ')' + ':' + str(shout[p_k]))


# 输出每一轮有胜负游戏的结果
def shuchu_jieguo_win_loss(play_name, shout, code_list):
    for p_k, p_v in play_name.items():
        for s_k, s_v in shout.items():
            if p_k == s_k:
                if p_k in code_list:
                    print(str(p_k) + '(' + str(play_name[p_k]) + ',获胜' + ')' + ':' + str(shout[p_k]))
                else:
                    print(str(p_k) + '(' + str(play_name[p_k]) + ',失败' + ')' + ':' + str(shout[p_k]))


if __name__ == '__main__':
    times_calculate()
    prob_calculate()
    number_to_name_shout(shout)
    play_score(go_a_game.score)
