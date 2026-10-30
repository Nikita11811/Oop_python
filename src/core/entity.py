from abc import ABC, abstractmethod
from typing import Self


class Entity(ABC):
    """
    Базовый класс для всех сущностей.
    """

    @abstractmethod
    def step(self, world: "UniversityWorld") -> None:
        """
        Perform one simulation step.
        """
        raise NotImplementedError
