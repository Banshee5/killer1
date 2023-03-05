class Genius:

    def __init__(self, name):
        self.name = name

    def write_genius(self):
        return f'{self.name} гений'


class ABC(Genius):

    def __init__(self, name):
        super().__init__(name)

    def make_object(self):
        one = Genius(self.name)
        return one

    def complete(self):
        print(f'{self.make_object().write_genius()}, но его отчислят если он не будет учить ООП')


def check():
    test = ABC('alex')
    test.complete()


check()