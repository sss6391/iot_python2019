# coding: cp949
input_age = 0
ident = 0
age = ['����', '���', 'û�ҳ�', '����', '����']
charge = 0
client = 0
free_ticket = [5, 3]
park_fare = [0, 2000, 3000, 5000]
while True:
    input_age = int(input("\n���̸� �Է��ϼ���: "))
    while input_age < 0:
        input_age = int(input("���� �Դϴ� �ٽ� �Է��ϼ���: "))
    if input_age in range(4):
        charge = park_fare[0]
        ident = age[0]
    elif input_age in range(4,14):
        charge = park_fare[1]
        ident = age[1]
    elif input_age in range(14,19):
        charge = park_fare[2]
        ident = age[2]
    elif input_age in range(19,66):
        charge = park_fare[3]
        ident = age[3]
    else:
        charge = park_fare[0]
        ident = age[4]
    if charge == 0:
        print("���ϴ� %s ����̸� ����� ���� �Դϴ�. Ƽ���� �����մϴ�." % ident)
        continue
    print("���ϴ� %s ����̸� ����� %d�� �Դϴ�.\n" % (ident, charge))
    pay_type = int(input("��� ������ �����ϼ���. (1: ����, 2: ��������ſ�ī��): "))
    if pay_type == 1:
        input_money = int(input("\n����� �Է��ϼ���: "))
        if input_money == charge:
            print("�ݾ��� ��ġ�մϴ�. �����մϴ� Ƽ���� �����մϴ�.")
            client = client + 1
        elif input_money > charge:
            print("�����մϴ�. Ƽ���� �����ϰ� �Ž����� %d���� ��ȯ�մϴ�." %(input_money-charge))
            client = client + 1
        else:
            print("%d���� ���ڶ��ϴ�. �Է��Ͻ� %d���� ��ȯ�մϴ�." % (((input_money-charge)*-1), input_money))
    elif pay_type == 2:
        client = client + 1
        charge = charge * 0.9
        if input_age >= 60 and input_age < 65:
            charge = charge * 0.95
        print("%d�� ���� �Ǿ����ϴ�. Ƽ���� �����մϴ�."%charge)
    if client > 0 and client % 7 == 0 and free_ticket[0] > 0:
        free_ticket[0] = free_ticket[0] - 1
        print("�����մϴ�. 1�ֳ� �̺�Ʈ�� ��÷�Ǿ����ϴ�. ���� ���� Ƽ���� �����մϴ�. �ܿ� ����Ƽ�� %d��" % free_ticket[0])
    if client > 0 and client % 4 == 0 and free_ticket[1] > 0:
        free_ticket[1] = free_ticket[1] - 1
        print("�����մϴ�. ����ȸ���� ���� �̺�Ʈ�� ��÷�Ǽ̽��ϴ�. ���� ȸ�� ���� Ƽ���� �����մϴ�. �ܿ� ����Ƽ�� %d��" % free_ticket[1])
