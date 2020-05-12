# -*-coding:utf-8-*-
# 功能：52周存钱挑战,记录每周的存款数
import math

def main():

    i = 1                #记录周数
    money_per_week = 10  #每周存入的金额
    increase_money = 10  #递增的金额
    total_week = 52      #总共的周数
    saving = 0           #账户累计金额

    money_list = []      #记录每周的存款数的列表

    while i <= total_week:
        # saving += money_per_week
        money_list.append(money_per_week)
        saving = math.fsum(money_list)
        print('第{}周，存入{}元，账户累计{}元。'.format(i,money_per_week,saving))
        money_per_week += increase_money
        i += 1


if __name__ == '__main__':
    main()