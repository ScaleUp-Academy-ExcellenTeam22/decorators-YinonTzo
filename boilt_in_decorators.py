"""
https://docs.python.org/3.5/library/functools.html#functools.wraps
Here I show how functools.wraps works
"""
import functools


def wrap_func_using_functools(func: callable) -> callable:
    """
    Wrap some func.
    :param func: To execute.
    """
    @functools.wraps(func)
    def wrapper():
        print("Hello from wrap.")
        func()

    return wrapper


@wrap_func_using_functools
def some_func() -> None:
    """
    Function to be wrap
    """
    print("Hello from Some func")


def wrap_func_without_using_functools(func: callable) -> callable:
    """
    Wrap some func.
    :param func: To execute.
    """
    # @functools.wraps(func) don't use it and leaves you doc
    def wrapper():
        print("Hello from wrap.")
        func()

    return wrapper


@wrap_func_without_using_functools
def other_func() -> None:
    """
    Function to be wrap
    """
    print("Hello from other func")


if __name__ == '__main__':
    # Here you can see that @wrap keeps on name and doc.
    some_func()
    print(some_func.__name__)
    print(some_func.__doc__)

    # Here you can see that you lost your doc and get garbage.
    other_func()
    print(other_func.__name__)
    print(other_func.__doc__)
