import functools
from typing import Callable


def type_check(correct_type: any) -> Callable:
    """
    Check if the argument is the correct type.
    For more explanation I used this articles:
    https://realpython.com/primer-on-python-decorators/#decorators-with-arguments
    https://www.geeksforgeeks.org/decorators-with-parameters-in-python/
    :param correct_type: Type of argument.
    :return: Decorator function if the argument is ok.
    :raise Type error if the argument is not instance of correct type.
    """

    def decorator_func(func: Callable) -> any:
        @functools.wraps(func)
        def wrapper_func(arg: any) -> any:
            if isinstance(arg, correct_type):
                return func(arg)
            else:
                raise TypeError(f'Incorrect type. Type should be {correct_type}')

        return wrapper_func

    return decorator_func


@type_check(correct_type=int)
def times2(num: int) -> int:
    """
    Multiply by 2.
    :param num: Number to multiply.
    :return: Multiply value.
    """
    return num * 2


if __name__ == '__main__':
    print(times2(2))
    print(times2("stam"))
