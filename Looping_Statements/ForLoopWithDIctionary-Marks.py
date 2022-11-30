m={"bhagyashri":[90,89,87,75,56],"shruti":[56,89,76,45,41],"kirti":[90,89,67,65,63],"Rakhi":[90,98,54,57,40]}
l1=[]
l2=[]
f=0
for i in m:
   # print(m[i])
   sum=0
   l1.append(i)
   for j in m[i]:
      if(j<35):
         f=1
      sum=sum+j
      # print(sum)
   per=sum/5
   # print(per)
   l2.append(per)
   if(f==1):
      print(i,"faill...",per)
      f=0
   elif(per>35 and per<50):
      print(i,"passs...",per)
   elif(per>=50 and per<60):
      print(i,"second class with ",per)
   elif(per>=60 and per<75):
      print(i,"1st class wth dist")
   elif(per>=75 and per<=100):
      print(i,"dist...",per)
   print("----------------------------------------------------------")
# print(l1,l2)
d=dict(zip(l1,l2))
print(d)
m=max(l2)
for s in d:
   if(m==d[s]):
      print("Tooper",s,"wth",d[s]);
   
