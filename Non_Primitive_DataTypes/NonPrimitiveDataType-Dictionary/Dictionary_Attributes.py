a={1:"Bhagyashri",2:"Shruti",3:"Snehal",4:"asmita",5:"Masira"}
print(a)
print("print all dict keys(variables)---",a.keys())
print("Print all dictonary values---",a.values())

print("--------------------------------------------------------------------------------------")
b={"name":"Bhagyashri","class":"B.TECH -SY","rollno":1286,"DOB":"15/july/2004"}
print(b)
print("---------------------------------------------------------------------------------------------")

# Bulti-in function-Zip()
x=zip(a,b)
print(x)
y=dict(x)
print(x,"\n",y)
print("----------------------------")
print(dict(zip(a,b)))
print("----------------------------")
print(type(zip(a,b)))
print(type(dict(zip(a,b))))