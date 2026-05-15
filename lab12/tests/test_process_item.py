import pytest
from src.async_tool.functions import process_item
from src.async_tool.classes import TaskItem


@pytest.mark.asyncio
async def test_process_item_success():
    
    item: TaskItem = {"id": 1, "delay": 0.01, "good": True}
    
    result = await process_item(item)
    
    assert result["id"] == 1
    assert result["status"] == "done"

@pytest.mark.asyncio
async def test_process_item_failure():

    item: TaskItem = {"id": 2, "delay": 0.01, "good": False}
    
    with pytest.raises(ValueError) as exc_info:
        await process_item(item)
    
    assert str(exc_info.value) == "Task 2 failed"

@pytest.mark.asyncio
async def test_process_item_structure():

    item: TaskItem = {"id": 3, "delay": 0.01, "good": True}
    
    result = await process_item(item)
    
    assert "id" in result
    assert "status" in result
    
    assert isinstance(result["id"], int)
    assert isinstance(result["status"], str)