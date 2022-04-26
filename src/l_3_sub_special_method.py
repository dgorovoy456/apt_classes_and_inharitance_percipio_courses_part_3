class MethodSub:
    def __init__(self, number):
        self.__number = number

    def __sub__(self, other):
        return self.__number - other.__number


num_1 = MethodSub(10)
num_2 = MethodSub(5)

print(num_1 - num_2)
print(num_2 - num_1)


class MethodSub:
    def __init__(self, number):
        self.__number = number

    def __sub__(self, other):
        return self.__number * other.__number


num_1 = MethodSub(10)
num_2 = MethodSub(5)

print(num_1 - num_2)
print(num_2 - num_1)

