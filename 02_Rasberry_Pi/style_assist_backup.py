import urllib.request
import datetime
import json
import time
import re

access_key = 'arUGyHfSIvuuisVWulspIDqDRNaEEkPTXBKzLni5OzcFJoxrCbEaywqixKDH%2F3wmqB8wEFFKci7512Q7q%2BwyiA%3D%3D'
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
    yyy = time.strftime('%Y-%m-%d', time.localtime(time.time()))
    # p22
    end_point = "http://openapi.airkorea.or.kr/openapi/services/rest/ArpltnInforInqireSvc/getMinuDustFrcstDspth"
    parameters = "?searchDate=%s&ServiceKey=%s&_returnType=json" % (yyy, access_key)
    url = end_point + parameters
    retData = get_Requrest_URL(url)
    if (retData == None):
        return None
    else:
        return json.loads(retData)

def Make_dust_Json():
    jsonData = get_dust_URL()
    p = re.compile('%s : (\w+),' % city_name)
    m = p.search(str(jsonData))
    dust = m.group(1)
    print(dust)

    yyyymmdd = time.strftime('%Y%m%d', time.localtime(time.time()))
    with open('%s_미세먼지예보_%s.json' % (city_name, yyyymmdd), 'w', encoding='utf-8') as outfile:
        retJson = json.dumps(jsonData, indent=4, sort_keys=True, ensure_ascii=False)
        outfile.write(retJson)
    print('%s_미세먼지예보_%s.json' % (city_name, yyyymmdd))

Make_dust_Json()






