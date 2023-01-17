class demo1:
    def method1(self):
        print("method 1 calling ")

    def method2(self):
        print("method 2 calling ")

    def method3(self):
        print("method 3 calling")
class demo2(demo1):
    def method4(self):
        print("method 4 calling ")

    def method5(self):
        print("method 5 calling ")

    def method6(self):
        print("method 6 calling")

obj=demo2()
obj.method5()
obj.method6()