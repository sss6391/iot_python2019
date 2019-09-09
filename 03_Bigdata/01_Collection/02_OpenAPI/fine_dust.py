import urllib.request
import datetime
import json
import time

json_dust_result = []
access_key =  'arUGyHfSIvuuisVWulspIDqDRNaEEkPTXBKzLni5OzcFJoxrCbEaywqixKDH%2F3wmqB8wEFFKci7512Q7q%2BwyiA%3D%3D'
# city_name = '%EB%8C%80%EA%B5%AC' # 대구
city_name = '대구'

def get_Requrest_URL(url):
    req = urllib.request.Request(url)

    try:
        response = urllib.request.urlopen(req)
        if response.getcode() == 200:
            print("[%s] Url:%s => Request Success" % (datetime.datetime.now(), url))
            return response.read().decode('utf-8')
    except Exception as e:
        print(e)
        print("[%s] Error for URL: %s" % (datetime.datetime.now(), url))
        return None

def get_dust_URL():
    # p18
    end_point = "http://openapi.airkorea.or.kr/openapi/services/rest/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty"
    parameters = "?sidoName=%s&pageNo=1&numOfRows=10&ServiceKey=%s&ver=1.3&_returnType=json" \
                 % (urllib.parse.quote(city_name), access_key)
    # url ='http://openapi.airkorea.or.kr/openapi/services/rest/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty?sidoName=%EC%8B%A0%EC%95%94%EB%8F%99&pageNo=1&numOfRows=10&ServiceKey=arUGyHfSIvuuisVWulspIDqDRNaEEkPTXBKzLni5OzcFJoxrCbEaywqixKDH%2F3wmqB8wEFFKci7512Q7q%2BwyiA%3D%3D&ver=1.3&_returnType=json'
    url = end_point + parameters
    retData = get_Requrest_URL(url)
    if (retData == None):
        return None
    else:
        return json.loads(retData)

def Make_dust_Json():
    jsonData = get_dust_URL()
    for data in jsonData['list']:
        json_dust_result.append(data)
    # json_dust_result.append(jsonData)

    yyyymmdd = time.strftime('%Y%m%d_%H%M', time.localtime(time.time()))
    with open('대구_실시간_미세먼지_%s.json' % (yyyymmdd), 'w', encoding='utf-8') as outfile:
        retJson = json.dumps(json_dust_result, indent=4, sort_keys=True, ensure_ascii=False)
        outfile.write(retJson)
    print('대구_실시간_미세먼지_%s.json' % (yyyymmdd))

Make_dust_Json()

