from abc import ABC, abstractmethod

from src.core.student import Student
from src.core.teacher import Teacher


class LearningStrategy(ABC):
    """
    Strategy for student learning behavior.
    """

    @abstractmethod
    def apply(
        self,
        student: Student,
        teacher: Teacher,
        hours: int,
        difficulty: float,
    ) -> None:
        pass


class BasicLearningStrategy(LearningStrategy):
    """
    Simple learning model.
    """

    def apply(
        self,
        student: Student,
        teacher: Teacher,
        hours: int,
        difficulty: float,
    ) -> None:
        if student.status.name != "ENROLLED":
            return

        knowledge_gain = (
            teacher.teaching_quality
            * student.motivation
            * hours
            / (1 + difficulty)
        ) * 0.01

        student.knowledge += knowledge_gain
        student.fatigue += hours * difficulty * 0.5
        student.motivation -= student.fatigue * 0.01

        # clamp values
        student.knowledge = min(student.knowledge, 100)
        student.motivation = max(student.motivation, 0)
