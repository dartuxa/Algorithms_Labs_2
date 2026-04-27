import logging

logger = logging.getLogger(__name__)

def _cleanup_pieces(parts: list[str]) -> list[str]:
    cleaned = []
    for item in parts:
        item = item.strip()
        if item:
            cleaned.append(item)
    return cleaned

def parse_numbers(text: str) -> list[float]:
    logger.debug("Starting string parsing...")
    
    normalized_text = text.replace(";", ",").replace(" ", ",")
    pieces = normalized_text.split(",")
    
    cleaned_pieces = _cleanup_pieces(pieces)
    result = []

    for p in cleaned_pieces:
        try:
            result.append(float(p))
        except ValueError as e:
            logger.error(f"Could not convert '{p}' to number: {e}")
            raise

    logger.info(f"Successfully parsed {len(result)} numbers.")
    return result

def _check_input(numbers: list[float]):

    if not numbers:
        logger.warning("Attempted to analyze an empty list of numbers.")
        raise ValueError("numbers must not be empty")

def analyze_numbers(numbers: list[float]) -> dict:

    _check_input(numbers)
    
    logger.info("Performing statistical analysis...")
    
    total = sum(numbers)
    count = len(numbers)
    avg = total / count

    stats = {
        "count": count,
        "sum": total,
        "min": min(numbers),
        "max": max(numbers),
        "mean": avg,
    }
    
    logger.debug(f"Analysis results: {stats}")
    return stats

def sort_numbers(numbers: list[float]) -> list[float]:

    logger.debug("Sorting numbers for the report.")
    return sorted(numbers)

if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    print("Testing parse_numbers with '1,2; 3 4.5':")
    print(parse_numbers("1,2; 3 4.5"))