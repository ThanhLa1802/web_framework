#demo query big data
from fastapi import FastAPI, Query, HTTPException
from fastapi.responses import JSONResponse, StreamingResponse
from fastapi.middleware.cors import CORSMiddleware
import sqlite3
import json

app = FastAPI()
DATABASE = 'big_data.db'



origins = [
    "http://127.0.0.1:5501",  # URL FE của bạn
    "http://localhost:5501",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,        # cho phép domain FE
    allow_credentials=True,
    allow_methods=["*"],          # GET, POST, ...
    allow_headers=["*"],          # tất cả headers
)

def initialize_db():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS big_data (
            id INTEGER PRIMARY KEY,
            data TEXT
        )
    ''')
    # Insert sample big data if table is empty
    cursor.execute('SELECT COUNT(*) FROM big_data')
    if cursor.fetchone()[0] == 0:
        for i in range(1, 1000001):
            cursor.execute('INSERT INTO big_data (data) VALUES (?)', (f'Sample data {i}',))
    conn.commit()
    conn.close()

initialize_db()

#query directly all big data
@app.get("/direct_query")
def direct_query():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('SELECT id, data FROM big_data')
    rows = cursor.fetchall()
    conn.close()
    results = [{"id": row[0], "data": row[1]} for row in rows]
    return JSONResponse(content=results)

#paginated query from big data
@app.get("/pagination")
def paginated_query(page: int = 1, size: int = 100):
    if page < 1 or size < 1:
        raise HTTPException(status_code=400, detail="Page và Size phải lớn hơn 0")
        
    offset = (page - 1) * size
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    
    try:
        cursor.execute("SELECT COUNT(*) FROM big_data")
        total_items = cursor.fetchone()[0]
    except Exception as e:
        conn.close()
        raise HTTPException(status_code=500, detail=f"Lỗi truy vấn COUNT: {e}")
        
    cursor.execute('SELECT id, data FROM big_data LIMIT ? OFFSET ?', (size, offset))
    rows = cursor.fetchall()
    
    conn.close()
    
    results = [{"id": row[0], "data": row[1]} for row in rows]
    
    return JSONResponse(content={
        "page": page, 
        "size": size, 
        "total_items": total_items, # Thêm tổng số bản ghi
        "results": results
    })


#streamed query from big data
@app.get("/stream")
def streamed_query():
    def generate():
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        cursor.execute("SELECT id, data FROM big_data")
        for row in cursor:
            yield json.dumps({"id": row[0], "data": row[1]}) + "\n"
        conn.close()

    headers = {"Content-Disposition": "attachment; filename=big_data.json"}
    return StreamingResponse(generate(), media_type="application/json", headers=headers)

#push data to s3 bucket and return link
@app.get("/push_to_s3")
def push_to_s3():
    # This is a placeholder function. Implement actual S3 upload logic here.
    s3_link = "https://s3.amazonaws.com/your-bucket/big_data.json"
    #send email with link (omitted)
    return JSONResponse(content={"s3_link": s3_link})   