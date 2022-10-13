class newmobile():
    def mobiles(self):
        self.nmane="REDMI 7A"
        print(self.nmane)

class oldmobile():
    def mobiles(self):
        self.mobname="oppa 7"
        print(self.mobname)

class mob():
    def getmobile(self,o):
        o.mobiles()
        


object=newmobile()
obj=mob()
obj.getmobile(object)
