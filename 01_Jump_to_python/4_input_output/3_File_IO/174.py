f = open('새파일.txt','r',encoding='UTF-8')

while True:
    line = f.readline()
    if not line: break
    print(line,end='')

f.close()