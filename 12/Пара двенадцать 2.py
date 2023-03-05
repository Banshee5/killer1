def decorate(f):
    print('Данная функция выводит все числа между ' + str(f[0]) + ' и ' + str(f[1]))
    print(*f[2:])
def func(a, b):
    stack = [a, b]
    for i in range(a, b + 1):
        if i % 3 == 0:
            stack.append(i)
    return stack