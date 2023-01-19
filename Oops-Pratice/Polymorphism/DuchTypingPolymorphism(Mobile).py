class samsung():
    def config(self):
        print("samsung galaxy s22")
        print("ram 6GB")
        print("rom 128GB")

class apple():
    def config(self):
        print("Apple 14")
        print("ram 16GB")
        print("ROM 64 GB")

class mobiles():
    def data(self,a):
        a.config()



obj=mobiles()
obj1=apple()
obj.data(obj1)


