from pathlib import Path

def save_report(report_text: str, file_path: Path) -> Path:
    """
    saves report text to a file at the specified path
    pathlib for reliable file system operations
    """
    path = Path(file_path)
    
    path.write_text(report_text, encoding="utf-8")
    
    return path

def read_input_file(file_path: Path) -> str:
    """
    reads raw data from the input file for further processing
    """
    path = Path(file_path)
    
    if not path.exists():
        raise FileNotFoundError(f"Input file not found: {path}")
        
    return path.read_text(encoding="utf-8")

def read_back(filepath: str) -> str:
    """
    keeps the function for compatibility with the previous code
    but now uses pathlib internally
    """
    return Path(filepath).read_text(encoding="utf-8")

if __name__ == "__main__":
    print()
    print("Module: saveit")
    print()
    print("Purpose: Working with files through pathlib.")
    print()