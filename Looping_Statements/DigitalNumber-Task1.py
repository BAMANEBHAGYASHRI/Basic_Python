num=(input("enter your value"))
sum=0
s1=0
s2=0
for i in num:
    sum=sum+int(i)
print(sum)
s=str(sum)
if(len(s)>1):
    for j in s:
        s1=s1+int(j)
    print(s1)
s=str(s1)
if(len(s)>1):
    for p in s:
        s2=s2+int(p)
    print(s2)

