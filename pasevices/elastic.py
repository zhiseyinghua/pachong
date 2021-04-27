import requests
from services.reques_http import RequestHandler
from urllib import parse
import json
import time
from services.mysql import MysqlOperation


'''
更改接口方法
'''


class gaijiekou:
    def getElastic(self):
        getAlllastic()


def getAlllastic():
    HEADERS = {"Content-Type": "application/json"}
    url = 'http://121.4.210.49:80/development_and_reform_commission/_doc/_search'

    body = {
        "query": {
            "match_all": {}
        }
    }

    data = parse.urlencode(body)
    res = RequestHandler().get(url, data=data, headers=HEADERS)
    newData = json.loads(res.text)
    datalist = newData['hits']['hits']
    print(datalist)
    for item in datalist:
        if type(item['_source']['accessory']) == list:
            print("123")
        elif item['_source']['accessory'] == '':
            item['_source']['accessory'] = []
            postOneElast(item['_source']['range'], item['_source'])
        else:
            item['_source']['accessory'] = [item['_source']['accessory']]
            postOneElast(item['_source']['range'], item['_source'])


def postOneElast(range, data):
    HEADERS = {"Content-Type": "application/json", "Connection": "keep-alive"}
    print(range)
    print(data)
    url = 'http://121.4.210.49:80/development_and_reform_commission/_doc/' + range
    print(url)
    newData = json.dumps(data)
    res = RequestHandler().put(url, data=newData, headers=HEADERS)

    print(res.text)
    # newData = json.loads(res.text)
