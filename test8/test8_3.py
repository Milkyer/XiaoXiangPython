# -*-coding:utf-8-*-
# 功能：AQI空气质量计算,json转换csv文件格式

import json
import csv

#解码json文件
def process_json_file(filepath):
    f = open(filepath, mode='r', encoding='utf-8')
    city_list = json.load(f)
    return city_list

def main():
    filepath = input('请输入json文件名称:')
    city_list = process_json_file(filepath)
    city_list.sort(key=lambda city: city['aqi'])

    lines = []
    #列名
    lines.append(list(city_list[0].keys()))
    for city in city_list:
        lines.append(list(city.values()))

    f = open('aqi.csv', 'w', encoding='utf-8', newline='')
    writer = csv.writer(f)
    for line in lines:
        writer.writerow(line)
    f.close()

if __name__ == '__main__':
    main()
