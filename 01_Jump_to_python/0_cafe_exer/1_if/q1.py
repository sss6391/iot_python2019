# coding: cp949
# ���̸� �Է� �޾� ���̿� ���� �뱸 IT���� ����Ḧ 
# ��� �ϴ� ���α׷��� �ۼ��Ͻÿ�.

age = 0;

age = int(input("���̸� �Է��ϼ���: "))

print("����� ", end='')
if age in range(4,14):
    print('2000', end='')
elif age in range(14,19):
    print('3000', end='')
elif age in range(19,66):
    print('5000', end='')
else:
    print('0', end='')
print("�� �Դϴ�.")
