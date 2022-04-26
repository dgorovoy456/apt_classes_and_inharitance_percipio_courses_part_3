class Wrestler:
    def __init__(self):
        self.__name = ''

    @property
    def name(self):
        print('getter method called')
        return self.__name

    @name.setter
    def name(self, value):
        print('setter method called')
        self.__name = value

    @name.deleter
    def name(self):
        print('deleter method called')
        del self.__name


w = Wrestler()
w.name = 'Anna'
print(w.name)
w.name = 'Denys'
print(w.name)

del w.name

print('\n##################################################\n')


class Wrestler:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    @property
    def name(self):
        print('name getter method called')
        return self.__name

    @name.setter
    def name(self, value):
        print('name setter method called')
        self.__name = value

    @name.deleter
    def name(self):
        print('name deleter method called')
        del self.__name

    @property
    def age(self, ):
        print('age method getter called')
        return self.__age

    @age.setter
    def age(self, value):
        print('age setter method called')
        self.__age = value

    @age.deleter
    def age(self):
        print('age deleter method called')
        del self.__age


w = Wrestler('Anna', 31)

w.name = 'Denys'
w.age = 30

print(w.name, w.age)

del w.name
del w.age
