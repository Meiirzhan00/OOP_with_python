players = [('Carlsen',1990, 2842),('Caruana', 1992, 2822), ('Mamedyarov', 1985, 2801)]

print(players[0])

from collections import namedtuple

Player = namedtuple('Player','name age rating')

players = [Player('Carlsen',1990, 2842), Player('Caruana', 1992, 2822), Player('Mamedyarov', 1985, 2801)]

print(players[0].rating)

p1 = Player('Carlsen',1990, 2842)

print(p1.name)
print(p1.age)
print(p1.rating)
