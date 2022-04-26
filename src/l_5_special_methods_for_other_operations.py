a = 10 // 3
print(a)


class MethodFloordiv:
    def __init__(self, number):
        self.__number = number

    def __floordiv__(self, other):
        return self.__number // other.__number


s1 = MethodFloordiv(10)
s2 = MethodFloordiv(3)

print(s1 // s2)

print('\n###############################################################\n')

a = 4 % 2
print(a)

a = int.__mod__(4, 2)
print(a)


class MethodFloordiv:
    def __init__(self, number):
        self.__number = number

    def __mod__(self, other):
        return self.__number % other.__number


s1 = MethodFloordiv(10)
s2 = MethodFloordiv(3)

print(s1 % s2)

print('\n###############################################################\n')

a = 6 ** 2
print(a)

a = int.__pow__(6, 2)
print(a)


class MethodFloordiv:
    def __init__(self, number):
        self.__number = number

    def __pow__(self, other):
        return self.__number ** other.__number


s1 = MethodFloordiv(6)
s2 = MethodFloordiv(2)

print(s1 ** s2)

a = s1.__pow__(s2)
print(a)