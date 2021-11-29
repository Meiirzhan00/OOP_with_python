class Animal:
    def set_health(self, health):
        print('set in animal')

class Carnivour(Animal):
    def set_health(self, health):
        print('set in carnivour')

class Mammal(Animal):
    def set_health(self, health):
        print('set in mammal')

class Dog(Carnivour, Mammal):
    pass
#
# dog = Dog()
# dog.set_health(10)

class Animal:
    def set_health(self, health):
        print('set in animal')

class Carnivour(Animal):
    def set_health(self, health):
        print('set in carnivour')

class Mammal(Animal):
    def set_health(self, health):
        print('set in mammal')

class Dog(Carnivour, Mammal):
    def set_health(self, health):
        Mammal.set_health(self, health)
        Carnivour.set_health(self,health)
        Animal.set_health(self,health)

        print('set in dog')

# dog = Dog()
# dog.set_health(20)

class Animal:
    def set_health(self, health):
        print('set in animal')

class Carnivour(Animal):
    def set_health(self, health):
        Animal.set_health(self, health)
        print('set in carnivour')

class Mammal(Animal):
    def set_health(self, health):
        Animal.set_health(self, health)
        print('set in mammal')

class Dog(Carnivour, Mammal):
    def set_health(self, health):
        Mammal.set_health(self, health)
        Carnivour.set_health(self,health)

        print('set in dog')

# dog = Dog()
# dog.set_health(20)

class Animal:
    def set_health(self, health):
        print('set in animal')

class Carnivour(Animal):
    def set_health(self, health):
        super().set_health(health)
        print('set in carnivour')

class Mammal(Animal):
    def set_health(self, health):
        super().set_health(health)
        print('set in mammal')

class Dog(Carnivour, Mammal):
    def set_health(self, health):
        super().set_health(health)

        print('set in dog')

dog = Dog()
dog.set_health(20)


class Animal:
    def __init__(self):
        self.health = 100

    def hit(self, damage):
        self.health -= damage

class Carnivour(Animal):
    def __init__(self):
        super().__init__()
        self.legs = 4

c = Carnivour()
c.hit(10)

print(c.health)
