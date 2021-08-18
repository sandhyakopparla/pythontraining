import collections 
employees=collections.namedtuple('employees',["name","empId","salary"])
e1=employees("sandy","10001","23000")
print(e1.name)