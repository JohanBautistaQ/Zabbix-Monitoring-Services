import time
import random
from fastapi import FastAPI

app = FastAPI()

@app.get("/process")
async def process():
    delay = random.randint(5, 10)
    time.sleep(delay)
    return {"status": "done", "delay": delay}
