class Fourcal:
    def __init__(self, first, second):
        self.first = first
        self.second = second

    def setdata(self, first , second):
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

a = Fourcal(4,2)
b = Fourcal(3,8)
print(a.add())
print(a.mul())
print(a.sub())
print(a.div())

print(b.add())
print(b.mul())
print(b.sub())
print(b.div())

a.setdata(9, 4) # setxxx 관련 함수가 있기 때문에 원하는 연산을 초기화하여 다시
                # 수행 할 수 있다.
b.setdata(382, 48)
