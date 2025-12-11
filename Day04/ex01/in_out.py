def square(x: int | float) -> int | float:
    """Returns the square of x."""
    return x * x


def pow(x: int | float) -> int | float:
    """Returns x raised to the power of x."""
    return x ** x


def outer(x: int | float, function) -> object:
    """Returns a closure that applies 'function' to 'x'
    and updates 'x' each time it's called."""
    count = 0

    def inner() -> int | float:
        nonlocal x, count
        count += 1
        result = function(x)
        x = result
        print(f"Function called {count} time(s).")
        return result
    return inner
