class Fourcal:
        # first = 0
        # second = 0 중간에 맴버 변수를 정의할 수 있어도 명싲거으로 클래스
                    # 맴버 변수를 class 다음에 지정하는 것은
                    # 프로그램 유지보수와 가독성에 더 좋다고 볼 수 있다.
    def setdata(self, first , second):
        self.first = first # 맴버변수가 없음에도 중간에 새로운 객체생성이후에
                            # 클래스의 맴버변수를 생성하는 것이 가능하다.
        self.second = second

    def print_number(self):
        print("first: %d, second: %d" % (self.first, self.second))

#a = Fourcal(1, 2) # 두개의 인자를 갖는 생성자가 없으므로 에러가 발생한다.
a = Fourcal()
a.setdata(3,2) # 객체 생성 이후의 맴버 변수 값을 설정할 때 사용한다.
a.print_number()
print(id(a.first))
print(id(a))

b = Fourcal()
b.setdata(3,2) # 객체 생성 이후의 맴버 변수 값을 설정할 때 사용한다.
b.print_number()
print(id(b.first))
print(id(b))
