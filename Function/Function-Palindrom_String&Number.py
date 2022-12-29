def stringPalindrom(*x):
    return x==x[::-1]

    
x=stringPalindrom("aabbaa")
if(x):
    print("yes")
else:
    print("no")
