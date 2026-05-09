## Answers for Lab 11: Async Batch Processor


1. Why does ```await``` inside a loop lead to sequential execution?


The ```await``` keyword pauses the execution of the current coroutine until the awaited task is completed. When placed inside a loop, the program must wait for the current task to finish before it can move to the next iteration. This results in tasks being processed one after another in a serial fashion.  


2. How does ```asyncio.gather``` change behavior?


```asyncio.gather``` allows multiple coroutines to be scheduled and executed concurrently. Instead of waiting for each task to complete before starting the next, the event loop manages all tasks simultaneously. This leads to a significant speedup for I/O-bound operations because the total execution time is determined by the longest individual task rather than the sum of all task delays.  


3. What happens if one task fails in async mode without ```--continue-on-error```?


If a task fails and the ```--continue-on-error``` flag is not provided, the program stops execution immediately upon the first failure. The exception from the failed task is propagated, and the tool exits with a non-zero status code.  


4. Why is a semaphore needed?


A semaphore (```asyncio.Semaphore```) is necessary to control and limit the number of concurrent tasks running at any given time. This prevents the application from overwhelming system resources, such as memory or network sockets, and helps avoid hitting rate limits on external services.  


5. When should async NOT be used?


Asynchronous programming should not be used for CPU-bound tasks, such as heavy mathematical computations, image processing, or data encryption. Because ```asyncio``` runs in a single thread, a blocking CPU-intensive task will "freeze" the event loop, preventing all other tasks from making progress. For such tasks, multi-processing is generally a better approach.