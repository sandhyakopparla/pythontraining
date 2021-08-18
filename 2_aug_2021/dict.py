#ordereddict
import collections
d1=collections.OrderedDict()
d1['name']="sandy"
d1['rollno']="22"
d1['admno']="1002"
for key,value in d1.items():
    print(key,value)