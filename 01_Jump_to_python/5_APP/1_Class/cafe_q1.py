class Restaurant:
    def __init__(self, name, type):
        self.restauran_name = name
        self.cuisine_type = type

    def describe_restaurant(self):
        print("저희레스토랑 명칭은 %s 이고 %s 전문점입니다" % (self.restauran_name, self.cuisine_type))

    def open_restaurant(self):
        print("저희 %s 레스토랑 오픈했습니다. 어서오세요" %self.restauran_name)

name, type = input("레스토랑 이름과 요리 종류를 선택하세요.(공백으로 구분) : ").split()

restaurant = Restaurant(name, type)
restaurant.describe_restaurant()
restaurant.open_restaurant()
