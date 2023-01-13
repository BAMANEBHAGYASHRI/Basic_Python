class mobile:
    def __init__(self):
        print("--------REDMI 7A MOBILE CONFIGURAION------------")
        self.model="REDMI 7A"
        self.displaytype="IPS LCD"
        self.ram="2/3GB"
        self.os="Andoid 9.0"

    def config(self):
        print("MODEL-",self.model)
        print("DISPLAY TYPE-",self.displaytype)
        print("RAM-",self.ram)
        print("OPERTING SYSTEM",self.os)


m1=mobile()
print("m1 object--Model Name",m1.model)
m2=mobile()
# print("m2 object--Model Name",m2.model)
m2.model=m2.model+"Pro"
print(m2.model)
