class Company:
    def __init__(self):
        self.cname="Amplifier Electronics PVT.LTD"
        self.Domain="Web Devlopment"+"Embeeded System And IOT"
        self.founder="S.A.Shinde"

    def Companyinfo(self):
        print("company name",self.cname)
        print("company domain",self.Domain)
        print("company founder",self.founder)

object=Company()
object.Companyinfo()
print(object.founder)




