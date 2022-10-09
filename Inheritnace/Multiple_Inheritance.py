class Amplifier():
    def __init__(self):
        self.name="Amplifier Eletronics"
        self.domain="web devlpoment"
    def details(self):
        print(self.name)
        print(self.domain)

class ESC():
    def __init__(self):
        self.cname="ESC software"
        Amplifier.__init__(self)
        self.cdomain="app devlopment"
        self.addnewdomain=self.domain
    def detailsesc(self):
        print(self.cname)
        print(self.cdomain + self.addnewdomain)

class serpenes(Amplifier,ESC):
    def __init__(self):
        self.sname="Srepenes Software"
        self.sdomain="python devlpoment"
        Amplifier.__init__(self)
        ESC.__init__(self)

    def macompany(self):
        print(self.sname)
        print(self.sdomain)
        print("new adding coursee-",self.cdomain,""+self.addnewdomain)

object=serpenes()
object.macompany()




