import time
from functools import wraps

from src.utils.console import console


def track_step(func):
    counter = 0

    @wraps(func)
    def wrapper(self, *args, **kwargs):
        nonlocal counter

        start = time.perf_counter()
        result = func(self, *args, **kwargs)
        elapsed = time.perf_counter() - start

        counter += 1

        console.print(
            f"[bold cyan][STEP][/bold cyan] "
            f"{self.__class__.__name__}.{func.__name__} | "
            f"calls={counter} | "
            f"time={elapsed:.6f}s"
        )

        return result

    return wrapper

