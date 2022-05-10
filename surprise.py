import functools


def surprise(func: callable) -> callable:
    """
    Make a decorator that Does something else than func.
    :param func: Function to call
    :return: function that returns other string than func.
    """
    @functools.wraps(func)
    def decorate_function():
        return "Surprise!"

    return decorate_function


@surprise
def some_function() -> str:
    """
    Make some string
    :return: str.
    """
    return "Some function"


if __name__ == '__main__':
    print(some_function())
