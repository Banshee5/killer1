def task3():
    team1 = 0
    team2 = 0
    while True:
        user = input('Press enter')
        if user != 'off':
            number = randint(1, 2)
            print('Your number is:', number)
            if number == 1:
                team1 += 1
            else:
                team2 += 1
            print('Участников в первом забеге:', team1)
            print('Участников во втором забеге:', team2)
        else:
            break