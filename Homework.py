# Возьмите 1-3 задачи из тех, что были на прошлых
# семинарах или в домашних заданиях. Напишите к ним
# классы исключения с выводом подробной информации.
# Поднимайте исключения внутри основного кода. Например,
# нельзя создавать прямоугольник со сторонами отрицательной длины.
class NegativeValueError(Exception):
    def __init__(self, value: int | float):
        self.value = value

    def __str__(self):
        return f"This parameter can't be negative: {self.value}"


class SubtractionError(Exception):
    def __str__(self):
        return f"Can't subtract greater from lesser. The result will be negative."


class Rectangle:
    """Rectangle class containing length & width, computing perimeter & area."""
    def __init__(self, length: int | float, width: int | float = None):
        self.length = length
        if not width:
            width = length
        if length < 0:
            raise NegativeValueError(length)
        elif width < 0:
            raise NegativeValueError(width)
        self.width = width

    def perimeter(self) -> int | float:
        """Return perimeter of the rectangle"""
        return 2 * self.length + 2 * self.width

    def area(self) -> int | float:
        """Return area of the rectangle"""
        return self.length * self.width

    def __add__(self, other):
        perimeter = self.perimeter() + other.perimeter()
        return Rectangle(perimeter / 4)

    def __sub__(self, other):
        perimeter = self.perimeter() - other.perimeter()
        if perimeter < 0:
            raise SubtractionError()
        return Rectangle(perimeter / 4)

    def __eq__(self, other):
        return self.area() == other.area()

    def __ne__(self, other):
        return self.area() != other.area()

    def __gt__(self, other):
        return self.area() > other.area()

    def __ge__(self, other):
        return self.area() >= other.area()

    def __lt__(self, other):
        return self.area() < other.area()

    def __le__(self, other):
        return self.area() <= other.area()

    def __str__(self):
        return f'length = {self.length}; width = {self.width}'

    def __repr__(self):
        return f'Rectangle({self.length}, {self.width}'


if __name__ == '__main__':
    r1 = Rectangle(5, 2)
    r2 = Rectangle(5, 20)
    r3 = r2 - r1
    r4 = r1 - r2

