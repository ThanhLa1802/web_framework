from datetime import timedelta
from fastapi import FastAPI, UploadFile, Form
from utils.image_utils import convert_image_grayscale
from utils.text_utils import reserve_text
import io
import aioboto3

AWS_BUCKET_NAME = "test-bucket"

app = FastAPI(title="Async API Demo")

async def upload_to_s3(file_bytes: bytes, filename: str) -> str:
    session = aioboto3.Session()
    async with session.client("s3", region_name="ap-southeast-1") as s3_client:
        await s3_client.put_object(
            Bucket=AWS_BUCKET_NAME,
            Key=filename,
            Body=file_bytes,
            ContentType="image/png"
        )
        # Tạo presigned URL có thời hạn 1 giờ
        url = await s3_client.generate_presigned_url(
            "get_object",
            Params={"Bucket": AWS_BUCKET_NAME, "Key": filename},
            ExpiresIn=int(timedelta(hours=1).total_seconds())
        )
        return url

@app.post("/convert-image/")
async def convert_image(file: UploadFile):
    """
    Endpoint to convert an uploaded image to grayscale.
    
    Args:
        file (UploadFile): The uploaded image file.
    
    Returns:
        StreamingResponse: The grayscale image as a response.
    """
    image_bytes = await file.read()
     # Convert sang grayscale
    processed_bytes = await convert_image_grayscale(image_bytes)

    # Upload kết quả lên S3
    output_filename = f"converted/{file.filename}"
    url = await upload_to_s3(processed_bytes, output_filename)

    return {"download_url": url}

@app.post("/progress-text/")
async def convert_text(text: str = Form(...)):
    """
    Endpoint to convert text to speech.
    
    Args:
        text (str): The text to convert to speech.
    
    Returns:
        str: The reserved text.
    """
    reserved_text = await reserve_text(text)
    return {"original_text": text, "reserved_text": reserved_text}