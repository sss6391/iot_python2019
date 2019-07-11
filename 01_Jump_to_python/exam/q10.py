class Calculator:
    def __init__(self, number_list):
        self.list = number_list
        self.total = 0
        self.mean = 0
        self.len = len(number_list)
    def sum(self):
        for number in self.list:
            self.total += number
        return self.total
    def avg(self):
        return self.total / self.len

cal1 = Calculator([1,2,3,4,5])
print(cal1.sum())
print(cal1.avg())

cal2 = Calculator([6,7,8,9,10])
print(cal2.sum())
print(cal2.avg())
