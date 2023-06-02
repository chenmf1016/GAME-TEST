import random


# 将用户所喊字符转化为数字
def name_to_number(shout_name):
    if shout_name == '鸡':
        return 0
    elif shout_name == '老虎':
        return 1
    elif shout_name == '棒子':
        return 2
    else:
        return -1


# 将对应的数字转化为中文
def number_to_name(number):
    if number == 0:
        shout_name = '鸡'
    elif number == 1:
        shout_name = '老虎'
    elif number == 2:
        shout_name = '棒子'
    else:
        shout_name = '所喊无效'
    return shout_name


# 用户输入随机时，则走随机数，否则根据用户所喊的内容来返回数字
def shout_out(shout_name):
    if shout_name == 'suiji' or shout_name == '随机':
        number = random.randint(0, 2)
    else:
        number = name_to_number(shout_name)
    return number
