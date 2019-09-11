import urllib.request
import datetime
import json
import csv

json_dust_result = []
access_key =  'arUGyHfSIvuuisVWulspIDqDRNaEEkPTXBKzLni5OzcFJoxrCbEaywqixKDH%2F3wmqB8wEFFKci7512Q7q%2BwyiA%3D%3D'
city_name = '대구'
header_list = ['stationName', 'coValue', ]

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
    end_point = "http://openapi.airkorea.or.kr/openapi/services/rest/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty"
    parameters = "?sidoName=%s&pageNo=1&numOfRows=10&ServiceKey=%s&ver=1.3&_returnType=json" \
                 % (urllib.parse.quote(city_name), access_key)
    url = end_point + parameters
    retData = get_Requrest_URL(url)
    if (retData == None):
        return None
    else:
        return json.loads(retData)

def Make_dust_csv():
    jsonData = get_dust_URL()
    for data in jsonData['list']:
        json_dust_result.append(data)

    keys = json_dust_result[0].keys()
    data_time = json_dust_result[0]['dataTime']
    data_time = data_time[:10]+'_'+data_time[11:13]+data_time[14:]
    with open('대구_실시간_미세먼지_%s.csv' % (data_time), 'w', newline='') as outfile:
        filewriter = csv.writer(outfile)
        filewriter.writerow(keys)
        for index in range(len(json_dust_result)):
            value_list = []
            for key in keys:
                value_list.append(json_dust_result[index][key])
            filewriter.writerow(value_list)
Make_dust_csv()
