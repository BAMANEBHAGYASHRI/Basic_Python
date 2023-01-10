a="hieeeeee i'm bhagyashri vijay bamane "
if(ord(a[0])>97 and ord(a[0])<=122):
    c=ord(chr(c),end=" ")

else:
    print(a[0],end=" ")

for j in range(len(a)):
    if(ord(a[j])==32):
        if(ord(a[j+1])>=97 and ord(a[j+1])<=122):
            c=(ord(a[j+1])-32)
            print(chr(c),end=" ")
            continue
        if((j+1)==len(a)):
            break
        print(a[j+1],end="")




