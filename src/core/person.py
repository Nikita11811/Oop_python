from abc import ABC
from dataclasses import dataclass, field

from src.core.entity import Entity


@dataclass(slots=True)
class Person(Entity, ABC):
    name: str = "Unnamed"
    energy: float = field(default=80.0)
    motivation: float = field(default=80.0)

    def is_active(self) -> bool:
        return self.energy > 0 and self.motivation > 0
