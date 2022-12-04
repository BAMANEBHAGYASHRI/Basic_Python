def Maximum_Number(*a):
    b=a[0]
    
    for i in range(1,len(a)):
        if(a[i]>b):
            b=a[1]
    print("maximun nuber is---",b)
            

Maximum_Number(90,78,65,9,43,15)
    
