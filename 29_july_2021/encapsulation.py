class iphone:
    def __init__(self):
        self.__price=2000
        self.x=500
    def sellingprice(self):
        print(self.__price)
        print("x=.",self.x)
    def offerprice(self,discount):
        self.__price=self.__price-discount
obj=iphone()
obj.sellingprice()
obj.__price=500
obj.sellingprice()
obj.offerprice(500)
obj.sellingprice()
obj.x=1000
obj.sellingprice()



