lst=[[12,23,34,45,56],[65,67,87,98,90],[78,66,54,89,55],[43,89,63,25,33],[99,73,96,48,98]]
t=[]
p=[]
for i in range(len(lst)):
    s=0
    for j in range(len(lst[i])):
        s=s+lst[i][j]
    t.append(s)
    p.append(s/5)
print("sum of list----",t,"\n","precentage---",p)
