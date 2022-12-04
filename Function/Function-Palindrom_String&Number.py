def stringPalindrom(*x):
    s=x[::-1]
    return s
    
x=stringPalindrom("aabbaa")
if(x):
    print("yes")
else:
    print("no")
