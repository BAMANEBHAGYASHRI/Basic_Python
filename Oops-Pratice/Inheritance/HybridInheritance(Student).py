class collage:
    def __init__(self):
        self.cname = "ADARSH INSTITUDE OF TECHONOLOGY AND RESERACH CNTER"
        self.location = "VITA,SANGLI"
        self.Director = "pooja patil"
        self.chirman = "vaibhav patil"
        self.branches = "5"
        self.univercity = "DBATU univercity"
        self.insitudecode = "1228"

    def collagedetils(self):
        print(self.cname, self.location, self.Director, self.chirman, self.branches, self.univercity, self.insitudecode)


class student(collage):
    def __init__(self):
        self.sname = "BHAGYASHRI VIJAY BAMANE"
        self.sclass = "CES-SY"
        self.dep = "CSE"
        self.rollname = "CS2069"
        collage.__init__(self)

    def studentdetails(self):
        print(self.sname)
        print(self.cname+self.location)


class examform(student, collage):
    def __init__(self):
        student.__init__(self)
        collage.__init__(self)

    def examdetails(self):
        print(self.univercity + self.insitudecode)


obj = examform()
obj.examdetails()
obj1=student()
obj1.studentdetails()