# -*-coding:utf-8-*-
# 功能：AQI空气质量计算,判断文件格式并进行相应操作

import json
import csv
import os

#处理json文件
def process_json_file(filepath):
    with open(filepath, mode='r', encoding='utf-8') as f:
        city_list = json.load(f)
    print(city_list)

#处理csv文件
def process_csv_file(filepath):
    with open(filepath, mode='r', encoding='utf-8', newline='') as f:
        reader = csv.reader(f)
        for row in reader:
            print(', '.join(row))


def main():
    filepath = input('请输入文件名称：')
    filename, file_ext = os.path.splitext(filepath)

    if file_ext == '.json':
        process_json_file(filepath)
    elif file_ext == '.csv':
        process_csv_file(filepath)
    else:
        print('不支持的文件格式！')

if __name__ == '__main__':
    main()
