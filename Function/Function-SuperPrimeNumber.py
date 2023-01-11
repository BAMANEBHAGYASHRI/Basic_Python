def superprime(a):
    b=a//2
    state=0
    for i in range(2,a):
        if(i%2==0):
            state=i
            break
    if(state==1):
        return False,a
    else:
       return True,a

x,y=superprime(31)
#print(x)
if(x==True):
    z=len(str(y))
    if(z>=2):
        s=0
        for j in str(y):
            s=s+int(j)
        p,q=superprime(s)

        if(x==True):
            print(y,"----super prime number")
        else:
            print(y,"---not super prime")


    
