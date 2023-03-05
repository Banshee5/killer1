class Account:

    def __init__(self, name, balance, passport, password):
        self._name = name
        self.__balance = balance
        self.__passport = passport
        self.__password = password

    def get_balance(self):
        return self.__balance

    def set_balance(self, new_balance):
        self.__balance = new_balance

    def get_password(self):
        return self.__password

    def get_passport(self):
        return self.__passport

    def set_passport(self, new_passport, password):
        if password == self.get_password():
            self.__passport = new_passport
            print('успешно изменен')
        else:
            print('Не тот пароль')

    def del_passport(self, password):
        if password == self.get_password():
            del self.__passport
            print('паспорт удален')
        else:
            print('Не тот пароль')

    def change_balance(self, new):
        if self.__balance + new >= 0:
            self.__balance += new
            print(f'balance: {self.get_balance()}')
        else:
            print('Balance < 0 !!!')