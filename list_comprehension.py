greeting = 'Hello World'

chars = []

for i in greeting:
    chars.append(i)

print(chars)

chars = [i for i in greeting]
print(chars)

numbers = [l for l in range(11)]

print(numbers)

numbers = [n*n for n in range(11)]
print(numbers)

numbers = [n*n for n in range(11) if n%2!=0]
print(numbers)

len_int_centimeters = [12, 10, 54, 124, 64]
len_in_inches = [(round(cm / 2.54, 3)) for cm in len_int_centimeters]

print(len_in_inches)

rating = [2485, 2580, 2480, 2600, 2482, 2520]
titles = ['GM' if x>=2500 else 'MM' for x in rating]

print(titles)
