import collections
list=[]
for i in range (1,10):
    names=input("enter the names:")
    list.append(names)
print(list)
x=collections.Counter(list)
print(x)



