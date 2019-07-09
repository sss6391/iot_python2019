class Fourcal:
    def __init__(self, first, second):
        self.first = first
        self.second = second

    def setdata(self, first, second):
        self.first = first
        self.second = second

    def add(self):
        result = self.first + self.second
        return result

    def mul(self):
        result = self.first * self.second
        return result

    def sub(self):
        result = self.first - self.second
        return result

    def div(self):
        result = self.first / self.second
        return result

    def print_number(self):
        print("first: %d, second: %d" % (self.first, self.second))

class MoreFourcal(Fourcal):
    def pow(self):
        result = self.first ** self.second
        return result
    def div(self):  # 매서드 오버라이딩: 자식클래스에서 맴버함수를 재정의
        if self.second == 0:
            return 0
        else:
            result = self.first / self.second
            return result

a = Fourcal(4,2)

child = MoreFourcal(2,3)
child.print_number()
print(child.pow())

child.setdata(3,0)
print(child.div())
