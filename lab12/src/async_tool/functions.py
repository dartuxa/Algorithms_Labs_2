import asyncio
import logging


from .classes import TaskItem, TaskResult


async def process_item(item: TaskItem) -> TaskResult:
    await asyncio.sleep(item["delay"])
    if not item["good"]:
        raise ValueError(f"Task {item['id']} failed")
    return {
        "id": item["id"],
        "status": "done"
    }

async def safe_process(item: TaskItem, continue_on_error: bool) -> TaskResult:
    logging.info(f"Task {item['id']} started")
    try:
        result = await process_item(item)
        logging.info(f"Task {item['id']} completed")
        return result
    except Exception as e:
        logging.error(f"Task {item['id']} failed: {e}")
        if continue_on_error:
            return {
                "id": item["id"],
                "status": "error",
                "message": str(e)
            }
        else:
            raise

async def run_sync(tasks: list[TaskItem], continue_on_error: bool) -> list[TaskResult]:
    results: list[TaskResult] = []
    for task in tasks:
        result = await safe_process(task, continue_on_error)
        results.append(result)
    return results

async def run_async(tasks: list[TaskItem], continue_on_error: bool) -> list[TaskResult]:
    coros = [safe_process(task, continue_on_error) for task in tasks]
    return list(await asyncio.gather(*coros))

async def run_limited(tasks: list[TaskItem], limit: int, continue_on_error: bool) -> list[TaskResult]:
    semaphore = asyncio.Semaphore(limit)

    async def sem_process(task: TaskItem) -> TaskResult:
        async with semaphore:
            return await safe_process(task, continue_on_error)

    coros = [sem_process(task) for task in tasks]
    return list(await asyncio.gather(*coros))