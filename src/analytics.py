from pathlib import Path

import matplotlib.pyplot as plt

from src.core.world import UniversityWorld


def create_visualizations(world: UniversityWorld, output_dir: Path) -> None:
    """Создаёт и сохраняет два графика по результатам симуляции."""
    output_dir.mkdir(parents=True, exist_ok=True)

    # График 1: средний уровень знаний по неделям.
    if world.history:
        weeks = [int(item["week"]) for item in world.history]
        average_knowledge = [
            item["average_knowledge"] for item in world.history
        ]

        plt.figure(figsize=(9, 5))
        plt.plot(weeks, average_knowledge, marker="o")
        plt.title("Average student knowledge over time")
        plt.xlabel("Simulation week")
        plt.ylabel("Average knowledge")
        plt.grid(True, linestyle="--", alpha=0.5)
        plt.tight_layout()
        plt.savefig(output_dir / "knowledge_over_time.png", dpi=150)
        plt.close()

    # График 2: итоговый уровень знаний каждого студента.
    students = world.students
    if students:
        names = [student.name for student in students]
        knowledge = [student.knowledge for student in students]

        plt.figure(figsize=(9, 5))
        bars = plt.bar(names, knowledge)
        plt.title("Final knowledge by student")
        plt.xlabel("Student")
        plt.ylabel("Knowledge")
        plt.ylim(bottom=0)
        plt.grid(axis="y", linestyle="--", alpha=0.5)

        for bar, value in zip(bars, knowledge):
            plt.text(
                bar.get_x() + bar.get_width() / 2,
                bar.get_height(),
                f"{value:.1f}",
                ha="center",
                va="bottom",
            )

        plt.tight_layout()
        plt.savefig(output_dir / "final_knowledge_by_student.png", dpi=150)
        plt.close()

    print(f"Charts saved to: {output_dir.resolve()}")
