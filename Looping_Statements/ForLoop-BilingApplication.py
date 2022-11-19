sum=0
for i in range(300):
    x=int(input("Enter your amount"))
    y=input("do you want continue ")
    sum=sum+x
    print("sum of product",sum)
    if(y=="no"):
        break
    if(sum>100 and sum<=500):
        dis=sum*0.05
        total=sum-dis
        print("discount",total)
    elif(sum>=500 and sum<=1000):
        dis = sum * 0.10
        total = sum - dis
        print("discount",total)
    elif(sum>=1000 and sum<=1500):
        dis =sum* 0.015
        total = sum - dis
        print("discount", total)
    elif(sum>=1500 and sum<=2000):
        dis = sum * 0.20
        total = sum - dis
        print("discount",total)
    elif(sum>=2500 and sum<=3000):
        dis= sum * 0.25
        total = sum - dis
        print("discount",total)
    elif (sum >= 2500 and sum <= 3000):
        dis = sum * 0.30
        total = sum - dis
        print("discount", total)
print("-----Thank youuuu ! -------")
