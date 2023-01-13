#constructor in a special method and which helps to  declared the attributes
class calulator():
    def __init__(self):
        self.a=10
        self.b=15
        print("-----------------------------------------------------------")
    def addition(self):
        c=self.a+self.b
        print("Addition",c)

    def substraction(self):
        c=self.a-self.b
        print("substrcation",c)


    def multiplication(self):
        c=self.a*self.b
        print("multiplication",c)


    def division(self):
        c=self.a/self.b


        print("division",c)


    def power(self):
        c=self.a**self.a
        print("power",c)

obj=calulator()
obj.multiplication()