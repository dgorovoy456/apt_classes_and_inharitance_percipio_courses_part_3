some_list = [1, 2, 3, 4, 5, 6, 7]

for num in some_list:
    print(num)


class Participants:
    def __init__(self):
        self.__participants = []
        self.__index = 0

    def add_participants(self, name):
        self.__participants.append(name)

    def __len__(self):
        return len(self.__participants)

    def __iter__(self):
        self.__index = 0
        return self

    def __next__(self):
        if self.__index == len(self.__participants):
            raise StopIteration
        p = self.__participants[self.__index]

        self.__index += 1

        return p


participants = Participants()

participants.add_participants('Denys')
participants.add_participants('Anna')
participants.add_participants('Matvii')
participants.add_participants('Mia')

for p in participants:
    print(p)

participants.add_participants('cat')

for p in participants:
    print(p)

print(iter(participants))
print(next(participants))
print(next(participants))
print(next(participants))
print(next(participants))
print(next(participants))