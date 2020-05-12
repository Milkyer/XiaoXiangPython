# -*-coding:utf-8-*-
# 功能：52周存钱挑战,记录每周的存款数
import math
import datetime

saving = 0
def save_money(money_per_week,increase_money,total_week):
    global saving    #全局变量的使用要加global（可删）
    money_list = []  # 记录每周的存款数的列表

    for i in range(total_week):
        money_list.append(money_per_week)
        saving = math.fsum(money_list)

        print('第{}周，存入{}元，账户累计{}元。'.format(i + 1, money_per_week, saving))
        money_per_week += increase_money
    return saving

def main():
    money_per_week = float(input('请输入每周存入的金额：'))  #每周存入的金额
    increase_money = float(input('请输入每周递增的金额：'))  #递增的金额
    total_week = int(input('请输入总共的周数：'))      #总共的周数
    saved_money_list = save_money(money_per_week,increase_money,total_week)
    print('总金额是：',saving)

if __name__ == '__main__':
    main()