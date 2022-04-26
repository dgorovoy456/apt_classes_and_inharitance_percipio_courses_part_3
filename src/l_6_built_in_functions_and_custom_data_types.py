a = len('test')
print(a)

a = str.__len__('test')
print(a)

some_list = [1, 2, 3, 4, 5, 6]

print(len(some_list))

a = list.__len__(some_list)
print(a)


class Participants:
    def __init__(self):
        self.__participants = []

    def add_participants(self, name):
        self.__participants.append(name)

    def __len__(self):
        return len(self.__participants)


s = Participants()
s.add_participants('Denys')
s.add_participants('Anna')

print(len(s))
print(s.__len__())

print('\n#####################################################\n')

print(list.__dict__)