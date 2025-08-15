# Sử dụng Python 3.11 slim để nhẹ
FROM python:3.11-slim

# Thiết lập thư mục làm việc
WORKDIR /app

# Copy file requirements.txt và cài đặt dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy toàn bộ source code vào container
COPY . .

# Expose cổng API
EXPOSE 8000

# Chạy API bằng uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]