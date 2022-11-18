lst=[[12,23,34,45,56],[65,67,87,98,90],[78,66,54,89,55],[43,89,63,25,33],[99,73,96,48,98]]
# print(lst)
i=0
total=[]
per=[]
while(i<len(lst)):
    # print(lst[3][0])
    j=0
    sum=0
    while(j<len(lst[i])):
        sum=sum+lst[i][j]
        j=j+1
    total.append(sum)
    per.append(sum/5)
    i=i+1
print("sum of list----",total,"\n","precentage---",per)
