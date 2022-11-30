lst=[[12,23,34,45,56],[65,67,87,98,90],[78,66,54,89,55],[43,89,63,25,33],[99,73,96,48,98]]
t=[]
for test in lst:
    # print("lenght of lst",len(i))
    sum=0
    for test1 in test:
        sum=sum+test1
    t.append(sum)
print(t)

