# -*-coding:utf-8-*-
# 功能：AQI空气质量计算,写AQI排名前五的json数据

import json

#解码json文件
def process_json_file(filepath):
    f = open(filepath, mode='r', encoding='utf-8')
    city_list = json.load(f)
    return city_list

def main():
    filepath = input('请输入json文件名称:')
    city_list = process_json_file(filepath)
    city_list.sort(key=lambda city: city['aqi'])
    top5_list = city_list[:5]

    f = open('top5_aqi.json', mode='w', encoding='utf-8')
    json.dump(top5_list, f, ensure_ascii=False)
    f.close()


if __name__ == '__main__':
    main()