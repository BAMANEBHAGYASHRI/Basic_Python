class StudentData:
    def __init__(self):
        Class="B.TECH"
        self.rollno=102

    def Student1(self):
        print("Bhagyashri Vijay Bamane")
        print(self.rollno)

    def student2(self):
        print("Snehal Bhandare")
        print(self.rollno)

    def student3(self):
        print("Tejal Patil")
        

object=StudentData()
object.Student1()
# updating roll no
object.rollno=22
object.student2()