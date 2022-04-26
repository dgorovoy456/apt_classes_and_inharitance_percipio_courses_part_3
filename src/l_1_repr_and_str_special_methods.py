class Competition:
    def __init__(self, name, prize):
        self.__name = name
        self.__prize = prize


rowing = Competition('Rowing', 1000)
print(rowing)

print('\n############################################################\n')


class Competition:
    def __init__(self, name, prize):
        self.__name = name
        self.__prize = prize

    def __repr__(self):
        return f'{self.__name}, {self.__prize}'


rowing = Competition('Rowing', 1000)
print(rowing)

print(repr(rowing))

print(str(rowing))

print('\n############################################################\n')


class Competition:
    def __init__(self, name, country, prize):
        self.__name = name
        self.__country = country
        self.__prize = prize

    def get_name_country(self):
        return f'{self.__name}, {self.__country}'

    def __repr__(self):
        return f'Competition {self.__name} held {self.__country}, prize: {self.__prize}'

    def __str__(self):
        return f'{self.get_name_country()}, {self.__prize}'


archery = Competition('Archery', 'Ukraine', 10000)

print(archery)
print(repr(archery))
print(str(archery))
print(archery.__str__())
print(archery.__repr__())

print('\n############################################################\n')
