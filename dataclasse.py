from dataclasses import dataclass
from typing import ClassVar

@dataclass

class user:
    first_name: str
    last_name: str
    age: int

    def __post_init__(self):
        self.full_name = f"{self.first_name} {self.last_name} {self.age} "

    # c:ClassVar[int]

E1 = user(first_name = "BAHATI", last_name="Innocent", age=35)
# print(E1.first_name)
# print(E1.last_name)
# print(E1.age)
print(E1.full_name)
# print(E1.__dict__)