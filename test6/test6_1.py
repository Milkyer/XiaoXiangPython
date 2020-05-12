# -*-coding:utf-8-*-
# 功能：判断密码强度

def check_number_exist(password_str):
    has_number = False
    for a in password_str:
        if a.isnumeric():
            has_number = True
            break
    return has_number

def check_letter_exist(password_str):
    has_letter = False
    for b in password_str:
        if b.isalpha():
            has_letter = True
            break
    return has_letter


def main():
    try_times = 5

    while try_times > 0:
        password = input('请输入密码：')
        #密码强度
        strength_level = 0
        #规则1：密码长度大于8
        if len(password) >= 8:
            strength_level += 1
        else:
            print('密码长度要求至少8位！')

        #规则2：包含数字
        if check_number_exist(password):
            strength_level += 1
        else:
            print('密码要求包含数字！')

        #规则2：包含字母
        if check_letter_exist(password):
            strength_level += 1
        else:
            print('密码要求包含字母！')

        if strength_level == 3:
            print('恭喜，密码强度合格！')
            break
        else:
            print('密码强度不合格！')
            try_times -= 1
    if try_times <= 0:
        print('尝试次数过多，密码设置失败。')

if __name__ == '__main__':
    main()