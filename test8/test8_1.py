# -*-coding:utf-8-*-
# 功能：AQI空气质量计算

#范围缩放
def cal_linear(iaqi_lo, iaqi_hi, bp_lo, bp_hi, cp):
    iaqi = (iaqi_hi - iaqi_lo) * (cp - bp_lo) / (bp_hi - bp_lo) + iaqi_lo
    return iaqi


def cal_pm_iaqi(pm_val):
    if 0 <= pm_val < 36:
        iaqi = cal_linear(0, 50, 0, 35, pm_val)
    elif 36 <= pm_val < 76:
        iaqi = cal_linear(50, 100, 35, 75, pm_val)
    elif 76 <= pm_val < 116:
        iaqi = cal_linear(100, 150, 75, 115, pm_val)
    else:
        pass


def cal_co_iaqi(co_val):
    if 0 <= co_val < 36:
        iaqi = cal_linear(0, 50, 0, 3, co_val)
    elif 36 <= co_val < 76:
        iaqi = cal_linear(50, 100, 2, 4, co_val)
    else:
        pass



def cal_aqi(param_list):
    pm_val = param_list[0]
    co_val = param_list[1]
    pm_iaqi = cal_pm_iaqi(pm_val)
    co_iaqi = cal_co_iaqi(co_val)

    iaqi_list = []
    iaqi_list.append(pm_iaqi)
    iaqi_list.append(co_iaqi)


def main():
    input('请输入以下信息，用空格分隔')
    input_str = input('(1)PM2.5 (2)CO:')
    str_list = input_str.split(' ')
    pm_val = float(str_list[0])
    co_val = float(str_list[1])

    param_list = []
    param_list.append(pm_val)
    param_list.append(co_val)

    #调用AQI计算器
    aqi_val = cal_aqi(param_list)
    print('空气质量指数：{}'.format(aqi_val))


if __name__ == '__main__':
    main()
