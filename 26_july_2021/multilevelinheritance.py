class Parent:
    def eatfood(self,food):
        print(self.food)
class Father(Parent):
    def drinkcoffee(self,coffee):
        print(self.coffee)
class Child(Father):
    def eatchocolates(self,chocolates):
        print(self.chocolates)
objChild=Child()
objChild.eatchocolates("munch")
objChild.drinkcoffee("continental coffee")
objChild.eatfood("biryani")
