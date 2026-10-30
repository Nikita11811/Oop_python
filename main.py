from pathlib import Path

from src.analytics import create_visualizations
from src.core.world import UniversityWorld
from src.core.teacher import Teacher
from src.data_loader import load_students
from src.univ.course import Course


def main() -> None:
    project_dir = Path(__file__).resolve().parent
    students = load_students(project_dir / "data" / "students.csv")

    world = UniversityWorld()
    teacher = Teacher(
        name="Alex Morgan",
        teaching_quality=0.8,
        workload=0.5,
    )

    course = Course(
        name="OOP in Python",
        difficulty=1.2,
        hours_per_week=4,
        teacher=teacher,
        students=students.copy(),
    )

    world + teacher
    for student in students:
        world + student
    world + course

    world.run(16)

    print("\\nFinal student results:")
    for student in students:
        print(
            f"{student.name}: knowledge={student.knowledge:.2f}, "
            f"motivation={student.motivation:.2f}, status={student.status.name}"
        )

    create_visualizations(world, project_dir / "results")


if __name__ == "__main__":
    main()
