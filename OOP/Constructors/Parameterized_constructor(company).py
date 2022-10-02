class Company:
    def __init__(self,cname,Domain,founder):
        self.cname=cname
        self.Domain=Domain
        self.founder=founder

    def Companyinfo(self):
        print("company name- ",self.cname)
        print("company domain- ",self.Domain)
        print("company founder- ",self.founder)

object=Company("Amplifier Electronics PVT.LTD","Web Devlopment"+"Embeeded System And IOT","S.A.Shinde")
object.Companyinfo()


