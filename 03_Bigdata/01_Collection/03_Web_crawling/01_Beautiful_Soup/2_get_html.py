import requests
from bs4 import BeautifulSoup

'http://www.weather.go.kr/weather/observation/currentweather.jsp'

reponse = requests.get("http://www.weather.go.kr/weather/observation/currentweather.jsp")
soup = BeautifulSoup(reponse.content, 'html.parser')

table = soup.find('table', {'class': 'table_develop3'})
data = []

def data_correction(org_text):
    if org_text == '\xa0':
        return 'N/A' # Not Applicable
    return org_text

for tr in table.find_all('tr'):
    tds = tr.find_all('td')
    if tds:
        point = data_correction(tds[0].a.text)
        cloud = data_correction(tds[1].text)
        visibility = data_correction(tds[2].text)
        temperature = data_correction(tds[5].text)
        wd_temp = data_correction(tds[7].text)
        data.append([point, cloud, visibility, temperature, wd_temp])


'''
for tr in table.find_all('tr'):
    table = list(tr.find_all('td'))
    # 각 날씨 값을 리스트로 만듦
    for td in tds:  # <td> 태그 리스트 반복(각 날씨 값을 가져옴)
        if td.find('a'):
            # <a> 태그 안에서 지점을 가져옴
            point = data_correction(td.find('a').text)
            cloud = data_correction(tds[1].text)
            # <td> 태그 리스트의 인덱스 1에서 날씨(하늘) 가져옴
            visibility = data_correction(tds[2].text)
            temperature = data_correction(tds[5].text)
            wd_temp = data_correction(tds[7].text)
            data.append([point, cloud, visibility, temperature, wd_temp])
'''



print(data)

