class Person:

    def krya_krya(self):
        print('крякаю')

    def wear_clothes(self):
        print('штаны мое все')


class Duck:

    def krya_krya(self):
        print('КРЯ!!!')

    def wear_clothes(self):
        print('Я тип утка КРЯЯЯЯЯЯ!')


def main():
    my_list = [Person(), Duck()]
    for i in my_list:
        i.krya_krya()
        i.wear_clothes()


main()