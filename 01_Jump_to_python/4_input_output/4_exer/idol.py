# coding: cp949
def show_candidates(candidate_list):
    print("현재 연습생 리스트")
    print(candidate_list)

def make_idol(candidate_list):
    print("신예 아이돌", candidate_list,"인기 급상승")

def make_world_star(candidate_list):
    print("아이돌", candidate_list, "월드스타 등극")

file = open("연습생.txt", 'r', encoding='utf8')
candidates = file.read().splitlines()

show_candidates(candidates)
for idol in candidates:
    make_idol(idol)
for idol in candidates:
    make_world_star(idol)
file.close()