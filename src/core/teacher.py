from dataclasses import dataclass, field

from src.core.person import Person
from src.core.decorators import track_step


@dataclass(slots=True)
class Teacher(Person):
    teaching_quality: float = field(default=0.7)
    workload: float = field(default=0.5)
    burnout: float = field(default=0.0)

    @track_step
    def step(self, world: "UniversityWorld") -> None:
        self.burnout += self.workload * 0.01
        self.energy -= self.workload * 2
