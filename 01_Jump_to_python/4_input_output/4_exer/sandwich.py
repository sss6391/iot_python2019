def input_ingredient():
    ingredient_list = []
    while True:
        ingredient = str(input("안녕하세요. 원하시는 재료를 입력하세요(종료입력시 종료): "))
        if ingredient == "종료":
            return ingredient_list
        else:
            ingredient_list.append(ingredient)

def make_sandwiches(ingredient_list):
    print("\n샌드위치를 만들겠습니다.")
    for name in ingredient_list:
        print(name, "추가합니다.")
    print("여기 주문하신 샌드위치 만들었습니다. 맛있게 드세요.")

while True:
    print("안녕하세요. 저희 가게에 방문하여 주셔서 감사합니다\n1. 주문\n2. 종료")
    order = input("입력: ")
    if order == '2. 종료':
        break
    elif order == '1. 주문':
        make_sandwiches(input_ingredient())
        break
