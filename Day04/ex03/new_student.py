import random
import string

from dataclasses import dataclass, field
def generate_id() -> str:
    return "".join(random.choices(string.ascii_lowercase, k = 15))

@dataclass
class Student:
    name: str
    surname: str
    active: bool = True
    login: str = field(init=False)
    id: str = field(default_factory=generate_id)

    def __post_init__(self) -> None:
        # Build login from name and surname safely (handle empty/whitespace)
        name = (self.name or "").strip()
        surname = (self.surname or "").strip()
        if name and surname:
            self.login = name[0].upper() + surname.lower()
        else:
            self.login = ""

    def __str__(self) -> str:
        return (
            f"Student(name={self.name}, surname={self.surname}, active={self.active}, "
            f"login={self.login}, id={self.id})"
        )
