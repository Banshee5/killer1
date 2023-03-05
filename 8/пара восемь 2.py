def discount(score):
    if 0 < score < 50:
        _str = '10%'
        print('Your discount:' + _str)
    elif 50 <= score < 100:
        _str = '15%'
        print('Your discount:' + _str)
    elif score >= 100:
        _str = '20%'
        print('Your discount:' + _str)