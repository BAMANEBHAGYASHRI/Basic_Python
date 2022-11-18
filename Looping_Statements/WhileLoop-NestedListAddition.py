lst=[77,43,(2,56,90,78),[88,90,98,66],(23,33,32,22),[24,44,55,31],11,15]
print("Length of list---",len(lst))
i=0
sum=0
while(i<len(lst)):
    # print(lst[i])
    if(type(lst[i])==list or type(lst[i])==tuple):
        j=0
        while(j<len(lst[i])):
            sum=sum+lst[i][j]
            j=j+1
    else:
        sum=sum+lst[i]
    i = i + 1
print("Addition of Nested List elements---",sum)

