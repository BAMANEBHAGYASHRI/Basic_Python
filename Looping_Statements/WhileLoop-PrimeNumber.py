num=int(input("Take value----"))
i=2
flag=0
while(i<num):
    if(num%2==0):
        flag=1
        break
    i=i+1
if(flag==0):
    print("Prime num")
else:
    print("not prime number")

