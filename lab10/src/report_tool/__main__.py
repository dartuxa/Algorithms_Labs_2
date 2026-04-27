import argparse
import logging
import sys
from pathlib import Path

from .functions import parse_numbers, analyze_numbers
from .report_output import build_sorted_report, build_json_report
from .saveit import save_report, read_input_file

def setup_logging(level_name):
    level = getattr(logging, level_name.upper(), logging.INFO)
    logging.basicConfig(
        level=level,
        format="%(levelname)s: %(message)s"
    )
    return logging.getLogger(__name__)

def main():
    parser = argparse.ArgumentParser(description="Report Tool CLI")
    parser.add_argument("--input", required=True, help="Path to input file")
    parser.add_argument("--out", required=True, help="Path to output file")
    parser.add_argument(
        "--format", 
        choices=["text", "json"], 
        default="text", 
        help="Output format (text or json)"
    )
    parser.add_argument(
        "--log-level", 
        choices=["DEBUG", "INFO", "WARNING", "ERROR"], 
        default="INFO", 
        help="Logging level"
    )

    args = parser.parse_args()

    logger = setup_logging(args.log_level)

    try:
        
        input_path = Path(args.input)
        logger.info(f"Reading input from: {input_path}")
        raw_data = read_input_file(input_path)

        logger.info("Parsing data...")
        numbers = parse_numbers(raw_data)
        
        logger.info("Analyzing numbers...")
        stats = analyze_numbers(numbers)

        if args.format == "json":
            logger.info("Generating JSON report...")
            result = build_json_report(stats)
        else:
            logger.info("Generating text report...")
            result = build_sorted_report(numbers, stats)

        output_path = Path(args.out)
        logger.info(f"Saving report to: {output_path}")
        save_report(result, output_path)

        logger.info("Done successfully!")

    except Exception as e:
        logger.error(f"An error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()