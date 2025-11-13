class calculator:

    def __init__(self, vector):
        """
        calculator constructor

        vector (list): The vector of numbers
        """
        self.vector = vector

    def __add__(self, object) -> None:
        """
        Returns:
            vector after addition.
        """
        self.vector = [i + object for i in self.vector]
        print(self.vector)
        return [i for i in self.vector]

    def __mul__(self, object) -> None:
        """
        Returns:
            vector after multiplication.
        """
        self.vector = [i * object for i in self.vector]
        print(self.vector)
        return [i for i in self.vector]

    def __sub__(self, object) -> None:
        """
        Returns:
            vector after subtraction.
        """
        self.vector = [i - object for i in self.vector]
        print(self.vector)
        return [i for i in self.vector]

    def __truediv__(self, object) -> None:
        """
        Returns:
            vector after division.

        Raises:
            ZeroDivisionError: If division by zero is attempted.
        """
        try:
            if object == 0:
                raise ZeroDivisionError("this is not a limit")
            self.vector = [i / object for i in self.vector]
            print(self.vector)
            return [i for i in self.vector]
        except ZeroDivisionError as error:
            print(ZeroDivisionError.__name__ + ":", error)
