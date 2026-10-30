from typing import List, Union

from src.univ.course import Course
from src.univ.exam import Exam
from src.core.entity import Entity
from src.core.student import Student, StudentStatus
from src.exception import ExamFailedError
from src.utils.console import console


class UniversityWorld:
    def __init__(self):
        self.entities: List[Entity] = []
        self.courses: List[Course] = []
        self.week: int = 0
        # История среднего уровня знаний: одна запись на каждую неделю.
        self.history: list[dict[str, float]] = []

    def add_entity(self, entity: Entity) -> None:
        self.entities.append(entity)

    def add_course(self, course: Course) -> None:
        self.courses.append(course)

    def __add__(self, other: Union[Entity, Course]):
        if isinstance(other, Course):
            self.add_course(other)
        else:
            self.add_entity(other)
        return self

    def run(self, weeks: int) -> None:
        console.print(
            f"[bold green]Starting university simulation for {weeks} weeks[/bold green]"
        )

        for _ in range(weeks):
            self.step()

        console.print("[bold green]Simulation finished[/bold green]")

    def step(self) -> None:
        console.print(f"[bold yellow]--- Week {self.week + 1} ---[/bold yellow]")

        # 1. Обучение
        for course in self.courses:
            course.conduct_week()

        # 2. Экзамены каждые пять недель
        if self.week > 0 and self.week % 5 == 0:
            self._conduct_exams()

        # 3. Шаг всех сущностей
        for entity in list(self.entities):
            entity.step(self)

        self.week += 1
        self._save_weekly_statistics()

    def _save_weekly_statistics(self) -> None:
        students = self.students
        average_knowledge = (
            sum(student.knowledge for student in students) / len(students)
            if students
            else 0.0
        )
        self.history.append({
            "week": float(self.week),
            "average_knowledge": average_knowledge,
        })

    def _conduct_exams(self) -> None:
        console.print("[bold magenta]Exams week![/bold magenta]")

        for course in self.courses:
            exam = Exam(course)

            for student in list(course.students):
                try:
                    exam.evaluate(student)
                    console.print(
                        f"[green]✔ {student.name} passed exam in {course.name}[/green]"
                    )
                except ExamFailedError as e:
                    console.print(f"[bold red]✘ {student.name}: {e}[/bold red]")
                    student.status = StudentStatus.DROPPED_OUT
                    course.students.remove(student)

    @property
    def students(self) -> List[Student]:
        return [
            entity for entity in self.entities
            if isinstance(entity, Student)
        ]
