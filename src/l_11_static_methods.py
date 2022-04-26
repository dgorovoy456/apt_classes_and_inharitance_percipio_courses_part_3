class Rectangle:

    def area(x, y):
        return x * y


Rectangle.area = staticmethod(Rectangle.area)

print('area of the rectangle is: ', Rectangle.area(15, 16))


class Rectangle:

    @staticmethod
    def area(x, y):
        return x * y


print('area of the rectangle is: ', Rectangle.area(15, 16))