a = int.__add__(1, 2)
print(a)

b = str.__add__('a', 'b')

print(b)


class Savings:
    def __init__(self, amount):
        self.__amount = amount


s1 = Savings(10000)
s2 = Savings(2000)

#
#
# print(s1 + s2)
# Traceback (most recent call last):
#   File "/home/dhorovyi/percipio_training/...
#     a = s1 + s2
# TypeError: unsupported operand type(s) for +: 'Savings' and 'Savings'

print('\n########################################################\n')


class Savings:
    def __init__(self, amount):
        self.__amount = amount

    def __add__(self, other):
        return self.__amount + other.__amount


s1 = Savings(10000)
s2 = Savings(2000)

print(s1 + s2)
