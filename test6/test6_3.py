# -*-coding:utf-8-*-
# 功能：判断密码强度,保存密码及强度文件，读取文件中的密码

def main():
    #读取文件
    f = open('D:\\password.txt','r')
    #1.read()
    # content = f.read()
    # print(content)

    #2.readline()
    # line = f.readline()
    # print(line)
    # line = f.readline()
    # print(line)

    #3.readlines()
    # for line in f.readlines():
    for line in f:
        print('read:{}'.format(line))

    f.close()


if __name__ == '__main__':
    main()