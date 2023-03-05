def task_5(colour, number, **kwargs):
    print(f'{colour}: {number}')
    for kw in kwargs:
        print(f'{kw}: {kwargs[kw]}')