per =lambda a:"Dist" if(a>=75 and a<=100) else "first class" if(a>=65 and a<=75) else "second class" if(a>=35 and a<=65) else "fail" if(a>=20 and a<=35)
print(per(90))
