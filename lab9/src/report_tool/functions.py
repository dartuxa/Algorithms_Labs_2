def _cleanup_pieces(parts):
    cleaned = []
    for item in parts:
        item = item.strip()
        if item != "":
            cleaned.append(item)
    return cleaned


def parse_numbers(text: str) -> list[float]:
    pieces = text.replace(";", ",").split(",")
    pieces = _cleanup_pieces(pieces)
    result = []

    for p in pieces:
        result.append(float(p))

    return result


def _check_input(numbers):
    if not numbers:
        raise ValueError("numbers must not be empty")


def analyze_numbers(numbers: list[float]) -> dict:
    _check_input(numbers)

    total = sum(numbers)
    count = len(numbers)
    avg = total / count

    return {
        "count": count,
        "sum": total,
        "min": min(numbers),
        "max": max(numbers),
        "mean": avg,
    }


def sort_numbers(numbers: list[float]) -> list[float]:
    return sorted(numbers)



if __name__ == "__main__":
    print()
    print("Module: helpers")
    print()
    print("Purpose: Parse text strings into numbers and perform mathematical analysis.")
    print("Public functions: parse_numbers, analyze_numbers, sort_numbers")
    print()
    print("Example usage:")
    print()
    print("  parse_numbers('1, 2, 3') -> [1.0, 2.0, 3.0]")
    print()