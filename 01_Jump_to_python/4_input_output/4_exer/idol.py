# coding: cp949
def show_candidates(candidate_list):
    print("���� ������ ����Ʈ")
    print(candidate_list)

def make_idol(candidate_list):
    print("�ſ� ���̵�", candidate_list,"�α� �޻��")

def make_world_star(candidate_list):
    print("���̵�", candidate_list, "���彺Ÿ ���")

file = open("������.txt", 'r', encoding='utf8')
candidates = file.read().splitlines()

show_candidates(candidates)
for idol in candidates:
    make_idol(idol)
for idol in candidates:
    make_world_star(idol)
file.close()