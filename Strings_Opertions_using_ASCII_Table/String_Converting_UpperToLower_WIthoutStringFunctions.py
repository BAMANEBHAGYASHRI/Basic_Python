str=input("Enter Your String")
for i in str:
    if(ord(i)>=65 and ord(i)<=90):
        print(chr(ord(i)+32),end=" ")
    if(ord(i)>=97 and ord(i)<=122):
        print(chr(ord(i)-32),end=" ")