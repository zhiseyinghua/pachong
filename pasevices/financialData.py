import requests
from services.reques_http import RequestHandler
from urllib import parse
import json
import time
from services.mysql import MysqlOperation


'''
这是一个爬取2021年实体经济企业经营预期调查网站的类
例子网站：http://data.chineseafs.org/report/setting/charts/view/6034c3cf9fc2a2d4e4f25394/
'''


class Chineseafs:
    def getManyChineseafst(self, amount):
        print(amount)
        for i in range(1, amount):
            print("123456789")
            print(i)
            getOneChineseafst(page=i)


# 这是获取企业名称城市联系电话http请求,并存进数据库
# 它只获取一条数据
# page 是一个字符串

def getOneChineseafst(page):
    print("page", page)
    HEADERS = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36", "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
               "Cookie": '_sessionid="2|1:0|10:1615793811|10:_sessionid|88:ZjhkMDRlZjZhOWRlNTExYTM4YWFmMjQ4ZjYzYjJjYTczNWE4MWQ0ZGFmMjVkMmJlZGE3ZGE1MDA0ODMzNmNjMQ==|38638517332a98dd1fac179f37069ca6d106a65d001491bb1a91e82f066d73c4"; Hm_lvt_2515953efbf2c7b9b2e46a6da74c8f02=1615795285; 6034c3cf9fc2a2d4e4f25394%7Cv=15; 6034c3cf9fc2a2d4e4f25394=187507; __xsrf=2|32b1760e|fffd976fd08e2d917c0133507bdabdeb|1616040919'}
    url = 'http://data.chineseafs.org/report/ajax/chart_info/60374d590ee9c30001b2d654/'

    body = {
        "page": page,
        "question_id": "6034d6979fc2a2d4e4f45d23",
        "__xsrf": "2|32b1760e|fffd976fd08e2d917c0133507bdabdeb|1616040919"
    }

    data = parse.urlencode(body)
    res = RequestHandler().post(url, data=data, headers=HEADERS)

    # print(res.encoding)
    # print(res.text)
    # res.encoding = "gb2312"
    # res.text = 'utf-8'
    # a =res.text()
    newData = json.loads(res.text)
    print(newData)
    # 用于取值的数据
    _company = newData['datas']['table_data']['columns'][0]['value']
    _locals = newData['datas']['table_data']['columns'][1]['value']
    _phone = newData['datas']['table_data']['columns'][2]['value']
    # print("1", _company)
    # print("2", _locals)
    # print("3", _phone)
    valueSeqList = []
    for item in _company:
        # print(item['seq'])
        valueSeqList.append(item['seq'])
    for newcompany, newlocals, newphone in zip(_company, _locals, _phone):
        print(newcompany['text'], newlocals['text'],
              newphone['text'], newphone['seq'])
        tt = int(time.time())

        print(tt)
        # 数据库的逐渐
        onekey = str(tt) + "_" + newphone['text'] + "_" + newphone['seq']
        print(onekey)
        obj = MysqlOperation()  # 对象
        sql = """
            create table if not exists phone_company(
                runoob_key  varchar(30) not null,
                runoob_locla  text not null,
                runoob_company text not null,
                runoob_phone  varchar(12) not null,
                runoob_sign  varchar(12) not null,
                primary key ( `runoob_key` )
            )
        """
        # insertsql = "INSERT INTO phone_company (runoob_key, runoob_locla, runoob_company, runoob_phone, runoob_sign) VALUES ('%s', '%s',  %s,  '%s',  '%s')"
        # insertval = {
        #     'runoob_key', 'runoob_locla', 'runoob_company', 'runoob_phone', 'runoob_sign'
        # }
        insertsql = 'INSERT ignore INTO phone_company(runoob_key,runoob_locla,runoob_company,runoob_phone,runoob_sign)VALUES("' + onekey + \
            '","' + newlocals['text'] + '","' + newcompany['text'] + '","' + \
            newphone['text'] + '","' + newphone['seq'] + '")'
        obj.__enter__()
        obj.execute(sql)
        obj.execute(insertsql)
        obj.__exit__()
