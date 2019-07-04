# coding: cp949

print("\n**********구구단 출력 프로그램**********\n")

for i in range(2,10):
    print("=====%s단 출력=====" % i)
    for j in range(1,10):
        print("%s * %s = %s" % (i, j, (i*j)))
    print('')
