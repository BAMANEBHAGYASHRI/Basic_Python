
class calulator():
    def __init__(self,a,b):
        self.a = a
        self.b =b

    def addition(self):
        c = self.a + self.b
        print("Addition", c)

    def substraction(self):
        c = self.a - self.b
        print("substrcation", c)

    def multiplication(self):
        c = self.a * self.b
        print("multiplication", c)

    def division(self):
        c = self.a / self.b

        print("division", c)

    def power(self):
        c = self.a ** self.a
        print("power", c)


obj = calulator(12,4)
obj.multiplication()