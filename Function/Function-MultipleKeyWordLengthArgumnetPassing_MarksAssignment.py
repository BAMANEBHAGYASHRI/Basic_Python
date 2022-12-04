def marks(**a):
    for i,j in a.items():
        
        sum=0
        for x in j:
            sum=sum+x
        pre=sum/5
        print(i,j,"\n","precentage",pre)


x=marks(bhagyashri=(90,78,67,99,65),afsana=(89,78,87,75,99),tejal=(90,75,36,54,22),kajal=(90,54,38,29,87))
    
