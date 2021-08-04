#ChainMap
import collections
dict1={"name":"ravi","age":22}
dict2={"name":"sanju","age":23}
comb_dict=collections.ChainMap(dict1,dict2)
print(comb_dict.maps) #maps is used for it will print dictionary into list
print(list(comb_dict.values())) #it is used to print values in the list