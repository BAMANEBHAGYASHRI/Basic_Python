per=lambda a:"distincation" if(a>=75 and a<=100) else "first class" if(a>=65 and a<=75) else "second class" if(a>=50 and a<=65) else "pass" if(a>=35  and a<=50) else "fail" if(a>=20 and a<=35) else "-----------"
print(per(80))
print(per(24))
print(per(70))
print(per(56))