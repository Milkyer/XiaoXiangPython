# -*-coding:utf-8-*-
# 功能：模拟掷骰子
import random

def roll_dice():
    roll = random.randint(1,6)
    return roll

def main():
    total_times = 10
    #初始化列表[0,0,0,0,0,0]
    result_list = [0] * 6

    for i in range(total_times):
        roll = roll_dice()
        for j in range(1,7):
            if roll == j:
                result_list[j - 1] += 1

    for i,result in enumerate(result_list):
        print('点数{}的次数：{}'.format(i+1,result,))

if __name__ == '__main__':
    main()