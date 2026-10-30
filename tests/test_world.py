from src.core.world import UniversityWorld
from src.core.student import Student
from src.core.teacher import Teacher


def test_add_entities():
    world = UniversityWorld()
    student = Student()
    teacher = Teacher()

    world + student + teacher

    assert student in world.entities
    assert teacher in world.entities
