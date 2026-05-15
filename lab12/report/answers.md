## Answers for Lab 12: Testing an Async CLI Tool


1. What is the difference between unit tests and behavior tests?


- Unit tests focus on verifying the logic of a single, isolated component - such as the ```process_item``` function-by calling it directly and checking its specific return values or exceptions.  

- Behavior tests (also known as black-box tests) evaluate the application as a whole from the user's perspective. They focus on how the system responds to inputs (e.g., CLI arguments) by checking the final output and exit codes without concern for the internal implementation details. 


2. Why is subprocess used for CLI testing?


The ```subprocess``` module is used because it allows the test suite to execute the tool as an independent process, mimicking exactly how a real user would run it in a terminal. It enables the tester to capture the standard output (stdout), error messages (stderr), and the process exit code, which are the primary indicators of a CLI tool's behavior.


3. What happens if one async task fails without error handling?


In an asynchronous environment, if a task encounters an error (like a ValueError) and there is no error handling in place, the exception will propagate up to the event loop. This typically results in the premature termination of the batch processing and causes the entire program to crash or exit with a non-zero status code.


4. When should you test internal functions vs full system behavior?


Internal functions should be tested when they contain complex calculations, specific business logic, or edge cases that need to be validated in isolation to ensure foundational correctness. Full system behavior should be tested to ensure that all internal components integrate correctly and that the tool meets its functional requirements, such as producing valid JSON output and preserving item order. 


5. What are the risks of time-based tests?


Time-based tests are highly susceptible to "flakiness" because execution speed depends on external factors like CPU load, the operating system's scheduler, or the testing environment (e.g., local machine vs. a CI/CD server). Because performance can fluctuate, using strict time thresholds often leads to false failures even when the underlying code logic is correct.