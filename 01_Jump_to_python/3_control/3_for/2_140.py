# coding: cp949

marks = [90, 25, 67, 45, 80]
number = 0
for mark in marks:
    number = number +1
    if mark < 60: continue
    else:
        print("%d�� �л� �����մϴ�. �հ��Դϴ�." % number)
