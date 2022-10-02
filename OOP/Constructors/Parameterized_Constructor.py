class student:
    def __init__(self,name,age,branch,rno):
        self.name=name
        self.age=age
        self.branch=branch
        self.rno=rno

    def studentdata(self):
        print("Student name",self.name)
        print("student age",self.age)
        print("student branch",self.branch)
        print("student roll no",self.rno)

object=student( "bhagyashri",18,"CSE",103)
object.studentdata()



