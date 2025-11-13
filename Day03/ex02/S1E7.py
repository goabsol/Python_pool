from S1E9 import Character


class Baratheon(Character):
    def __init__(self, name, is_alive=True):
        """
        Initialize a Baratheon character

        name (str): first name of the character
        is_alive (bool): is the character alive
        """
        super().__init__(name, is_alive)
        self.family_name = "Baratheon"
        self.eyes = "brown"
        self.hairs = "dark"

    def die(self):
        """
        /killself
        """
        self.is_alive = False


class Lannister(Character):
    def __init__(self, name, is_alive=True):
        """
        Initialize a Lannister character

        name (str): first name of the character
        is_alive (bool): is the character alive
        """
        super().__init__(name, is_alive)
        self.family_name = "Lannister"
        self.eyes = "blue"
        self.hairs = "light"

    def die(self):
        """
        Mark the character as not alive.
        """
        self.is_alive = False

    @classmethod
    def create_lannister(cls, name, is_alive):
        """
        Factory method to create a Lannister character.

        name (str): first name of the character
        is_alive (bool): is the character alive

        Returns:
        Lannister: A new instance of Lannister with the given attributes.
        """
        instance = cls(name)
        instance.is_alive = is_alive
        return instance
