import asyncio
import uvicorn
from fastapi import FastAPI
from app.routes import router
from app.database import create_db_and_tables

app = FastAPI()
app.include_router(router)

@app.get("/")
async def root():
    return {"Hello": "World"}

async def main():
    await create_db_and_tables()
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)

if __name__ == "__main__":
    asyncio.run(main())
