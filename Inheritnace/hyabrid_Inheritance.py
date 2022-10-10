class Amplifier():
    def __init__(self):
        self.name="Amplifier Eletronics"
        self.domain="web devlpoment"
        self.designation="Embeddeed devlpoer"
    def details(self):
        print(self.name)
        print(self.domain)
        print(self.designation)

class ESC():
    def __init__(self):
        self.cname="ESC software"
        self.cdesignation="Applicaton devlpoment"
        self.cdomain="app devlopment"

    def detailsesc(self):
        print(self.cname)
        print(self.cdesignation)
        print(self.cdomain)

class serpenes(Amplifier,ESC):
    def __init__(self):
        self.sname="SREPENES-LIVE YOUR LIFE!""\u2764\ufe0f"
        self.sdomain="Full Satck Devlpoment"
        Amplifier.__init__(self)
        ESC.__init__(self)
        self.newdomainadded=self.domain,""+self.cdomain


    def macompany(self):
        print(self.sname)
        print(self.sdomain)
        print(self.newdomainadded)

object=serpenes()
object.macompany()




