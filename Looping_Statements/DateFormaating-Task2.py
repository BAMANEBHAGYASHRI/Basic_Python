a="15/07/2004"
d=int(a[0:2])
m=a[3:5]
y=a[6:]
f1=0
f2=0
f3=0
if(str(m)=="01" or  str(m)=="03" or str(m)=="05" or str(m)=="07" or str(m)=="08" or str(m)=="10" or str(m)=="12"):
    f2=1
    if(d>0 and d<=31):
        f1=1
elif(str(m)=="04" or str(m)=="06" or str(m)=="09" or str(m)=="11"):
    f2=1
    if(d>0 and d<=30):
        f1=1
elif(str(m)=="02"):
    pass
if(len(y)==4):
    f3=1

if(f1==1 and f2==1 and f3==1):
    print("Valid Date !")
elif(f1==0):
    print("invalid")
elif(f2==0):
    print("invalid")
elif(f3==0):
    print("invalid")