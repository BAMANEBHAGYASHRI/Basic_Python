num=int(input("Take value----"))
i=2
flag=0
if(num==1 or num<0):
    flag=2
while(i<num):
    if(num%i==0):
        flag=1
        break
    i=i+1
if(flag==0):
    print("prime num")
elif(flag==2):
        print("natural num")
else:
    print("not prime number")
