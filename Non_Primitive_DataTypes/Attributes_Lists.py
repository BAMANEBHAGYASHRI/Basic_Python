lst=[1,"shruti",90.87,67,54]
lst1=[12,34,56,87,32,546,2342,89]
print(lst)
#append
lst.append(15)
lst.append("Bhagyashri")
print("Appending Elements---",lst)
print("----------------------------")
#index
b=lst.index("shruti")
c=lst.index(54)
print("Indexing of list---",b)
print("Indexing of list---",c)
print("----------------------------")
#Extend
lst.extend([0,1,2,3,4,5,6,7,8,9,10])
print("Extending of List---",lst)
print("----------------------------")
#pop[hint-give the index value]
d=lst.pop(2)
print("poping the List---",d)
print("----------------------------")
#remove[hint-give the elements]
lst.remove(54)
print("Removing the elements---",lst)
print("----------------------------")
#reversee
lst.reverse()
print("reversing the list---",lst)
print("----------------------------")
lst1.sort()
print("sorting the list ---",lst1)
