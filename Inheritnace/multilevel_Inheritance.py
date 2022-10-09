class Amplifier():
    def __init__(self):
        self.name="Amplifier Eletronics"
        self.domain="web devlpoment"
        self.designation="Embeddeed devlpoer"
    def details(self):
        print(self.name)
        print(self.domain)
        print(self.designation)

class ESC(Amplifier):
    def __init__(self):
        self.cname="ESC software"
        self.cdesignation="Applicaton devlpoment"
        Amplifier.__init__(self)
        self.cdomain="app devlopment"
        self.addnewdomain=self.domain
        self.partner=self.name+self.designation

    def detailsesc(self):
        print(self.cname)
        print(self.cdomain + self.addnewdomain)
        print("new partner",self.partner)

class serpenes(ESC):
    def __init__(self):
        self.sname="SREPENES-LIVE YOUR LIFE!""\u2764\ufe0f"
        self.sdomain="Full Satck Devlpoment"
        ESC.__init__(self)
        self.partnership=self.partner

    def macompany(self):
        print(self.sname)
        print(self.sdomain)
        print("new adding coursee-",self.cdomain,""+self.addnewdomain)
        print(self.partner)
        print("new partner",self.partnership)

object=serpenes()
object.macompany()




