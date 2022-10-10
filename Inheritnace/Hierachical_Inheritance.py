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

    def detailsesc(self):
        print(self.cname)
        print(self.cdomain + self.addnewdomain)

class serpenes(Amplifier):
    def __init__(self):
        self.sname="SREPENES-LIVE YOUR LIFE!""\u2764\ufe0f"
        self.sdomain="Full Satck Devlpoment"
        Amplifier.__init__(self)
        self.newdomain=self.domain
    def macompany(self):
        print(self.sname)
        print(self.sdomain)
        print(self.newdomain)


object=serpenes()
object.macompany()




