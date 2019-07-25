import json

with open('아베_naver_news.json', encoding='utf-8') as json_file:
    json_data = json.load(json_file)
    # json_data_string = json.dumps(json_data)
    # jsonResult = json.loads(json_data_string)
    org_link_dic = {}
    count_none = 0
    count_vail = 0
    print("데이터 분석을 시작합니다.")
    for dics in json_data:
        try:
            link = dics['org_link'].split('/')[2]
            count_vail += 1
            if link not in org_link_dic.keys():
               org_link_dic[link] = 1
            else:
                org_link_dic[link] += 1
        except:
            print("'org_link'가 없는 기사를 발견했습니다.")
            count_none += 1

print("\n<네이버 검색 빅데이터 분석>\n검색어: 아베\n전체 도메인 수: %s" % len(org_link_dic.keys()))
print("유효한 데이터수: " , count_vail)
print("부정확한 데이터수: " , count_none)
print('\n- 도메인 별 뉴스 기사 분석')
org_link_dic_sorted = sorted(org_link_dic.items(), key=lambda x: x[1], reverse=True)
for list in org_link_dic_sorted:
    print(' >>',list[0],':',str(list[1])+'건')

