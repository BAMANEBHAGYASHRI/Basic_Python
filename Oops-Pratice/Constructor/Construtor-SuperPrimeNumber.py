class SuperPrimeNumber:
    def prime(self, p):
        flag = 0
        for i in range(2, p):
            if (i % 2 == 0):
                flag = 1
                break
        if (flag == 1):
            return False,p
        else:
            return  True,p

    def superprime(xyz,abc):
        if(xyz==True):
            c=len(str(abc))
            if(c>2):
                s = 0
                for j in str(abc):
                    s = s + int(j)
                    t,u=superprime(s)



                # if (xyz == True):
                #     print(abc, "----super prime number")
                # else:
                #     print(abc, "---not super prime")




obj1 = SuperPrimeNumber()
xyz,abc=obj1.prime(18)
# print(xyz,abc)
obj1.superprime()




