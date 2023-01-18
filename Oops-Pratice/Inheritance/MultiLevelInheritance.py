class demo1:
    def method11(self):
        print("method 1 calling")

    def method12(self):
        print("method 2 calling")

class demo2(demo1):
    def method21(self):
        print("method 1 calling")

    def method22(self):
        print("method 2 calling")

class demo3(demo2):
    def method31(self):
        print("method 1 calling")

    def method32(self):
        print("method 2 calling")


obj1=demo3()
obj1.method11()


