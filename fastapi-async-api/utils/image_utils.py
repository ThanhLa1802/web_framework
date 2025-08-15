from PIL import Image
import io

async def convert_image_grayscale(image_bytes: bytes) -> bytes:
    """
    Convert an image to grayscale.

    Args:
        image_bytes (bytes): The input image in bytes format.

    Returns:
        bytes: The grayscale image in bytes format.
    """
    # Open the image from bytes
    image = Image.open(io.BytesIO(image_bytes))
    
    # Convert the image to grayscale
    grayscale_image = image.convert("L")
    
    # Save the grayscale image to a bytes buffer
    output_buffer = io.BytesIO()
    grayscale_image.save(output_buffer, format='PNG')
    
    # Return the bytes of the grayscale image
    return output_buffer.getvalue()