def bilingapplication():
    s=0
    for i in range(500):
        p=int(input("product value: "))
        q=input("do you want to cantinue? ")
        s=s+p
        if(q=="no"):
            break
    if(s>100 and s<=500):
        print("payable amount")
        d=s*0.05
        amount=s-d
        
    elif(s>500 and s<=1000):
        print("payable amount")
        d=s*0.10
        amount=s-d
        
    elif(s>1000 and s<=1500):
        print("payable amount")
        d=s*0.15
        amount=s-d
        
    elif(s>1500 and s<=2000):
        print("payable amount")
        d=s*0.20
        amount=s-d
    return amount
x=bilingapplication()
print(x)
