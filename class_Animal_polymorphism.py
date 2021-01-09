class Animal:
  def __init__(self,name):
    self.name=name

  def eat(self):
    print(f"{self.name} is eating.")

class Dog(Animal):
  def __init__(self,name,breed):
    super().__init__(name)
    self.breed=breed
    print(self.breed)

  def bark(self):
    print(f"Dog named {self.name} is barking.")

class Cat(Animal):
  def meaw(self):
    print(f"{self.name} says Meaw.")

class Frog(Animal):
  def eat(self):
    print(f"Frog with name {self.name} is eating.")

d=Dog('Arlan','Kazakhy')
c=Cat('Lusi')
f=Frog('Kwaly')

d.bark()
d.breed
d.eat()

c.eat()
c.meaw()
