# !/usr/bin/python
# -*- coding: utf-8 -*-
from shoutout import shout_out
from scorecalculate import socre_calculate

# 每个玩家的初始分数为100
score = {'com1_score': 100, 'com2_score': 100, 'com3_score': 100, 'player_score': 100}
# 定义玩家的姓名
p = {'com1_name', 'com2_name', 'com3_name', 'player_name'}


# 通过判断玩家的姓名来决定哪个是玩家哪个是电脑，如果是电脑则采用生成，如果是玩家则从【鸡，老虎，棒子】中选择输入
def shout_one_round(users):
    shout_dic = {}
    for name in users:
        if 'com1' in name:
            com1_code = shout_out.shout_out('suiji')
            shout_dic.update({'com1': com1_code})
        elif 'com2' in name:
            com2_code = shout_out.shout_out('suiji')
            shout_dic.update({'com2': com2_code})
        elif 'com3' in name:
            com3_code = shout_out.shout_out('suiji')
            shout_dic.update({'com3': com3_code})
        elif 'player' in name:
            # 如果是玩家的话，则由玩家自行出拳，玩家只能输入鸡，老虎，棒子，否则输入无效
            while True:
                player_code_in = input('请出拳（只能输入鸡，老虎，棒子）：')
                if '鸡' == player_code_in:
                    player_code = shout_out.shout_out(player_code_in)
                    shout_dic.update({'player': player_code})
                    break
                elif '老虎' == player_code_in:
                    player_code = shout_out.shout_out(player_code_in)
                    shout_dic.update({'player': player_code})
                    break
                elif '棒子' == player_code_in:
                    player_code = shout_out.shout_out(player_code_in)
                    shout_dic.update({'player': player_code})
                    break
                else:
                    print('您的输入无效，请重新输入！')
        else:
            break
    return shout_dic


def play_one_round(players, s):
    # 用列表存储最终的结果，0表示平局，非平局时返回获胜玩家
    result_list = []
    win_code_list = []
    # 判断玩家数量，如果大于1，则可以继续进行游戏
    if len(players) > 1:
        # 根据传入的玩家数据，算出各个玩家所喊的内容
        shout_result = shout_one_round(players)
        # 将产生的结果去重统计数量
        func = lambda z: dict([x, y] for y, x in z.items())
        shout_result_f = func(shout_result)
        # 如果去重后的数组的个数为1或者3个，则此局打成平手
        if len(set(shout_result_f)) == 1 or len(set(shout_result_f)) == 3:
            # 打成平手时，往结果数组内，加入一个0，然后调用平局时计算分数的函数并返回最终分数
            result_list.append(0)
            socre_calculate.score_cal_tie(s)
            return players, s, result_list, shout_result
        # 如果去重后的结果列表个数为2个，则需计算胜负
        elif len(set(shout_result_f)) == 2:
            # 定义一个列表来存储去重后的结果，只取key，即所喊的内容
            code_list_key = list()
            for key in shout_result_f.keys():
                code_list_key.append(key)
            # 将去重后所喊的结果分别存在code1和code2
            code1 = code_list_key[0]
            code2 = code_list_key[1]
            # 根据code1及code2的差值比较最终赢家
            code_compare = code1 - code2
            # 当code_compare等于1或者-2时，则code1为获胜方，code2为输的一方
            if code_compare == 1 or code_compare == -2:
                # 获取字典中对应value的key值，
                code1_list = return_key(code1, shout_result)
                code2_list = return_key(code2, shout_result)
                result_list = code1_list
                # win_code_list = code1_list
                # 根据输赢结果计算此局游戏各个玩家的最终分数
                s1 = socre_calculate.score_cal_win(code1_list, s)
                s = socre_calculate.score_cal_loss(code2_list, s1)
                # 判断玩家的分数，若分数为0，则玩家被从列表移除
                for key in list(s.keys()):
                    if s[key] == 0 or s[key] < 0:
                        if 'com1' in key:
                            print('com1分数耗尽，退出了游戏。')
                            players.remove('com1_name')
                            s.pop('com1_score')
                        elif 'com2' in key:
                            print('com2分数耗尽，退出了游戏。')
                            players.remove('com2_name')
                            s.pop('com2_score')
                        elif 'com3' in key:
                            print('com3分数耗尽，退出了游戏。')
                            players.remove('com3_name')
                            s.pop('com3_score')
                        elif 'player' in key:
                            print('您的分数为0，无法继续游戏，请等待决出胜负！！')
                            players.remove('player_name')
                            s.pop('player_score')
                return players, s, result_list, shout_result
            elif code_compare == -1 or code_compare == 2:
                # 当code_compare==2或者-1时，code1为输的一方，code2为胜方
                code1_list = return_key(code1, shout_result)
                code2_list = return_key(code2, shout_result)
                result_list = code2_list
                # win_code_list = code2_list
                # 根据输赢结果计算此局游戏各个玩家的最终分数
                s1 = socre_calculate.score_cal_win(code2_list, s)
                s = socre_calculate.score_cal_loss(code1_list, s1)
                # 判断玩家的分数，若分数为0，则玩家被从列表移除
                for key in list(s.keys()):
                    if s[key] == 0 or s[key] < 0:
                        if 'com1' in key:
                            print('com1分数耗尽，退出了游戏。')
                            players.remove('com1_name')
                            s.pop('com1_score')
                        elif 'com2' in key:
                            print('com2分数耗尽，退出了游戏。')
                            players.remove('com2_name')
                            s.pop('com2_score')
                        elif 'com3' in key:
                            print('com3分数耗尽，退出了游戏。')
                            players.remove('com3_name')
                            s.pop('com3_score')
                        elif 'player' in key:
                            print('您的分数为0，无法继续游戏，请等待决出胜负！！')
                            players.remove('player_name')
                            s.pop('player_score')
                return players, s, result_list, shout_result
    else:
        print('游戏结束啦')


# 获取字典中对应value所对应的key
def return_key(val, curr_dic):
    key_list = []
    for k, v in curr_dic.items():
        if v == val:
            key_list.append(k)
    return key_list


if __name__ == '__main__':
    shout_one_round(p)
    play_one_round(p, score)
