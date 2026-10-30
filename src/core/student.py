from dataclasses import dataclass, field
from enum import Enum, auto

from src.core.person import Person
from src.core.decorators import track_step

class StudentStatus(Enum):
    ENROLLED = auto()
    DROPPED_OUT = auto()


@dataclass(slots=True)
class Student(Person):
    knowledge: float = field(default=0.0)
    fatigue: float = field(default=0.0)
    status: StudentStatus = field(default=StudentStatus.ENROLLED)

    @track_step
    def step(self, world: "UniversityWorld") -> None:
        if not self.is_active():
            self.status = StudentStatus.DROPPED_OUT

    @property
    def performance(self) -> float:
        """
        Overall performance metric.
        """
        return self.knowledge * self.motivation / (1 + self.fatigue)