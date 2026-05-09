import asyncio
import argparse
import json
import logging
import sys
from pathlib import Path


from .classes import TaskItem
from .functions import run_sync, run_async, run_limited


async def main_async() -> None:
    parser = argparse.ArgumentParser(description="Async Batch Processor CLI")
    parser.add_argument("input_json", type=str, help="path to input file")
    parser.add_argument("--mode", choices=["sync", "async", "limited"], default="sync", help="Execution mode")
    parser.add_argument("--limit", type=int, default=5, help="Concurrency limit (for limited mode)")
    parser.add_argument("--continue-on-error", action="store_true", help="Continue processing if a task fails")
    parser.add_argument("--log-level", choices=["DEBUG", "INFO", "WARNING", "ERROR"], default="WARNING", help="Logging level")

    args = parser.parse_args()

    log_level = getattr(logging, args.log_level)
    logging.basicConfig(level=log_level, format="%(levelname)s: %(message)s")

    input_path = Path(args.input_json)
    if not input_path.exists():
        logging.error(f"Input file not found: {args.input_json}")
        sys.exit(1)

    try:
        with open(input_path, "r", encoding="utf-8") as f:
            tasks: list[TaskItem] = json.load(f)
    except json.JSONDecodeError as e:
        logging.error(f"Invalid JSON file: {e}")
        sys.exit(1)

    try:
        if args.mode == "sync":
            results = await run_sync(tasks, args.continue_on_error)
        elif args.mode == "async":
            results = await run_async(tasks, args.continue_on_error)
        else: # limited
            results = await run_limited(tasks, args.limit, args.continue_on_error)
        
        print(json.dumps(results, indent=2))

    except Exception as e:
        logging.error(f"Batch processing stopped due to error: {e}")
        sys.exit(1)

def main() -> None:
    asyncio.run(main_async())

if __name__ == "__main__":
    main()