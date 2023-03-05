from random import randint
def task():
    team1 = int(input('Число участников сборной 1:'))
    team2 = int(input('Число участников сборной 2:'))
    print(randint(1, team1), '-', randint(1, team2))
