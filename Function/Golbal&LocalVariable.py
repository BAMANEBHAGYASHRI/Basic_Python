def add():
    global c
    a=20
    b=30
    c=4
    print("Addition,InsideFunction",a+b+c)

def sub():
    a=3
    d=a-b
    print("SUbstraction",d)

a=15
b=5
e=a+b
add()
print(e)
print( "outside function ",c)
sub()
