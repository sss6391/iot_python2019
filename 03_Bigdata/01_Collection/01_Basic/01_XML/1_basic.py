from xml.etree.ElementTree import Element,dump

# <>    노드
# <노드명 속성 = '값'>
# <노드A>     값1    </노드A>
# <노드A 속성1="값1">

# <to>Tove</to>     ==>    <to name="Tove/>


note = Element('note')  # 노드 중 최상의 노드

to = Element('to')      # 자식 노드
to.text = 'Tove'        # 현재 엘리먼트(Tag)에 값 추가
note.append(to)         # 부모 노드에 자식노드 추가

dump(note)
dump(to)