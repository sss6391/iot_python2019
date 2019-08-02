import urllib.request
from bs4 import BeautifulSoup
import re

html = urllib.request.urlopen('http://movie.naver.com/movie/sdb/rank/rmovie.nhn')
soup = BeautifulSoup(html,'html.parser')

trs = soup.tbody.find_all('tr')
movies_ranks = []
index = 1
for tr in trs:
    up_down = re.findall(r'alt="(\w+)"', str(tr))
    title = re.findall(r'title=".+">(.+)</a>', str(tr))
    fl_num = re.findall(r'<td class="range ac">(\d?)<', str(tr))
    if title:
        if up_down[1] == 'up':          up_down = '+'
        elif up_down[1] == 'down':      up_down = '-'
        else:                           up_down = ''
        movies_ranks.append([str(index), title[0], up_down+fl_num[0]])
        index = index +1
print(movies_ranks)

f = open('output_r.csv', 'w', encoding='utf-8')
f.write('순위 |    영화명     |변동폭\n')
for m in movies_ranks:
    f.write(m[0].center(5))
    f.write('|')
    f.write(m[1].center(15))
    f.write(m[2].center(5))
    f.write('\n')
f.close()
