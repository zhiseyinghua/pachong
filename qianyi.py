# coding=utf-8

import os
import sys
import pyes


index_list = [
    ["central_peoples_government", "central_peoples_government"],
    # ["human_resources_and_social_security", "human_resources_and_social_security"],
    # ["ministry_of_agriculture_and_rural_affairs",
    #     "ministry_of_agriculture_and_rural_affairs"],
    # ["national_development_and_reform_commission",
    #     "national_development_and_reform_commission"],
    # ["chinese_ministry_of_justice", "chinese_ministry_of_justice"],
    # ["urban_and_rural_construction", "urban_and_rural_construction"],
    # ["industrial_information", "industrial_information"],
    # ["bureau_of_education", "bureau_of_education"],
    # ["culture_and_tourism", "culture_and_tourism"],
    # ["ethnic_affairs_commission", "ethnic_affairs_commission"],
    # ["ecological_environment", "ecological_environment"],
    # ["science_and_technology", "science_and_technology"],
    # ["department_of_natural_resources", "department_of_natural_resources"],
    # ["chinese_ministry_of_finance", "chinese_ministry_of_finance"],
    # ["chinese_ministry_of_civil_affairs", "chinese_ministry_of_civil_affairs"],
]


ES_URL = "http://121.4.210.49:9200/"
NEW_ES_URL = "http://159.75.131.110:9200/"


def main():
    for _index, _type in index_list:
        conn = pyes.es.ES(ES_URL)
        search = pyes.query.MatchAllQuery().search(bulk_read=10000)
        hits = conn.search(search, _index, _type, scan=True, scroll="30m", model=lambda _,hit: hit)
         
        conn2 = pyes.es.ES(NEW_ES_URL)
        count = 0 
        for hit in hits:
            conn2.index(hit['_source'], _index, _type, hit['_id'], bulk=True)
            count += 1
            if count % 10000 == 0:
                # print count
                conn2.flush()
        conn2.flush()
        conn2 = None
 
        conn = None
 
 
if __name__ == '__main__':
    main()