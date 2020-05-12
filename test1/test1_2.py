# -*-coding:utf-8-*-
# 汇率兑换案例2:根据输入判断是人民币还是美元，进行相应的转换计算，进行循环输入
USD_VS_RMB = 6.77
currency_str_value = input('请输入带单位的货币金额(退出程序请输入Q):')
unit = currency_str_value[-3:]
value = currency_str_value[:-3]

i=0
while currency_str_value != 'Q':
    i = i + 1
    print('循环次数：',i)
    if unit == 'CNY':
        result = eval(value) / USD_VS_RMB
        print('转换后美元金额是：', result,'USD')
    elif unit == 'USD':
        result = eval(value) * USD_VS_RMB
        print('转换后人民币金额是：', result, 'CNY')
    else:
        print('暂不支持该货币，请重新输入！')

    print('************************************')
    currency_str_value = input('请输入带单位的货币金额(退出程序请输入Q):')

print('程序已退出！')