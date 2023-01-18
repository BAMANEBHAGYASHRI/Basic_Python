class company1:
    def __init__(self):
        self.aname="Alphabet inc."
        self.aCEO="Sunder pichai"
        self.aproduct="AI","automation"
        self.aheadquarters="US"
        self.aareaserved="worldwide"

    def alphabet(self):
        print(self.aname,self.aCEO,self.aproduct,self.aheadquarters,self.aareaserved)

class company2(company1):
    def __init__(self):
        self.gname = "Google"
        self.product = "workshop", "android", "youtube"
        self.headquarters = "US"
        self.areaserved = "worldwide"
        company1.__init__(self)


    def google(self):
        print(self.gname)
        print(self.aCEO)



obj=company2()
obj.google()