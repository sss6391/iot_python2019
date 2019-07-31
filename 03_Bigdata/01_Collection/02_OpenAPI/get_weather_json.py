import urllib.request
import datetime
import json
import time

access_key = 'arUGyHfSIvuuisVWulspIDqDRNaEEkPTXBKzLni5OzcFJoxrCbEaywqixKDH%2F3wmqB8wEFFKci7512Q7q%2BwyiA%3D%3D'
x_coodinate = "89"
y_coodinate = "91"

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

def get_Weather_URL(day_time):
    base_date = time.strftime('%Y%m%d', time.localtime(time.time()))
    end_point = "http://newsky2.kma.go.kr/service/SecndSrtpdFrcstInfoService2/ForecastTimeData"
    parameters = ("?base_date=%s&base_time=%s&nx=%s&ny=%s&_type=json&numOfRows=100&serviceKey=%s") \
                 %(base_date,day_time,x_coodinate,y_coodinate,access_key)

    url = end_point + parameters
    retData = get_Requrest_URL(url)
    if (retData == None):
        return None
    else:
        return json.loads(retData)

def Make_Weather_Json(day_time):
    jsonData = get_Weather_URL(day_time)
    json_weather_result = []
    for data in jsonData['response']['body']['items']['item']:
        json_weather_result.append(data)

    yyyymmdd = time.strftime('%Y%m%d', time.localtime(time.time()))
    with open('동구_신암동_초단기예보조회_%s%s.json' % (yyyymmdd, day_time), 'w', encoding='utf-8') as outfile:
        retJson = json.dumps(json_weather_result, indent=4, sort_keys=True, ensure_ascii=False)
        outfile.write(retJson)
    print('동구_신암동_초단기예보조회_%s%s.json' % (yyyymmdd, day_time))

def get_Realtime_Weather_Info():
    if time.localtime().tm_min in range(0,31):
        real_time = str(time.localtime().tm_hour - 1) + '59'
    else:
        real_time = time.strftime('%H%M', time.localtime(time.time()))
    # real_time = time.strftime('%H%M', time.localtime(time.time()))
    if len(real_time) == 3:
        real_time = '0' + real_time
    Make_Weather_Json(real_time)

get_Realtime_Weather_Info()
