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



class founder(company2,company1):
    def __init__(self):
        self.fname="sundar pichai"
        company1.__init__(self)
        company2.__init__(self)

    def founderdeatils(self):
        print(self.fname)
        print(self.aname)
        print(self.gname)



obj1=company2()
obj1.google()
obj=founder()
obj.founderdeatils()