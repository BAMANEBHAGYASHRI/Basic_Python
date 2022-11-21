lst=[45,90,78,56,99,34,67]
maxnum=lst[0]
for i in range(1,len(lst)):
    if(lst[i]>maxnum):
        maxnum=lst[i]
    

print("Maximum Number is--",maxnum)