import random

# def randoms(min, max, n):
#     return [random.randint(min,max) for _ in range(n)]
#
# for i in randoms(10, 30, 5):
#     print(i)
#
# print('---------------------')

def randoms(min, max, n):
    for i in range(n):
        yield random.randint(min, max)

for i in randoms(10,30,5):
    print(i)


rand_sequence = randoms(1, 10 ,10)
print(rand_sequence)

for i in rand_sequence:
    print(i)

seq = list(randoms(1,10,5))
print(seq)

def randoms(min, max):
    while True:
        yield random.randint(min,max)
        
import itertools

rand_sequence = randoms(1,1000000)

five_taken = list(itertools.islice(rand_sequence,5))
print(five_taken)

rand_seq = randoms(1,10)
n = next(rand_seq)
print(n)
n = next(rand_seq)
print(n)
n = next(rand_seq)
print(n)

my_list = [1, 2, 3, 4]
squares = [x**2 for x in my_list]
print(squares)

squares = (x**2 for x in my_list) # generator
print(squares)
