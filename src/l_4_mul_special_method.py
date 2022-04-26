a = 1.0 * 2.1
b = float.__mul__(1.0, 2.1)
# c = float.__mul__(1, 2.1)

print(a)
print(b)


# print(c)
#     c =  float.__mul__(1, 2.1)
# TypeError: descriptor '__mul__' requires a 'float' object but received a 'int'

class Savings:
    def __init__(self, amount):
        self.__amount = amount

    def __add__(self, other):
        return self.__amount + other.__amount

    def __mul__(self, other):
        if type(other) == int or type(other) == float:
            return self.__amount * other
        else:
            raise ValueError('Can only multiply by int or float')


s1 = Savings(1000)
s2 = Savings(200)

print(s1 + s2)
# print(s1 * s2)
#     raise ValueError('Can only multiply by int or float')
# ValueError: Can only multiply by int or float
print(s1 * 3)
print(s1.__mul__(3))
print(s2.__mul__(3))
print(s1.__mul__(3.1))

