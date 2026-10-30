from dataclasses import dataclass, field

from src.core.student import Student
from src.core.teacher import Teacher

from src.univ.learning import LearningStrategy, BasicLearningStrategy


@dataclass(slots=True)
class Course:
    name: str
    difficulty: float
    hours_per_week: int
    teacher: Teacher
    learning_strategy: LearningStrategy = field(
        default_factory=BasicLearningStrategy
    )
    students: list[Student] = field(default_factory=list)

    def conduct_week(self) -> None:
        self.teacher.energy -= self.hours_per_week

        for student in self.students:
            self.learning_strategy.apply(
                student=student,
                teacher=self.teacher,
                hours=self.hours_per_week,
                difficulty=self.difficulty,
            )

