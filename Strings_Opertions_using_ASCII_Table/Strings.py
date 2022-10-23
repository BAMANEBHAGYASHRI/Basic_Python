str=input("Enter Your String")
for i in str:
    if(ord(i)>=20 and ord(i)<=63):
        print(ord(i) + 32, end=" ")

    if(ord(i)>=63 and ord(i)<=95):
        print(ord(i) + 32, end=" ")

    if(ord(i)>=95 and ord(i)<=126):
        print(ord(i) + 32, end=" ")