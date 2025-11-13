from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
    """DiamondTrap character class. \"false\" king"""
    def __init__(self, first_name, is_alive=True):
        """
        Initialize a DiamondTrap character
        name (str): first name of the character
        is_alive (bool): is the character alive
        """
        super().__init__(first_name, is_alive)

    def set_eyes(self, color):
        """
        Set the eye color of the character.
        color (str): The new eye color.
        """
        self.eyes = color

    def set_hairs(self, color):
        """
        Set the hair color of the character.
        color (str): The new hair color.
        """
        self.hairs = color

    def get_eyes(self):
        """
        Get the eye color of the character.
        Returns:
        str: The eye color.
        """
        return self.eyes

    def get_hairs(self):
        """
        Get the hair color of the character.
        Returns:
        str: The hair color.
        """
        return self.hairs
