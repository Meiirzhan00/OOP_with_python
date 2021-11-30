players = [('Carlsen',2842), ('Caruana',2822),('Giri', 2780)]

print(all(rating > 2800 for _, rating in players))
print(any(rating > 2800 for _, rating in players))

names = ['Meiirzhan', 'Abylaikhan', 'Nesipbay', 'Aidos']
ages = [21, 20, 20, 19]

persons = dict(zip(names, ages))
print(persons)

def square(*args):
    return [x*x for x in args]

print(square(1,2,3,4,5))

def square(number):
    return number*number

numbers = [1,2,3,4,5,6]
mapped = map(square, numbers)

print(list(mapped))

def is_adult(age):
    return age>=18

ages = [17,18,31,10,50]

l = list(map(is_adult,ages))
f = list(filter(is_adult,ages))

print(l)
print(f)
