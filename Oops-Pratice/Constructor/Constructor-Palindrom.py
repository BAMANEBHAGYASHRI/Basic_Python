class palindrom:
    def string(self,*s):
        return s == s[::-1]



obj1=palindrom()
c=obj1.string("madam")
print(c)

