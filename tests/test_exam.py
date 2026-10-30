import pytest

from src.core.student import Student
from src.core.teacher import Teacher
from src.univ.course import Course
from src.univ.exam import Exam
from src.exception import ExamFailedError


def test_exam_failure_raises_exception():
    student = Student(
        knowledge=5,
        motivation=10,
        fatigue=50,
    )
    teacher = Teacher(teaching_quality=0.5)

    course = Course(
        name="Test Course",
        difficulty=1.0,
        hours_per_week=2,
        teacher=teacher,
        students=[student],
    )

    exam = Exam(course, pass_threshold=50)

    with pytest.raises(ExamFailedError):
        exam.evaluate(student)
