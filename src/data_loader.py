import csv
from pathlib import Path

from src.core.student import Student


def load_students(csv_path: Path) -> list[Student]:
    """Загружает студентов из CSV-файла."""
    students = []

    with csv_path.open("r", encoding="utf-8-sig", newline="") as file:
        reader = csv.DictReader(file)

        required_columns = {"name", "motivation", "energy", "knowledge"}
        if not required_columns.issubset(reader.fieldnames or set()):
            raise ValueError(
                "CSV должен содержать столбцы: name, motivation, energy, knowledge"
            )

        for row in reader:
            students.append(
                Student(
                    name=row["name"],
                    motivation=float(row["motivation"]),
                    energy=float(row["energy"]),
                    knowledge=float(row["knowledge"]),
                )
            )

    if not students:
        raise ValueError("В CSV-файле нет студентов.")

    return students
