import os


def save_report(report_text: str, filename: str) -> str:
    '''
    function for saving reports to files
    '''
    path = f"{filename}.txt"
    with open(path, "w", encoding="utf-8") as f:
        f.write(report_text)
    return path


def read_back(filepath: str) -> str:
    '''
    function to read back the contents of a saved report file
    '''
    with open(filepath, "r", encoding="utf-8") as f:
        return f.read()



if __name__ == "__main__":
    print()
    print("Module: saveit")
    print()
    print("Purpose: Save and read text files containing reports.")
    print("Public functions: save_report, read_back")
    print()
    print("Example usage:")
    print()
    print("  save_report('report text', 'report_output') -> saves to report_output.txt")
    print()
    print("  read_back('report_output.txt') -> returns the contents of the file")
    print()
