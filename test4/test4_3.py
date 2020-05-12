# -*-coding:utf-8-*-
# 功能：52周存钱挑战,可得到某周的存款总金额
import math
import datetime

def save_money(money_per_week,increase_money,total_week):
    money_list = []  # 记录每周的存款数的列表
    saved_money_list = []   #记录每周账户累计金额

    for i in range(total_week):
        money_list.append(money_per_week)
        saving = math.fsum(money_list)
        saved_money_list.append(saving)
        #print('第{}周，存入{}元，账户累计{}元。'.format(i + 1, money_per_week, saving))
        money_per_week += increase_money
    return saved_money_list

def main():
    money_per_week = float(input('请输入每周存入的金额：'))  #每周存入的金额
    increase_money = float(input('请输入每周递增的金额：'))  #递增的金额
    total_week = int(input('请输入总共的周数：'))      #总共的周数

    saved_money_list = save_money(money_per_week,increase_money,total_week)

    input_date_str = input('请输入日期（yyyy/mm/dd）:')
    input_date = datetime.datetime.strptime(input_date_str, '%Y/%m/%d')
    #isocalendar()返回年份、这一年的第几周、周几,[1]则取第几周
    week_num = input_date.isocalendar()[1]
    print('第{}周的存款：{}元'.format(week_num,saved_money_list[week_num - 1]))

if __name__ == '__main__':
    main()