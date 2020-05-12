# -*-coding:utf-8-*-
# BMR计算器

def cal_bmr():
    print('请输入以下信息，用空格分割')
    input_str = input('性别 体重（kg） 身高（cm） 年龄：')
    str_list = input_str.split(' ')

    try:
        gender = str_list[0]
        weight = float(str_list[1])
        height = float(str_list[2])
        age = int(str_list[3])
        if gender == '男':
            bmr = 13.7 * weight + 5.0 * height - 6.8 * age + 66
        elif gender == '女':
            bmr = 9.6 * weight + 1.8 * height - 4.7 * age + 655
        else:
            bmr = -1

        if bmr != -1:
            print('性别：{}，体重：{}公斤，身高：{}厘米，年龄：{}岁'.format(gender, weight, height, age))
            print('基础代谢率:{}大卡'.format(bmr))
        else:
            print('暂不支持该性别')
    except ValueError:
        print('请输入正确的信息！')
    except IndexError:
        print('输入的信息过少！')
    except:
        print('程序异常！')

def main():
    y_or_n = input('用户是否退出程序(y/n):')

    while y_or_n != 'y':
        cal_bmr()

        print()  # 输出空行
        y_or_n = input('用户是否退出程序(y/n):')

if __name__ == '__main__':
    main()