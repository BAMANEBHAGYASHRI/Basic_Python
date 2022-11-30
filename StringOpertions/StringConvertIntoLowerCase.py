a="HELLO,I'M BHAGYASHRI VIJAY BAMANE !"
for i in a:
    x=ord(i)
    # print(x)
    if(i==" "):
        print(" ",end=" ")
    elif(x>=65 and x<=90):
        c=x+32
        print(chr(c),end=" ")