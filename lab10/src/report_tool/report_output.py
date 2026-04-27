import json
from .functions import sort_numbers

def build_report(stats: dict) -> str:
    lines = []
    lines.append("number report".strip())
    lines.append("-" * 20)
    lines.append(f"count = {stats['count']}")
    lines.append(f"sum = {stats['sum']}")
    lines.append(f"min = {stats['min']}")
    lines.append(f"max = {stats['max']}")
    lines.append(f"mean = {round(stats['mean'], 2)}")
    return "\n".join(lines)

def build_sorted_report(numbers: list[float], stats: dict) -> str:
    ordered = sort_numbers(numbers)
    
    base_report = build_report(stats)
    
    lines = [base_report]
    lines.append(f"sorted = {ordered}")
    return "\n".join(lines)

def build_json_report(stats: dict) -> str:
    
    return json.dumps(stats, indent=4)

if __name__ == "__main__":
    test_stats = {'count': 2, 'sum': 4.0, 'min': 1.0, 'max': 3.0, 'mean': 2.0}
    print("Text format:")
    print(build_report(test_stats))
    print("\nJSON format:")
    print(build_json_report(test_stats))