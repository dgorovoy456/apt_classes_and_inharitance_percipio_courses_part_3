from abc import ABC, abstractmethod


class Hominidae():
    def diet(self):
        pass

    def walk(self):
        pass

    def behavior(self):
        print('They show complex facial expression and social behavior')


chimpanzee = Hominidae()

chimpanzee.behavior()

chimpanzee.walk()


class Human(Hominidae):
    def diet(self):
        print('Humans are omnivorous')

    def walk(self):
        print('They are bipeds.')


paul = Human()

paul.walk()
paul.behavior()
paul.diet()


class Hominidae(ABC):  # Abstract Base Class
    @abstractmethod
    def diet(self):
        pass

    def walk(self):
        pass

    def behavior(self):
        print('They show complex facial expression and social behavior')


# some = Hominidae()
#     some = Hominidae()
# TypeError: Can't instantiate abstract class Hominidae with abstract methods diet

class Human(Hominidae):

    def diet(self):
        print('Humans are omnivorous')

    def walk(self):
        print('They are bipeds.')


class Hominidae(ABC):  # Abstract Base Class
    @abstractmethod
    def diet(self):
        pass

    @abstractmethod
    def walk(self):
        pass


class Human(Hominidae):

    def diet(self):
        print('Humans are omnivorous')

    def walk(self):
        pass

