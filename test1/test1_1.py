# -*-coding:utf-8-*-
# 汇率兑换案例1
rmb_str_value = input('请输入人民币(CNY)金额:')
rmb_value = eval(rmb_str_value)
USD_VS_RMB = 6.77
usd = rmb_value / USD_VS_RMB
print('美元(USD)金额是：', usd)
