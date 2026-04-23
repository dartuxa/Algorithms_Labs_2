from .functions import parse_numbers, analyze_numbers
from .report_output import build_sorted_report
from .saveit import save_report, read_back


def show_help():
    print()
    print("report_tool - Instrument for analysis of numerical reports.")
    print()
    print("Features: number parsing, statistical analysis, report formatting and saving to file.")
    print()
    print("Example input:")
    print('  "1, 2, 3, 4.5"')
    print()


def example_workflow():
    text = "15, 8, 4, 16, 23, 42"
    numbers = parse_numbers(text)
    stats = analyze_numbers(numbers)
    report = build_sorted_report(numbers, stats)
    return report


def main():
    show_help()
    print("Demonstration of work:")
    report = example_workflow()
    print(report)

    path = save_report(report, "report_output")
    print()
    print("Saved to:", path)
    print()
    print("Contents of the saved file:")
    print(read_back(str(path)))



if __name__ == "__main__":
    main()
