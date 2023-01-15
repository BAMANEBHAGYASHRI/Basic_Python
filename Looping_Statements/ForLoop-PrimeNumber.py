a=int(input("Enter The value"))
b=a//2
flag=0
for i in range(2,a):
    if(i%2==0):
        flag=1
        break
if(flag==1):
    print("not prime number")
else:
    print("Prime number")
