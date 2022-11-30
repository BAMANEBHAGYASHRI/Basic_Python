a=input("Enter Your String")
s=" "
for i in a:
    if (ord(i) >= 32 and ord(i) <= 47):
        s=s+i
    elif (ord(i) >= 48 and ord(i) <= 57):
        print(i)
    elif (ord(i) >= 58 and ord(i) <= 64):
        print(i)
    elif(ord(i)>=65 and ord(i)<=90):
        print(i)
    elif (ord(i) >= 91 and ord(i) <= 96):
        print(i)
    elif (ord(i) >= 97 and ord(i) <= 122):
        pass
print(s)













