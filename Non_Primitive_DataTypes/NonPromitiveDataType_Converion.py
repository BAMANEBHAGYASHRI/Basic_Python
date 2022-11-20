# Tuple data type
a=("bhagyashri",12,900,56.45)
print(a,"\n",type(a))
b=list(a)
print("tuple convert into list----",b,"\n",type(b))
c=set(a)
print("tuple convert into set----",c,"\n",type(c))
# hint- tuple does'nt follw dictionary
d=dict(a)
print("tuple convert into dictionary----",d,"\n",type(d))
print("---------------------------------------------------------------------------------------------")
# list data type
e=["bhagyashri",12,900,56.45]
print(e,"\n",type(e))
f=tuple(e)
print("list convert into tuple----",f,"\n",type(f))
g=set(e)
print("list convert into set----",g,"\n",type(g))
# hint- tuple does'nt follw dictionary
h=dict(e)
print("list convert into dict----",h,"\n",type(h))
print("---------------------------------------------------------------------------------------------")
# set data type
i={"bhagyashri",12,900,56.45}
print(i,"\n",type(i))
j=tuple(i)
print("set convert into Tuple----",j,"\n",type(j))
k=list(i)
print("set convert into list----",k,"\n",type(k))
# hint- tuple does'nt follow dictionary
l=dict(i)
print("set convert into dict----",l,"\n",type(l))

