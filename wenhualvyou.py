import requests
from lxml import html
import re
import time
import pymysql
import base64
from services.reques_http import RequestHandler
import random


def fac():
    url_start = "http://zwgk.mct.gov.cn/zfxxgkml/zcfg/zcjd/202012/t20201205_915379.html"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36 Edg/84.0.522.49"
    }
    params = {"sn": "a14062711010650606ss9p000000", "size": "0"}
    response = requests.get(url=url_start, params=params, headers=headers)
    response.encoding = "utf-8"
    pages_text = response.text
    etree = html.etree
    tree = etree.HTML(pages_text)
    zhuti1 = tree.xpath(
        '/html/body/div[1]/div/div[2]/div[2]/div[1]/div[1]/dl/dd/text()')
    zhuti2 = tree.xpath(
        '/html/body/div[1]/div/div[2]/div[2]/div[1]/div[1]/dl/dd/div/text()')
    zhuti3 = tree.xpath(
        '/html/body/div[1]/div/div[2]/div[2]/div[1]/div[1]/dl/dd/div/div/text()')
    zhuti = zhuti1 + zhuti2 + zhuti3
    zt = []
    for x in zhuti:
        zt.append(x.replace(u'\u3000', u' ').replace(u'\xa0', u' '))
    zhuti = [x.strip() for x in zt if x.strip() != '']
    souyinhao = tree.xpath(
        '//*[@class="content_head mhide"]/div[2]/dl[@class="tb1"]/dd/text()')
    # souyinhao = tree.xpath('//div[@class="bod_head"]/dl[@class="tb1"]/dd[2]/text()')
    # souyinhao = tree.xpath('//*[@class="tb1"]/dd/text()')
    fabujigou = tree.xpath(
        '//*[@class="content_head mhide"]/div[3]/dl[1]/dd/text()')
    faburiqi = tree.xpath(
        '//*[@class="content_head mhide"]/div[3]/dl[2]/dd/text()')
    felei = tree.xpath(
        '//*[@class="content_head mhide"]/div[4]/dl[1]/dd/text()')
    fl = []
    for x in felei:
        fl.append(x.replace(u'\u3000', u' ').replace(u'\xa0', u' '))
    felei = [x.strip() for x in fl if x.strip() != '']
    # felei = [neirong5 + "\n" for neirong5 in felei]
    zhutici = tree.xpath(
        '//*[@class="content_head mhide"]/div[4]/dl[2]/dd/text()')
    neirong1 = tree.xpath('//*[@class="gsj_htmlcon_bot"]/div[1]/p//text()')
    neirong2 = tree.xpath('//*[@id="ozoom"]/founder-content/p//text()')
    neirong3 = tree.xpath('//*[@class="gsj_htmlcon_bot"]/p//text()')
    neirong4 = tree.xpath('//*[@style="line-height: 150%;"]//text()')
    neirong5 = tree.xpath(
        '/html/body/div[1]/div/div[2]/div[2]/div[2]/div[2]/div/text()')
    neirong6 = tree.xpath(
        '/html/body/div[1]/div/div[2]/div[2]/div[2]/div[2]/div/font/text()')
    neirong7 = tree.xpath(
        '/html/body/div[1]/div/div[2]/div[2]/div[2]/div[2]/font/font/text()')
    neirong8 = tree.xpath(
        '/html/body/div[1]/div/div[2]/div[2]/div[2]/div[2]/div[1]/div/p/text()')
    neirong9 = tree.xpath(
        '/html/body/div[1]/div/div[2]/div[2]/div[2]/div[2]/div[1]/div/p/span/text()')
    neirong10 = tree.xpath(
        '/html/body/div[1]/div/div[2]/div[2]/div[2]/div[2]/font/text()')
    neirong11 = tree.xpath(
        '/html/body/div[1]/div/div[2]/div[2]/div[2]/div[2]/div[1]/div/div/p/span/text()')
    neirong12 = tree.xpath(
        '/html/body/div[1]/div/div[2]/div[2]/div[2]/div[2]/div[1]/div/span/p/font/text()')
    neirong13 = tree.xpath('//*[@id="ozoom"]/p/font/text()')
    neirong14 = tree.xpath(
        '/html/body/div[1]/div/div[2]/div[2]/div[2]/div[2]/div[1]/div/p/font/text()')
    neirong16 = tree.xpath(
        '/html/body/div[1]/div/div[2]/div[2]/div[2]/div[2]/div[1]/font/p/font/text()')
    neirong15 = tree.xpath(
        '/html/body/div[1]/div/div[2]/div[2]/div[2]/div[2]/div[1]/font/font/text()')
    neirong17 = tree.xpath(
        '/html/body/div[1]/div/div[2]/div[2]/div[2]/div[2]/div[1]/div/span/div/p/font/span/text()')
    neirong18 = tree.xpath('//*[@id="lTitle"]/p/font/text()')
    neirong19 = tree.xpath(
        '/html/body/div[1]/div/div[2]/div[2]/div[2]/div[2]/div[1]/div/p/font/span/text()')
    neirong = neirong1+neirong2+neirong3+neirong4+neirong5+neirong6+neirong7+neirong8+neirong9 + \
        neirong10+neirong11+neirong12+neirong13+neirong14 + \
        neirong15+neirong16+neirong17+neirong18+neirong19
    nr = []
    for x in neirong:
        nr.append(x.replace(u'\u3000', u' ').replace(u'\xa0', u' '))
    neirong = [x.strip() for x in nr if x.strip() != '']
    bqsy = '版权所有：中华人民共和国文化和旅游部'
    dz = '地址：东城区朝阳门北大街10号'
    yzbm = '邮政编码：100020'
    icp = 'ICP备案编号：京ICP备05084924号'
    dh = '电话：010-59881114'
    wzbs = "网站标识码bm23000001"
    jgwab = '京公网安备110401300059号'
    keys = base64.b64encode(url_start.encode("utf8"))
    key = str(keys, encoding="utf8")

    print(key)
    print(zhuti)
    print(souyinhao)
    print(fabujigou)
    print(faburiqi)
    print(felei)
    print(zhutici)
    print(neirong)
    print(bqsy)
    print(dz)
    print(yzbm)
    print(icp)
    print(dh)
    print(wzbs)
    print(jgwab)

    HEADERS = {"Content-Type": "application/json; "}
    url = '1270.0.01:9400/user/_doc/1'

    body = {
        "key": key,
        "yzbm": bqsy,
        "dfds": {
            "key": key,
            "yzbm": bqsy,
        }
    }

    RequestHandler.put(url=url, data=body, headers=HEADERS)


# for i in (1, 4):
#     fac()

# connect = pymysql.Connect(host='localhost', port=3306, user="root", passwd="1842505833", db="XCX",
#                               charset='utf8')
# cursor = connect.cursor()
# sql = 'INSERT ignore INTO wenhuahelvyoubu(`key`,zhuti,souyinhao,fabujigou,faburiqi,felei,zhutici,neirong,bqsy,dz,yzbm,icp,dh,wzbs,jgwab)VALUES("' + str(key) + '","' + str(zhuti) + '","' + str(souyinhao) + '","' + str(fabujigou) + '","' + str(faburiqi) + '","' + str(felei) + '","' + str(zhutici) + '","' + str(neirong) + '","' + str(bqsy) + '","' + str(dz) + '","' + str(yzbm) + '","' + str(icp) + '","' + str(dh) + '","' + str(wzbs) + '","' + str(jgwab) + '")'
# cursor.execute(sql)
# connect.commit()
# connect.close()
