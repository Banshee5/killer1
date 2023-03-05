def add_pineapple_and_salad(func_list):
    func_list.extend(['salad', 'pineapple'])
    print('Рецепт бутера:')
    n = 1
    for i in func_list:
        print(str(n) + '. ' + i)
        n += 1
print('')