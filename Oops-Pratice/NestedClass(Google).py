class company1:
    def __init__(self):
        self.aname="Alphabet inc."
        self.aCEO="Sunder pichai"
        self.aproduct="AI","automation"
        self.aheadquarters="US"
        self.aareaserved="worldwide"

    def alphabet(self):
        print(self.aname,self.aCEO,self.aproduct,self.aheadquarters,self.aareaserved)

    class company2:
        def __init__(self):
            self.gname="Google"
            self.CEO="Sunder pichai"
            self.product="workshop","android","youtube"
            self.headquarters="US"
            self.areaserved="worldwide"

        def google(self):
            print(self.gname,self.CEO,self.product,self.areaserved,self.headquarters)


obj=company1()
obj2=obj.company2()
obj2.google()