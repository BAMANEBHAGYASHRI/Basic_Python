class Computer:
    def result(self):
        print("frist year-75.90%")
        print("second year-85.99%")
        print("third Year-95.34%")
        print("b.tech-99.95%")


class ENTC:
    def result(self):
        print("frist year-66.89%")
        print("second year-90.67%")
        print("third Year-56.90%")
        print("b.tech-99.95%")


class mechnical:
    def result(self):
        print("frist year-89.67%")
        print("second year-90.45%")
        print("third Year-56.90%")
        print("b.tech-99.00%")


class report:
    def  dep(self,o):
        o.result()



obj=Computer()
obj1=report()
obj1.dep(obj)
