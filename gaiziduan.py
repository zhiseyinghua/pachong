from services.reques_http import RequestHandler
import json


def gaiziduan(data, id):

    _dict = {
        "fourteen_or_fifteen": "十四五",
        "the_ecological_environment": "生态环境",
        "economic": "经济",
        "new_energy": "新能源",
        "social": "社会",
        "education": "教育",
        "real_estate": "房产",
        "intellectual_property": "知识产权",
        "science_and_technology": "科技",
        "political": "政治",
        "military": "军事",
        "rural_agricultural": "农村农业",
        "medical": "医疗",
        "overcome_poverty": "脱贫扶贫",
        "construction": "建设",
        "tourism": "旅游",
        "other": "其他"
    }
    print(data)
    # res = RequestHandler().put(_url)
    _url = "http://121.4.210.49:80/central_peoples_government/_doc/" + id + "/" + "_update"
    # print("是否存在", ("key_words" in data) & ("zh_hans_keyword" in data))
    if ("key_words" in data) & (not ("zh_hans_keyword" in data)):
        key_word = data['key_words']
        try:
            for i, item in enumerate(key_word):
                # print(item, i)
                key_word[i] = _dict[item]
                # print(key_word)
                putdata = {
                    "doc": {
                        "zh_hans_keyword": key_word
                    }
                }
            putdata = json.dumps(putdata)
            print(putdata, _url)
            putRes = RequestHandler().post(url=_url, data=putdata, headers={
                "Content-Type": "application/json"})
            newputRes = res.json()
        except Exception:
            pass

       
        # print("更新结果",newputRes)
    else:
        print("没有key_word")


if __name__ == '__main__':
    url = "http://121.4.210.49:80/central_peoples_government/_search?from=0&size=100"
    data = {
        "query": {
            "match_all": {}
        }
    }
    res = RequestHandler().get(url, data=data)
    newRes = res.json()['hits']['hits']
    print(type(newRes))

    for item in newRes:
        gaiziduan(item['_source'], item['_id'])
