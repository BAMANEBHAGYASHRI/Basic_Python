a=(input("enter your values"))
sum=0
s=0
for i in a:
    sum=sum+int(i)
print("sumation of all values",sum)
# print(len(sum))
# print(len(str(sum)))
b=str(sum)
# print(len(b))
if(len(b)>1):
    for j in b:
        s=s+int(j)
    print(s)
