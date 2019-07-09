class Fourcal:
    def setdata(self, first , second):
        self.first = first
        self.second = second

    def add(self):
        result = self.first + self.second
        return result

    def print_number(self):
        print("first: %d, second: %d" % (self.first, self.second))

a = Fourcal()
a.setdata(3,2)
a.print_number()
print(a.add())

b = Fourcal()
b.setdata(1,2)
b.print_number()
print(b.add())

print(a.first + a.second)
# 위와같이 python의 모든 클래스의 맴버 변수. 함수는 속성이 public이라
# 외부에서 모두 접근이 가능하다.
# 하지만 클래스의 맴버 변수에 대해서 설정하는 것은
# 클래스 정의 시 맴버변수 정의, 생성자, setxxx() 함수로 정의 및 수정을 하는 것이
# 객체지향 프로그래밍에 가깝다.
temp  = [1,2,3,4]
temp.__class__
# 객체지향언어에서의 private 개념은 __맴버변수__.__맴버함수__() 로
# 적용할 수 있다. 접근은 가능하지만 사용하지 않는 암묵적인 룰을 준수한다.