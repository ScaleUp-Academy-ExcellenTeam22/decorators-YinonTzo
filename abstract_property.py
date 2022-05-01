"""
https://docs.python.org/3.5/library/functions.html#property
Here I show how property works
"""


class Circle:
    """
    Class represent circle.

    args:
        radius: Radius for the circle. must be positive.
    """
    def __init__(self, radius):
        self.radius = radius

    def perimeter(self):
        """
        Calculate the perimeter of the circle.
        :return: the perimeter of the circle.
        """
        return 3.14 * self._radius * 2

    def area(self):
        """
        Calculate the area of the circle.
        :return: the area of the circle.
        """
        return 3.14 * self._radius ** 2

    @property
    def radius(self):
        """
        :return: The radius of the circle
        """
        return self._radius

    @radius.setter
    def radius(self, length: int) -> None:
        """
        Set new radius to the circle. must be positive.
        :param length: New radius.
        """
        if length < 1:
            self._radius = 1
        else:
            self._radius = length

    def __str__(self):
        return f'Circle:radius = {self._radius}'


if __name__ == '__main__':
    # Here you can see that you can't put -1 to the radius because of @setter
    # and the setter put 1
    c1 = Circle(-1)
    print(c1)
    print(c1.area())
    print(c1.perimeter())
    # Here you can see that you set a new radius
    c1.radius = 2
    print(c1.radius)

    # Here you can see that you can't put -3 to the radius because of @setter
    # and the setter put 1 again
    c1.radius = -3
    print(c1.radius)

