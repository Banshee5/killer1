import time
def shahmaty_kek():
    t = time.monotonic()
    start = round(time(), 0)
    while time.monotonic() - t != 0:
        user_input = input('Enter: ')
        if user_input != 'off':
            check_time = round(time(), 0)
            left = (1800 - (check_time - start)) / 60
            print('Осталось:', round(left, 2), 'мин')
        else:
            break