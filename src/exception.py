class UniversitySimulationError(Exception):
    """Base exception for university simulation."""


class ExamFailedError(UniversitySimulationError):
    """Raised when a student fails an exam."""


class BurnoutError(UniversitySimulationError):
    """Raised when a teacher is burned out."""
