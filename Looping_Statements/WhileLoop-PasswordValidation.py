User=input("Enter Your Username")
pwd=input("Enter Your Password")
i=0
flag1=0
flag2=0
flag3=0
flag4=0
while(i<len(pwd)):
    if(len(pwd)>=8):
        if(ord(pwd[i])>=65 and ord(pwd[i])<=90):
            flag1=1
        if(ord(pwd[i])>=97 and ord(pwd[i])<=122):
            flag2=1
        if(ord(pwd[i])>=48 and ord(pwd[i])<=57):
            flag3=1
        if(ord(pwd[i])>=58 and ord(pwd[i])<=64):
            flag4=1
    else:
         print("password is less than 8 charachters")
    i=i+1
if(flag1==flag2==flag3==flag4):
    print("Password is validate")
else:
    print("Invalid Password")






