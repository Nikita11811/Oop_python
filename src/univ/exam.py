from dataclasses import dataclass

from src.core.student import Student
from src.univ.course import Course
from src.exception import ExamFailedError


@dataclass(slots=True)
class Exam:
    course: Course
    pass_threshold: float = 50.0

    def evaluate(self, student: Student) -> None:
        """
        Evaluate a student. Raises ExamFailedError on failure.
        """
        score = (
            student.knowledge
            * student.motivation
            / (1 + student.fatigue)
        )

        if score < self.pass_threshold:
            raise ExamFailedError(
                f"Student failed exam in {self.course.name}: {score:.2f}"
            )
