"""Simple examples demonstrating Python generators."""

from collections.abc import Iterable, Iterator
from typing import Generator


def count_up_to(limit: int) -> Generator[int, None, None]:
    """Yield numbers from 1 up to ``limit`` inclusive."""
    for number in range(1, limit + 1):
        yield number


def square_numbers(numbers: Iterable[int]) -> Generator[int, None, None]:
    """Yield squares for each provided number."""
    for value in numbers:
        yield value * value


def even_numbers() -> Iterator[int]:
    """Generate an infinite sequence of even numbers starting at 0."""
    current = 0
    while True:
        yield current
        current += 2


def main() -> None:
    print("Counting from 1 to 5 (using a generator function):")
    for num in count_up_to(5):
        print(f"  got {num}")

    print("\nSquares of 1 through 5 (chaining two generators):")
    for square in square_numbers(count_up_to(5)):
        print(f"  got {square}")

    print("\nFirst five even numbers (stopping an infinite generator early):")
    evens = even_numbers()
    for _ in range(5):
        print(f"  got {next(evens)}")

    print("\nGenerator expression for cubes of 1 through 5:")
    cubes = (value ** 3 for value in range(1, 6))
    for cube in cubes:
        print(f"  got {cube}")


if __name__ == "__main__":
    main()
