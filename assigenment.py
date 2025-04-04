#single level

# class animal:
#     def __init__(self,name):
#         self.name=name
#     def __str__(self):
#         print(self.name)
#     def eat(self):
#         print(f"generic eats food")
# class Dog(animal):
#     def __init__(self, name):
#         super().__init__(name)
#         self.name=name
#     # def eat(self):
#     #     print(f"{self.name} eat meat")
# a=Dog("esu")
# print(a.name)
# a.eat()
# b=animal("generic animal")
# b.eat()

#multi level

class car:
    type=" generic car"
    no_of_wheels=4
    def start(self):
        print(f"generic  engine starts")
    def start(self,*args):
        print(f"hp{args} engin starts")
        
class audi(car):
    type="audi"
    def start(self):
        print(f"{self.type} engine starts ")
        
class kia(car):
    type="kia"
c=car()
a=audi()
k=kia()

a.start()
c.start()
k.start()
c.start(400)
print(k.no_of_wheels)

