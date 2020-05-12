# -*-coding:utf-8-*-
# 功能：判断密码强度,面向对象编程，定义一个password和文件工具类

class PasswordTool:
    def __init__(self,password):
        #类的属性
        self.password = password
        self.strength_level = 0

    #类的方法
    def process_password(self):
        #规则1：密码长度大于8
        if len(self.password) >= 8:
            self.strength_level += 1
        else:
            print('密码长度要求至少8位！')

        #规则2：包含数字
        if self.check_number_exist():
            self.strength_level += 1
        else:
            print('密码要求包含数字！')

        #规则3：包含字母
        if self.check_letter_exist():
            self.strength_level += 1
        else:
            print('密码要求包含字母！')

    def check_number_exist(self):
        has_number = False
        for a in self.password:
            if a.isnumeric():
                has_number = True
                break
        return has_number

    def check_letter_exist(self):
        has_letter = False
        for b in self.password:
            if b.isalpha():
                has_letter = True
                break
        return has_letter

class FileTool:
    def __init__(self,filepath):
        self.filepath = filepath

    def write_to_file(self,line):
        f = open(self.filepath, 'a')
        f.write(line)
        f.close()

    def read_from_file(self):
        f = open(self.filepath,'r')
        lines = f.readlines()
        f.close()
        return lines

def main():
    try_times = 5
    filepath = 'D:\\password.txt'
    file_tool = FileTool(filepath)

    while try_times > 0:
        password = input('请输入密码：')
        #实例化密码工具对象
        password_tool = PasswordTool(password)
        password_tool.process_password()

        #写操作
        line = '密码：{}，强度：{}\n'.format(password,password_tool.strength_level)
        file_tool.write_to_file(line)

        if password_tool.strength_level == 3:
            print('恭喜，密码强度合格！')
            break
        else:
            print('密码强度不合格！')
            try_times -= 1

    if try_times <= 0:
        print('尝试次数过多，密码设置失败。')

    #读操作
    lines = file_tool.read_from_file()
    print(lines)

if __name__ == '__main__':
    main()