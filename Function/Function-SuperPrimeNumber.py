def superprime():
    a=int(input("Enter Your value"))
    b=a//2
    state=0
    lst=[]
    flag=0
    for i in range(2,a):
        if(i%2==0):
            state=i
            
            break

    if(state==1):
        print("not prime",a)
    else:
        print("prime",a)
    lst.append(a)
    print(len(lst))
    
    '''for j in range(2,lst):
        if(j%2==0):
            flag=i
            break
    if(flag==1):
        print("not super prime")

    else:
        print("super prime")'''
            
    
    
    
        
        

superprime()
    
