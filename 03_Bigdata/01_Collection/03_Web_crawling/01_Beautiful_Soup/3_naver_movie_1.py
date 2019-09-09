import urllib.request
from bs4 import BeautifulSoup

html = urllib.request.urlopen('http://movie.naver.com/movie/sdb/rank/rmovie.nhn')
soup = BeautifulSoup(html,'html.parser')

index = 1
f = open('output_1.csv', 'w', encoding='utf-8')
for tr in soup.tbody.find_all('tr'):
    if tr.find('div', attrs={'class':"tit3"}):
        # try:
            print([str(index), tr.a['title'],  tr.find('img', attrs=({"class":"arrow"})).attrs['alt']+tr.find('td', attrs={'class':"range ac"}).string])
            f.write('{0}, {1}, {2}, {3}\n'.format(str(index), tr.a['title'], tr.find('img', attrs=({"width":"7"})).attrs['alt'],tr.find('td', attrs={'class':"range ac"}).string))
            index = index + 1
        # except: pass
f.close()