# coding: cp949

payment_type = "카드"
#payment_type = "현금"
#payment_type = ""

#if True: # 상수형 객체
        # 프로그램 개발 과정에서 뼈대(skeleton)를 만드는 과정에서
        # statement block을 test하는 value로 활용할 수 있다.

"""
Step 1] Skeleton 제작
if True:
    pass
else:
    pass
"""

'''
Step 2] 조건 설정
if payment_type:
    pass
else:
    pass
'''

'''
Step 3] 최정 로직, 알고리즘 삽입
if payment_type:
    print("{0}이 있는 것으로 확인되었습니다" .format(payment_type))
    print("택시를 타고 가세요")
else:
    print("걸어가세요")
'''

if payment_type:
    print("{0}이 있는 것으로 확인되었습니다" .format(payment_type))
    print("택시를 타고 가세요")
else:
    print("걸어가세요")
