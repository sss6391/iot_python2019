with open("foo.txt",'w') as f:
    print('foo.txt 파일 오픈 성공')
    num = int(input('반복수'))
    for i in range(0,num):
        f.write('#%d life is too short, you need python\n' %i+1)
    print('작업종료')