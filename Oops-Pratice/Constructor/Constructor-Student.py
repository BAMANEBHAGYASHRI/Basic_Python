class Student:
    def marks(self,*p):
        i=0
        sum=0
        while(i<len(p)):
            sum=sum+p[i]
            i=i+1
        return sum


    def add(self):
        print("addition",sum)

obj1=Student()
marks=obj1.marks(90,78,99,95,45)
print("sumation",marks)