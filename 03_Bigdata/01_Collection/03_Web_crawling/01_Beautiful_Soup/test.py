import urllib.request
from bs4 import BeautifulSoup


html = urllib.request.urlopen('http://movie.naver.com/movie/sdb/rank/rmovie.nhn')
soup = BeautifulSoup(html,'html.parser')
# print(soup)
# print(soup.prettify()) # 원본 HTML의 indentation에 맞게 변경

movies_ranks = []


trs = soup.find('td', attrs={'class':"ac"}).img.attrs['alt']


print(trs)

