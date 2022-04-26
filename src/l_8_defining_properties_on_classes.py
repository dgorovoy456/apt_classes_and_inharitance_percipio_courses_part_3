class Wrestler:
    def __init__(self):
        self.__name = ''

    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name


w1 = Wrestler()
w1.set_name('Denys')
print(w1.get_name())

print('\n###################################################\n')


class Wrestler:
    def __init__(self):
        self.__name = ''

    def set_name(self, name):
        print('setter method called')
        self.__name = name

    def get_name(self):
        print('getter method called')
        return self.__name

    name = property(get_name, set_name)


w = Wrestler()

w.name = 'Anna'
print(w.name)

print('\n###################################################\n')


class Wrestler:
    def __init__(self):
        self.__name = ''

    def set_name(self, name):
        print('setter method called')
        self.__name = name

    def get_name(self):
        print('getter method called')
        return self.__name

    def del_name(self):
        print('deleter method called')
        del self.__name

    name = property(get_name, set_name, del_name)


w = Wrestler()

w.name = 'Anna'
print(w.name)

del w.name
