a="amplifier eletronics pvt ltd"
for i in range(len(a)):
    if(i==0):
        if(ord(a[i])>=97 and ord(a[i])<=122):
            d=ord(a[i])-32
            print(chr(d),end=" ")
        if(ord(a[i])==32):
            b=i+1
            if(ord(a[b])>97 and ord(a[b])<=122):
                c=ord(a[b]-32)
                print(chr(c),end=" ")
            else:
                if(i<len(a)-1):
                    print(a[i+1],end=" ")
