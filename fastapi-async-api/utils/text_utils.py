import asyncio

async def reserve_text(text: str) -> str:
    """
    Simulates reserving a text by returning it after a short delay.
    
    Args:
        text (str): The text to reserve.
    
    Returns:
        str: The reserved text.
    """
    await asyncio.sleep(0.1)  # Simulate a delay for reserving the text
    return text