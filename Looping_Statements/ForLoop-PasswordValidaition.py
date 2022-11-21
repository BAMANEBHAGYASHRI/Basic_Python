User=input("Enter Your Username")
password=input("Enter Your Password")
i=0
f1=0
f2=0
f3=0
f4=0
for i in range(len(password)):
    if (len(password) >= 8):
        if(ord(password[i])>=65 and ord(password[i])<=90):
            f1=1
        if(ord(password[i])>=97 and ord(password[i])<=122):
            f2=1
        if(ord(password[i])>=48 and ord(password[i])<=57):
            f3=1
        if(ord(password[i])>=58 and ord(password[i])<=64):
            f4=1
    else:
         print("password is less than 8 charachters")
    i=i+1
if(f1==f2==f3==f4):
    print("Password is validate")
else:
    print("Invalid Password")








