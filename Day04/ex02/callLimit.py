from typing import Any

def callLimit(limit: int):
    count = 0
    def callLimiter(function):
        def limit_function(*args: Any, **kwds: Any):
            nonlocal count
            if count < limit:
                count += 1
                return function(*args, **kwds)
            # When the limit is exceeded, print a helpful message and raise an error
            msg = f"Error: {function} call too many times"
            print(msg)
            # raise RuntimeError(msg)
        return limit_function
    return callLimiter