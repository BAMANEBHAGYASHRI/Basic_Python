lst=[77,43,(2,56,90,78),[88,90,98,66],(23,33,32,22),[24,44,55,31],11,15]
print("Length of list---",len(lst))
i=0
sum=0
for i in range(len(lst)):
    if(type(lst[i])==list or type(lst[i])==tuple):
        for j in range(len(lst[i])):
            # print(lst[i][j])
            sum=sum+lst[i][j]

    else:
        sum=sum+lst[i]

print("Addition of Nested List elements---",sum)
