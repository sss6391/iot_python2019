# coding: cp949
# ���̸� �Է� �޾� ���̿� ���� �뱸 IT���� ����Ḧ 
# ��� �ϴ� ���α׷��� �ۼ��Ͻÿ�.

age = 0
ident = 0
age1 = '����'
age2 = '���'
age3 = 'û�ҳ�'
age4 = '����'
age5 = '����'
charge = 0

age = int(input("���̸� �Է��ϼ���: "))
while age < 0:
    age = int(input("���� �Դϴ� �ٽ� �Է��ϼ���: "))

if age in range(4):
    charge = 0
    ident = age1
elif age in range(4,14):
    charge = 2000
    ident = age2
elif age in range(14,19):
    charge = 3000
    ident = age3
elif age in range(19,66):
    charge = 5000
    ident = age4
else:
    charge = 0
    ident = age5
print("���ϴ� %s ����̸� ����� %d�� �Դϴ�.\n" % (ident, charge))

pay_type = int(input("��� ������ �����ϼ���. (1: ����, 2: ��������ſ�ī��): "))

if pay_type == 2 and age >= 60 and age < 65:
    charge = charge * 0.85
    print("15���� ���� �Ǿ����ϴ� ����� %d�� �Դϴ�\n"%charge)
elif pay_type == 2:
    charge = charge * 0.9
    print("10���� ���� �Ǿ����ϴ� ����� %d�� �Դϴ�\n"%charge)

input_money = int(input("����� �Է��ϼ���: "))
if input_money == charge:
    print("�ݾ��� ��ġ�մϴ�. �����մϴ� Ƽ���� �����մϴ�.")
elif input_money > charge:
    print("�����մϴ�. Ƽ���� �����ϰ� �Ž����� %d�� ��ȯ�մϴ�." %(input_money-charge))
else: 
    print("%d�� ���ڶ��ϴ�. �Է��Ͻ� %d�� ��ȯ�մϴ�." % (input_money, input_money))