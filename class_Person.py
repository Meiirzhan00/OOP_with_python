class Person:
  def __init__(self, name, age):
    self.name=name
    self.age=age
    print('Person created')

  def say_hello(self):
    print(f"{self.name} says hello !")

class Student(Person):
  def __init__(self,name,age,average_grade):
    # Person.__init__(self,name,age)
    super().__init__(name,age)
    self.average_grade=average_grade
    print("Student created !")

  def study(self):
    print(f"{self.name} studied !")

  def say_hello(self):
    super().say_hello()
    print(f"Student with name : {self.name} says hello !")

class Teacher(Person):
  def teach(self):
    print(f"{self.name} teaches !")


# s1=Student('Bob',26,6.2)
# t1=Teacher('Asya',40)

# s1.say_hello()
# t1.say_hello()

# s1.study()
# t1.teach()

def introduce(person):
  print('Now, a person will say hello.')
  person.say_hello()

people_arr=[Student('Bob',24,4.5),Teacher('Kate',27),Student('Tom',31,6.4)]

for person in people_arr:
  introduce(person)
