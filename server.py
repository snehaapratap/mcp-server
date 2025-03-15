from fastapi import FastAPI
import requests
import os
from dotenv import load_dotenv

load_dotenv()  # Load API keys from .env

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "MCP Server is running"}

# Define MCP-compatible endpoint
@app.post("/mcp")
def mcp_handler(data: dict):
    return {"response": "MCP server received the request", "data": data}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
