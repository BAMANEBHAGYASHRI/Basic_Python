class Amplifier():
    def __init__(self):
        self.name="Amplifier Eletronics"
        self.domain="web devlpoment"
    def details(self):
        print(self.name)
        print(self.domain)

class ESC(Amplifier):
    def __init__(self):
        self.cname="ESC software"
        Amplifier.__init__(self)
        self.cdomain="app devlopment"
        self.addnewdomain=self.domain
    def detailsesc(self):
        print(self.cname)
        print("adding new course",self.cdomain + self.addnewdomain)

obj=ESC()
obj.detailsesc()



