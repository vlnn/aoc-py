from pathlib import Path


def get_input_path(day: int, part: int) -> Path:
    """Return the path to the input file for the given day."""
    return Path.cwd().parent / "inputs" / f"day{day}-{part}.txt"


def load_input(day: int, part: int) -> str:
    """Load the input for the given day as a string."""
    with open(get_input_path(day, part), "r") as f:
        return f.read()


def load_input_lines(day: int, part: int) -> list[str]:
    """Load the input for the given day as a list of lines."""
    return load_input(day, part).splitlines()
