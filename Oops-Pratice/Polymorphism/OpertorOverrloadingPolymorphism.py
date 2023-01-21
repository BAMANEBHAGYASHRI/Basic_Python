class marks():
    def __init__(self,a,b):
        self.a=a
        self.b=b

    def __add__(self, other):
        x=self.a+other.a
        y=self.b+other.b
        z=marks(x,y)
        return z


m1=marks(50,97)
m2=marks(79,45)
m3=m1+m2
print(m3.a+m3.b)
