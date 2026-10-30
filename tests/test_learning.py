from src.core.student import Student
from src.core.teacher import Teacher
from src.univ.learning import BasicLearningStrategy


def test_learning_increases_knowledge():
    student = Student(motivation=80)
    teacher = Teacher(teaching_quality=0.9)

    strategy = BasicLearningStrategy()

    initial_knowledge = student.knowledge

    strategy.apply(
        student=student,
        teacher=teacher,
        hours=4,
        difficulty=1.0,
    )

    assert student.knowledge > initial_knowledge
