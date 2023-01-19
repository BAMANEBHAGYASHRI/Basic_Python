class circle:
    def area(self,a):
        c=3.14*a*a
        return c

class sqaure:
    def area(self,a=10):
        return a*a

class Traingle:
    def area(self,a=4,b=8):
        return a*b

class tests:
    def test(self, x):
        z=x.area(4)
        return z

obj=tests()
obj1=circle()
s=obj.test(obj1)
print(s)


