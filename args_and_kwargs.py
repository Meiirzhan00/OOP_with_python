def calc_taxes(*args):
    for x in args:
        print(f'Got payment = {x}')
    return sum(args) * 0.06

print(calc_taxes(10,20,30))


def save_players(**kwargs):
    for k, v in kwargs.items():
        print(f'Player {k} has rating {v}')

save_players(Carlsen=2800, Giri = 2780)
