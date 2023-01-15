class Primenumber:
    def prime(self,p):
        flag=0
        for i in range(2,p):
            if(i%2==0):
                flag=1
                break
        if(flag==1):
            print("not prime")
        else:
            print(" prime")

obj1=Primenumber()
obj1.prime(18)
