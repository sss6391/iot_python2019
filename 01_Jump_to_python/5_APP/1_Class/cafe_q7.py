class Restaurant:
    def __init__(self, name, type):
        try:
            r_name = name + '_고객서빙현황로그.txt'
            file = open(r_name, 'r')
            file_number = file.read()
            self.todays_customer = int(file_number)
            file.close()
        except:
            self.todays_customer = 0
        finally:
            self.restauran_name = name
            self.cuisine_type = type
            self.number_served = 0

    def describe_restaurant(self):
        print("\n저희레스토랑 명칭은 %s 이고 %s 전문점입니다" % (self.restauran_name, self.cuisine_type))

    def open_restaurant(self):
        print("저희 %s 레스토랑 오픈했습니다. 어서오세요" %self.restauran_name)

    def reset_number_served(self):
        check = int(input("초기화 옵션 (전체: 1, 당일: 2): "))
        if check == 1:
            print("전체 손님 카운딩을 0으로 초기화 하였습니다")
            self.todays_customer = 0
        elif check == 2:
            print('당일손님 카운팅을 0으로 초기화 하였습니다.')
            self.todays_customer += self.number_served
            self.number_served = 0

    def increment_number_served(self, number):
        print('손님 %s명 들어오셨습니다. 자리를 안내해 드리겠습니다.' % number)
        self.number_served += number

    def check_customer_number(self):
        check = int(input("누적 고객확인 (전체: 1, 당일: 2): "))
        if check == 1:
            print("전체 손님 총 %d명 손님께서 오셨습니다." % self.todays_customer)
        elif check == 2:
            print('당일 손님 %d명 손님께서 오셨습니다.' % self.number_served)

    def __del__(self):
        print(self.restauran_name,"레스토랑 문 닫습니다")
        self.todays_customer += self.number_served
        num = str(self.todays_customer)
        try:
            r_name = self.restauran_name+'_고객서빙현황로그.txt'
            file = open(r_name, 'w')
            file.write(num)
            file.close()
        except:
            pass

class Restaurant_child1:
    def __init__(self):
        self.partyroom = 0
        self.soloroom = 0
    def solo(self, number):
        print('혼자오셨으므로 개인석으로 안내해드리겠습니다')
        self.number_served += number
        self.soloroom = self.partyroom + 1

    def party(self, number):
        print('단체 %s명 들어오셨습니다. 룸으로 안내해 드리겠습니다.' % number)
        self.number_served += number
        self.partyroom = self.partyroom + 1

class Restaurant_child2:
    # def __init__(self):
    #      pass

    def open_restaurant(self,):
        print("저희 레스토랑은 10시 오픈합니다 현재시간은", "입니다")
        print("저희 %s 레스토랑 오픈했습니다. 어서오세요" % cafe.restauran_name)


name, type = input("레스토랑 이름과 요리 종류를 선택하세요.(공백으로 구분) : ").split()
cafe = Restaurant(name, type)
cafe2 = Restaurant_child2()
cafe.describe_restaurant()
open_close = input("레스토랑을 오픈하시겠습니까? (y/n): ")
if open_close == 'y':
    if True :   cafe2.open_restaurant()
    else:       cafe.open_restaurant()
    while True:
        input_number = input('\n어서오세요. 몇명이십니까?(초기화:0입력,종료:-1,누적고객 확인:p) : ')
        if input_number == '-1':
            del cafe
            break
        elif input_number == '0':
            cafe.reset_number_served()
        elif input_number == 'p':
            cafe.check_customer_number()
        else:
            cafe.increment_number_served(int(input_number))
