from abc import ABC, abstractmethod


class Character(ABC):
    """Abstract class representing a character."""

    @abstractmethod
    def __init__(self, first_name, is_alive=True):
        """
        Character constructor

        name (str): character's first name
        is_alive (bool, optional): is the character alive
        Default is True.
        """
        self.name = first_name
        self.alive = is_alive

    def die(self):
        """
        /killself method to be implemented in subclasses
        """
        pass


class Stark(Character):
    """Stark character class."""
    def __init__(self, first_name, is_alive=True):
        """
        Stark character constructor
        """
        self.name = first_name
        self.is_alive = is_alive

    def die(self):
        """
        /killself
        """
        self.is_alive = False
