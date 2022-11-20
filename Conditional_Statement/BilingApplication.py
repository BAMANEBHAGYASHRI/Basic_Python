s=0
while(s<500):
    a=int(input("Enter your amount"))
    b=input("do you want continue ")
    s=s+a
    print("sum of product",s)
    if(b=="no"):
        break
    if(s>100 and s<=500):
        d=s*0.05
        c=s-d
        print("discount",c)
    elif(s>=500 and s<=1000):
        d = s * 0.10
        c = s - d
        print("discount",c)
    elif(s>=1000 and s<=1500):
        d = s * 0.015
        c = s - d
        print("discount", c)
    elif(s>=1500 and s<=2000):
        d = s * 0.20
        c = s - d
        print("discount",c)
    elif(s>=2500 and s<=3000):
        d = s * 0.25
        c = s - d
        print("discount",c)
