class collage:
    def __init__(self):
        self.cname="ADARSH INSTITUDE OF TECHONOLOGY AND RESERACH CNTER"
        self.location="VITA,SANGLI"
        self.Director="pooja patil"
        self.chirman="vaibhav patil"
        self.branches="5"
        self.univercity="DBATU univercity"
        self.insitudecode="1228"

    def collagedetils(self):
        print(self.cname,self.location,self.Director,self.chirman,self.branches,self.univercity,self.insitudecode)

    class student:
        def __init__(self):
            self.sname="BHAGYASHRI VIJAY BAMANE"
            self.sclass="CES-SY"
            self.dep="CSE"
            self.rollname="CS2069"
            self.univercity="DBATU univercity"

        def studentdetails(self):
            print(self.sname,self.sclass,self.dep,self.rollname,self.univercity)


obj=collage()
obj1=obj.student()
obj1.studentdetails()