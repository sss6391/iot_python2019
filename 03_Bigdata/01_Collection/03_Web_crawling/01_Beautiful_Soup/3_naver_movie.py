import urllib.request
from bs4 import BeautifulSoup

html = urllib.request.urlopen('http://movie.naver.com/movie/sdb/rank/rmovie.nhn')
soup = BeautifulSoup(html,'html.parser')

movies_ranks = []
trs = soup.tbody.find_all('tr')
index = 1
for tr in trs:
    if tr.find('div', attrs={'class':"tit3"}):
        title = tr.a['title']
        up_down = tr.find_all('img')[1].attrs['alt']
        fluctuation_num = tr.find('td', attrs={'class':"range ac"}).text
        if up_down == 'up':         up_down = '+'
        elif up_down == 'down':     up_down = '-'
        else:                       up_down = ''
        movies_ranks.append([str(index), title, up_down+fluctuation_num])
        index = index+1

print(movies_ranks)
f = open('output.csv', 'w', encoding='utf-8')
f.write('순위 |    영화명     |변동폭\n')
for m in movies_ranks:
    f.write(m[0].center(5))
    f.write('|')
    f.write(m[1].center(15))
    f.write(m[2].center(5))
    f.write('\n')
f.close()

# 과제
# 네이버 영화 랭킹 웹페이지를 분석하여 아래 형식으로 csv 파일을 생성하시오
# 순위 |      영화명       | 변동폭
#  1   |       1987        |   0
#  2   |  신과함께-죄와 벌 |  +1
#  3   |쥬만지: 새로운세계 |  -1.

# 또는 아래와 같이 영화 정보 행을 리스트로 만들어서 복잡 리스트로 작성하여 화면에출력한다.
# [[1,'1987','N/A'],[2,'신과함께-죄와 벌','+1'],[3,'쥬만지: 새로운세계','-1']]