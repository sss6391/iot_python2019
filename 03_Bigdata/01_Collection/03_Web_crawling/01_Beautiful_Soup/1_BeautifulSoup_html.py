from bs4 import BeautifulSoup

html='''
<td class="title">
    <div class="tit3">
        <a href="/movie/bi/mi/1. Basic Concept.nhn?code=158191" title="1987">한국 영화 1987
        </a>
    </div>
</td>
'''
soup = BeautifulSoup(html, 'html.parser')

print("<soup>")
print(soup)

# 해당 태그
print("\ntag=soup.td")
tag = soup.td
print(tag)

print("\ntag=soup.a")
tag = soup.a
print(tag)

# 태그이름 반환
print("\ntag.name")
print(tag.name)

# 태그 속성 반환 (딕셔너리)
print(tag.attrs)

# 태그 속성 딕셔너리의 값 반환
print(tag.attrs['title'])
print(tag.attrs['href'])

# 태그의 텍스트 출력
print(tag.text)

