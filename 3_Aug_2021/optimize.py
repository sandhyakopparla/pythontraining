import timeit
# print(timeit.timeit(stmt="a=10;b=5;c=a+b"))


# print(timeit.timeit(stmt="z=1+3"))


# mycode='''a=10+5'''
# print(timeit.timeit(stmt=mycode))


# mycode='''
# a=10
# if(a<15):
#     pass'''
# print(timeit.timeit(stmt=mycode))


# def printnumbers():
#     for n in range(1000):
#         pass
# print(timeit.timeit(printnumbers,number=10000))


# def printwhile():
#     n=0
#     while(n<=1000):
#         n=n+1
#         pass
# print(timeit.timeit(printwhile,number=10000))

mylist=[10,12,23,45,44,43,33,22,14]
def f1():
    filter(43,mylist)
def f2():
    for i in mylist:
        if(i==43):
            pass
print(timeit.timeit(f1,number=100000))
print(timeit.timeit(f2,number=100000))






