a="helloo , i'm bhagyashri bamane !"
print(a)
for i in a:
    x=ord(i)
    # print(x)
    if(i==" "):
        print(" ",end="")
    elif(x>=97 and x<=122):
        c=x-32
        print(chr(c),end="")