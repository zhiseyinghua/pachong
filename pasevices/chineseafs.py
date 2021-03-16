import requests
from services.reques_http import RequestHandler
from urllib import parse
import json
import time


'''
这是一个爬取2021年实体经济企业经营预期调查网站的类
例子网站：http://data.chineseafs.org/report/setting/charts/view/6034c3cf9fc2a2d4e4f25394/
'''


class Chineseafs:
    def getManyChineseafst(self, amount):
        print(amount)
        for i in range(1):
            print("123", i)
            data = getOneChineseafst(page=10)


# 这是获取企业名称城市联系电话http请求
# 它只获取一条数据
# page 是一个字符串
def getOneChineseafst(page):
    print(page)
    HEADERS = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36", "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
               "Cookie": "__xsrf=2|ac4b4a2a|fe9aa0e57c0cee349776b6c7bee3f658|1615787795; _sessionid='2|1:0|10:1615793811|10:_sessionid|88:ZjhkMDRlZjZhOWRlNTExYTM4YWFmMjQ4ZjYzYjJjYTczNWE4MWQ0ZGFmMjVkMmJlZGE3ZGE1MDA0ODMzNmNjMQ==|38638517332a98dd1fac179f37069ca6d106a65d001491bb1a91e82f066d73c4'; i18next=en; Hm_lvt_2515953efbf2c7b9b2e46a6da74c8f02=1615795285; Hm_lpvt_2515953efbf2c7b9b2e46a6da74c8f02=1615795285; 6034c3cf9fc2a2d4e4f25394%7Cv=15; 6034c3cf9fc2a2d4e4f25394=187507; VCODE=2293"}
    url = 'http://data.chineseafs.org/report/ajax/chart_info/60374d590ee9c30001b2d655/'

    body = {
        "page": page,
        "question_id": "6034d6979fc2a2d4e4f45d23",
        "__xsrf": "2|ac4b4a2a|fe9aa0e57c0cee349776b6c7bee3f658|1615787795"
    }

    data = parse.urlencode(body)
    # print(data)
    # print(HEADERS)

    # res = RequestHandler().post(url, data=data, headers=HEADERS)
    res = {
        "status": "200",
        "datas": {
            "table_data": {
                "rspd_count": "3095",
                "cur_page": "10",
                "columns": [
                    {
                        "value": [
                            {
                                "text": "贵州华科铝材料工程技术研究有限公司",
                                "seq": "178545"
                            },
                            {
                                "text": "新疆天山军垦牧业有限责任公司(141畜欣旺)",
                                "seq": "178551"
                            },
                            {
                                "text": "贵州嘉盈科技有限公司",
                                "seq": "178552"
                            },
                            {
                                "text": "固始县上一房地产开发有限公司",
                                "seq": "178553"
                            },
                            {
                                "text": "贵州古镇池酒业有限公司",
                                "seq": "178559"
                            },
                            {
                                "text": "石河子市新安镇双顺牧业有限公司141分公司",
                                "seq": "178580"
                            },
                            {
                                "text": "三都水族自治县国有林场投资开发有限公司",
                                "seq": "178584"
                            },
                            {
                                "text": "贵州融鹰塑业科技有限公司",
                                "seq": "178589"
                            },
                            {
                                "text": "三都水族自治县国有林场投资有限公司",
                                "seq": "178592"
                            },
                            {
                                "text": "三都水族自治县国有林场投资开发有限公司",
                                "seq": "178596"
                            }
                        ],
                        "label": "填空1"
                    },
                    {
                        "value": [
                            {
                                "text": "贵阳市",
                                "seq": "178545"
                            },
                            {
                                "text": "石河子141团3连",
                                "seq": "178551"
                            },
                            {
                                "text": "贵阳市白云区",
                                "seq": "178552"
                            },
                            {
                                "text": "信阳市固始县",
                                "seq": "178553"
                            },
                            {
                                "text": "贵阳",
                                "seq": "178559"
                            },
                            {
                                "text": "石河子市",
                                "seq": "178580"
                            },
                            {
                                "text": "三都县",
                                "seq": "178584"
                            },
                            {
                                "text": "贵州贵阳",
                                "seq": "178589"
                            },
                            {
                                "text": "贵州省",
                                "seq": "178592"
                            },
                            {
                                "text": "贵州三都县",
                                "seq": "178596"
                            }
                        ],
                        "label": "填空2"
                    },
                    {
                        "value": [
                            {
                                "text": "15285524453",
                                "seq": "178545"
                            },
                            {
                                "text": "13369932721",
                                "seq": "178551"
                            },
                            {
                                "text": "17885500623",
                                "seq": "178552"
                            },
                            {
                                "text": "13613971152",
                                "seq": "178553"
                            },
                            {
                                "text": "085184414019",
                                "seq": "178559"
                            },
                            {
                                "text": "13369932721",
                                "seq": "178580"
                            },
                            {
                                "text": "08544810335",
                                "seq": "178584"
                            },
                            {
                                "text": "13312253861",
                                "seq": "178589"
                            },
                            {
                                "text": "4810335",
                                "seq": "178592"
                            },
                            {
                                "text": "0854－4810335",
                                "seq": "178596"
                            }
                        ],
                        "label": "填空3"
                    }
                ],
                "total_page": "310"
            },
            "option_num": 3,
            "chart_type": "blank",
            "matrixrow_num": 0,
            "project_id": "6034c3cf9fc2a2d4e4f25394",
            "question_id": "6034d6979fc2a2d4e4f45d23"
        }
    }
    # print(res.encoding)
    # res.encoding = "gb2312"
    # res.content = 'utf-8'
    # a =res.text()
    # _locals = json.loads(res.text)['datas']['table_data']['columns'][0]

    # 用于取值的数据
    _company = res['datas']['table_data']['columns'][0]['value']
    _locals = res['datas']['table_data']['columns'][1]['value']
    _phone = res['datas']['table_data']['columns'][2]['value']
    print("1",_company)
    print("2",_locals)
    print("3",_phone)
    valueSeqList = []
    for item in _company:
        # print(item['seq'])
        valueSeqList.append(item['seq'])
    for newcompany, newlocals, newphone in zip(_company, _locals, _phone):
        print("123456789")
        print(newcompany['text'], newlocals['text'],
              newphone['text'], newphone['seq'])
        onekey = newphone['text'] + "_" + newphone['seq']
        print(onekey)
        cc = time.localtime(time.time())
        onekey = str(cc.tm_year)+'/'+str(cc.tm_mon)+'/'+str(cc.tm_mday) + "_" + newphone['text'] 
        print(onekey)
    return res
