import urllib.request
import datetime
import json
import time
from bs4 import BeautifulSoup
import re
from socket import *
import threading
import ctypes
import speech_recognition as sr

global g_mode
g_mode = False

port = 8080
server_ip = '192.168.0.5'
clientSock = socket(AF_INET, SOCK_STREAM)
clientSock.connect((server_ip, port))

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

def message():
    print("")
    if '비' or '소나기' in weather_list:
        print("오늘은 비가 올 것입니다. 우산을 챙기세요.")
        clientSock.send('12'.encode('utf-8'))
    elif '맑음' in weather_list:
        print('오늘은 하루종일 맑습니다.\n\t선크림을 바르세요.\n\t빨래를 하기 좋은 날입니다.')
        clientSock.send('11'.encode('utf-8'))

def check(temperature_list):
    global total
    for i in range(0, len(temperature_list)):
        total += int(temperature_list[i])

    total = total / len(temperature_list)
    print("\n***오늘의 패션 추천***")
    if total > 23:
        print("민소매티, 반바지, 반팔티, 원피스를 추천합니다.")
        clientSock.send('1'.encode('utf-8'))
    elif total in range(20,24):
        print("긴팔티,긴바지, 얇은 가디건을 추천합니다.")
        clientSock.send('2'.encode('utf-8'))
    elif total in range(16,21):
        print("맨투맨티, 얇은 가디건을 추천합니다.")
        clientSock.send('3'.encode('utf-8'))
    elif total in range(12,17):
        print("트렌치코트, 남방을 추천합니다.")
        clientSock.send('4'.encode('utf-8'))
    elif total in range(6,13):
        print("코트, 스웨터을 추천합니다.")
        clientSock.send('5'.encode('utf-8'))
    elif total < 6:
        print("패딩, 스웨터, 두꺼운 바지를 추천합니다.")
        clientSock.send('6'.encode('utf-8'))

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
        clientSock.send('15'.encode('utf-8'))
    elif '보통' in dust:
        print("미세먼지가 보통입니다. 외출시 마스크를 착용을 권장합니다")
        clientSock.send('16'.encode('utf-8'))
    else:
        print("미세먼지가 좋음입니다.")
        clientSock.send('14'.encode('utf-8'))

    yyyymmdd = time.strftime('%Y%m%d', time.localtime(time.time()))
    with open('%s_미세먼지예보_%s.json' % (city_name, yyyymmdd,), 'w', encoding='utf-8') as outfile:
        retJson = json.dumps(save_data, indent=4, sort_keys=True, ensure_ascii=False)
        outfile.write(retJson)
    # print('%s_미세먼지예보_%s.json' % (city_name, yyyymmdd))

g_AI_Mode = False
schedule_cycle = 2

def terminate_ai_mode():
    if not ai_scheduler.isAlive():
        return

    exc = ctypes.py_object(SystemExit)
    res = ctypes.pythonapi.PyThreadState_SetAsyncExc(
        ctypes.c_long(ai_scheduler.ident), exc)
    if res == 0:
        raise ValueError("nonexistent thread id")
    elif res > 1:
        ctypes.pythonapi.PyThreadState_SetAsyncExc(ai_scheduler.ident, None)
        raise SystemError("PyThreadState_SetAsyncExc failed")

def update_scheduler():
    while True:
        ti = time.strftime('%H%M', time.localtime(time.time()))
        se = time.strftime('%S', time.localtime(time.time()))

        if set_hour == int(ti[:2]) and set_minute == int(ti[2:]) and 0 == int(se):
            print("\n%s시 %s분 스케줄러 작동 완료" % (ti[:2], ti[2:]))
            # main()
            time.sleep(2)

def main():
    temperature()
    weatherforecast()
    rainfall()
    check(temperature_list)
    message()
    Make_dust_Json()

def print_main_menu():
    print("\n1. 스타일러 수동 작동")
    print("2. 음성인식 모드")
    print("3. Schedule_Mode")
    print("4. 수동 조작모드")
    print("0. 프로그램 종료")

def print_schedule_mode():
    if g_AI_Mode:
        print('Schedule_Mode 작동중입니다.')
    else: print('Schedule_Mode 꺼져있습니다')
    print("1. 모드변경")
    print("0. 이전 메뉴")

def mic():
    r = sr.Recognizer()
    mic = sr.Microphone()
    with mic as source:
        print("Speak into the microphone")
        audio = r.listen(source, timeout=2)

    try:
        print("Transcription: " + r.recognize_google(audio, language="ko-KO"))
    except sr.UnknownValueError:
        print("Audio unintelligible")
    except sr.RequestError as e:
        print("Cannot obtain results; {0}".format(e))

    voice = str(r.recognize_google(audio, language="ko-KO"))
    return voice
while True:
    print_main_menu()
    menu_num = int(input("메뉴를 선택하세요: "))

    if(menu_num == 1):
        main()
    elif (menu_num == 2):
        voice = mic()
        if voice == '입력모드':
            voice_1 = mic()
            while 1:
                if voice_1 == '온도':
                    temperature()
                elif voice_1 == '날씨':
                    weatherforecast()
                elif voice_1 == '강수':
                    rainfall()
                elif voice_1 == '추천':
                    check(temperature_list)
                elif voice_1 == '준비':
                    message()
                elif voice_1 == '미세먼지':
                    Make_dust_Json()
                else:
                    print("잘못 말씀하셨습니다.다시 말씀하세요.")
    elif (menu_num == 3):
        print_schedule_mode()
        mode_num = int(input("메뉴를 선택하세요: "))
        if mode_num == 1:
            g_AI_Mode = not g_AI_Mode
            if g_AI_Mode == True:
                print('스케줄러 작동 시간을 설정해주세요')
                set_hour = int(input('시(ex: 14): '))
                set_minute = int(input('분(ex: 53): '))
                ai_scheduler = threading.Thread(target=update_scheduler)
                ai_scheduler.daemon = True
                ai_scheduler.start()
                print("스케쥴러 작동 준비 완료!")
            else:
                while ai_scheduler.is_alive():
                    try:
                        terminate_ai_mode()
                    except: pass
                print("스케쥴러 정지 완료!")
    elif (menu_num == 4):
        while 1:
            sendData = input('(exit: 0)>>> ')
            if sendData == '0':
                break
            clientSock.send(sendData.encode('utf-8'))
    elif(menu_num == 0):
        clientSock.send('q'.encode('utf-8'))
        break
