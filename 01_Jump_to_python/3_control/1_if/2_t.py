# coding: cp949

payment_type = "ī��"
#payment_type = "����"
#payment_type = ""

#if True: # ����� ��ü
        # ���α׷� ���� �������� ����(skeleton)�� ����� ��������
        # statement block�� test�ϴ� value�� Ȱ���� �� �ִ�.

"""
Step 1] Skeleton ����
if True:
    pass
else:
    pass
"""

'''
Step 2] ���� ����
if payment_type:
    pass
else:
    pass
'''

'''
Step 3] ���� ����, �˰��� ����
if payment_type:
    print("{0}�� �ִ� ������ Ȯ�εǾ����ϴ�" .format(payment_type))
    print("�ýø� Ÿ�� ������")
else:
    print("�ɾ����")
'''

if payment_type:
    print("{0}�� �ִ� ������ Ȯ�εǾ����ϴ�" .format(payment_type))
    print("�ýø� Ÿ�� ������")
else:
    print("�ɾ����")
