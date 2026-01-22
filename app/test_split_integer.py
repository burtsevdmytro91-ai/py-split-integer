import pytest
from app import split_integer


@pytest.mark.parametrize(
    "value, parts, expected",
    [
        (17, 4, [4, 4, 4, 5]),
        (32, 6, [5, 5, 5, 5, 6, 6]),
        (10, 6, [1, 1, 2, 2, 2, 2]),
        (2, 5, [0, 0, 0, 1, 1]),
        (0, 5, [0, 0, 0, 0, 0]),
        (8, 1, [8]),
        (5, 5, [1, 1, 1, 1, 1]),
        (11, 3, [3, 4, 4]),
        (3, 10, [0, 0, 0, 0, 0, 0, 0, 1, 1, 1]),
    ]
)
def test_split_integer_rigorous(
        value: int, parts: int, expected: list
) -> None:
    result = split_integer.split_integer(value, parts)

    assert result == expected, (
        f"Error: for {value} with {parts} parts "
        f"expected {expected}, got {result}"
    )

    assert result == sorted(result), "Result must be sorted"
    assert sum(result) == value, "Sum of parts must equal value"
    assert len(result) == parts, "Length must equal parts"

    if parts > 0:
        assert max(result) - min(result) <= 1, "Diff must be <= 1"


def test_should_return_all_zeros_when_value_is_zero() -> None:
    result = split_integer.split_integer(0, 3)
    assert result == [0, 0, 0], "Should return zeros for zero value"
