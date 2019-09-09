import urllib.request
import datetime
import json
import time
from bs4 import BeautifulSoup
import re

access_key = 'arUGyHfSIvuuisVWulspIDqDRNaEEkPTXBKzLni5OzcFJoxrCbEaywqixKDH%2F3wmqB8wEFFKci7512Q7q%2BwyiA%3D%3D'
city_name = '대구'

html = urllib.request.urlopen('http://web.kma.go.kr/aboutkma/intro/daegu/index.jsp')
soup = BeautifulSoup(html, 'html.parser')

tags = soup.find_all('tr')
rain_list = []
temperature_list = []
weather_list = []
total = 0

def weatherforecast():
    title=re.compile('PD_none" title="(\w+)"')
    for tag in tags:
        try:
            if tag.th.string == '날씨':
                for td in tag:
                    t = title.search(str(td))
                    try:
                        if td.attrs['class'][0] in "bg_tomorrow":         break
                    except: pass
                    if t:
                       weather_list.append(t.group(1))
                break
        except: pass
    # print("날씨")
    # print(weather_list)

def rainfall():
    title=re.compile('<td class="">(\d+)</td>')
    for tag in tags:
        try:
            if tag.th.string == '강수확률(%)':
                for td in tag:
                    t = title.search(str(td))
                    try:
                        if td.attrs['class'][0] == "bg_tomorrow":         break
                    except: pass
                    if t:
                       rain_list.append(t.group(1))
                break
        except: pass
    # print("강수확률(%s)")
    # print(rain_list)

def temperature():
    title = re.compile('<p class="plus">(\d+)</p></td>')
    for tag in tags:
        try:
            if tag.th.string == '기온(℃)':
                for td in tag:
                    t = title.search(str(td))
                    try:
                        if td.attrs['class'][0] == "bg_tomorrow": break
                    except: pass
                    if t:
                        temperature_list.append(t.group(1))
                break
        except: pass
    # print("기온( C)")
    # print(temperature_list)

def message():
    print("")
    if '비' or '소나기' in weather_list:
        print("오늘은 비가 올 것입니다. 우산을 챙기세요.")
    elif '맑음' in weather_list:
        print('오늘은 하루종일 맑습니다.\n\t선크림을 바르세요.\n\t빨래를 하기 좋은 날입니다.')

def check(temperature_list):
    global total
    for i in range(0, len(temperature_list)):
        total += int(temperature_list[i])

    total = total / len(temperature_list)
    print("\n***오늘의 패션 추천***")
    if total > 23:
        print("민소매티, 반바지, 반팔티, 원피스를 추천합니다.")
    elif 20 < total < 23:
        print("긴팔티,긴바지, 얇은 가디건을 추천합니다.")
    elif 16 < total < 20:
        print("맨투맨티, 얇은 가디건을 추천합니다.")
    elif 12 < total < 16:
        print("트렌치코트, 남방을 추천합니다.")
    elif 6 < total < 12:
        print("코트, 스웨터을 추천합니다.")
    elif total < 6:
        print("패딩, 스웨터, 두꺼운 바지를 추천합니다.")

def get_Requrest_URL(url):
    req = urllib.request.Request(url)

    try:
        response = urllib.request.urlopen(req)
        if response.getcode() == 200:
            # print("[%s] Url:%s => Request Success" % (datetime.datetime.now(), url))
            return response.read().decode('utf-8')
    except Exception as e:
        print(e)
        print("[%s] Error for URL: %s" % (datetime.datetime.now(), url))
        return None

def get_dust_URL(pm):
    yyy = time.strftime('%Y-%m-%d', time.localtime(time.time()))
    # p22
    end_point = "http://openapi.airkorea.or.kr/openapi/services/rest/ArpltnInforInqireSvc/getMinuDustFrcstDspth"
    parameters = "?searchDate=%s&ServiceKey=%s&_returnType=json&InformCode=PM%s" % (yyy, access_key, pm)
    url = end_point + parameters
    retData = get_Requrest_URL(url)
    if (retData == None):
        return None
    else:
        return json.loads(retData)

def Make_dust_Json():
    dust = []
    save_data = []
    jsonData = get_dust_URL(10)
    p = re.compile('%s : (\w+),' % city_name)
    m = p.search(str(jsonData))
    dust.append(m.group(1))
    save_data.append(jsonData)

    jsonData = get_dust_URL(10)
    p = re.compile('%s : (\w+),' % city_name)
    m = p.search(str(jsonData))
    save_data.append(jsonData)

    dust.append(m.group(1))
    print("오늘의 미세먼지 PM10: " + dust[0] + " PM2.5: " + dust[1])
    if '나쁨' in dust:
        print("미세먼지가 많습니다. 외출시 마스크를 착용하세요!!")
    elif '보통' in dust:
        print("미세먼지가 보통입니다. 외출시 마스크를 착용을 권장합니다")

    yyyymmdd = time.strftime('%Y%m%d', time.localtime(time.time()))
    with open('%s_미세먼지예보_%s.json' % (city_name, yyyymmdd,), 'w', encoding='utf-8') as outfile:
        retJson = json.dumps(save_data, indent=4, sort_keys=True, ensure_ascii=False)
        outfile.write(retJson)
    # print('%s_미세먼지예보_%s.json' % (city_name, yyyymmdd))

def main():
    temperature()
    weatherforecast()
    rainfall()
    check(temperature_list)
    message()
    Make_dust_Json()

def print_main_menu():
    print("\n1. 스타일러 작동")
    print("2. 프로그램 종료")

while True:
    print_main_menu()
    menu_num = int(input("메뉴를 선택하세요: "))

    if(menu_num == 1):
        main()
    elif(menu_num ==2):
        break
