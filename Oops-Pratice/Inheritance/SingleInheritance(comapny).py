class company:
    def __init__(self):
        self.name="Amplifier Elteronics pvt.ltd"
        self.country="india"
        self.cost="10,00,000"
        self.founder="S.A.Shinde"
        self.domain="embedded system and IOT"

    def c_details(self):
        print("company details","\n",self.name,"\n",self.country,"\n",self.cost,"\n",self.founder,"\n",self.domain)

class companyFounder(company):
    def __init__(self):
        self.cfname = "S.A.Shinde"
        company.__init__(self)
        self.citizen = "indian"
        self.age = "40"
        self.state = "tamilnadu"
        self.qualification = "E&TC engineer"


    def fonder_detials(self):
        print(self.cfname)
        print(self.name)


obj=companyFounder()
obj.fonder_detials()