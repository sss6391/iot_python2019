from xml.etree.ElementTree import Element,dump, SubElement

note = Element('note')  # 노드 중 최상의 노드

to = Element('to')      # 자식 노드
to.text = 'Tove'        # 현재 엘리먼트(Tag)에 값 추가
note.append(to)         # 부모 노드에 자식노드 추가


SubElement(note,"from").text = "Jani"    # SubElement를 활용하여 자식노드 추가
dump(note)

dummy = Element("dummy")
note.insert(1,dummy)
dump(note)
note.remove(dummy)      # 부모노드에 있는 자식 노드를 인자로 넘겨줘야한다.
dump(note)
