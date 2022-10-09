class Amplifier:
    def __init__(self):
        self.name="Amplifier Eletronics PVT.LTD"
        self.CEO="s.A.Shinde"
    def detailsAmplifiers(self):
        print("name",self.name)
        print("ceo",self.CEO)

class ECS(Amplifier):
    def __init__(self):
        self.cname="ESC Softwares PVT.LTD"
        # print(self.cname)
        Amplifier.__init__(self)
        self.ESC_CEO =self.CEO

    def detailsesc(self):
        print("name",self.cname)
        print("ceo",self.ESC_CEO)

object=ECS()
object.detailsesc()