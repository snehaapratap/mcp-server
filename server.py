from fastapi import FastAPI, HTTPException
import requests
import os
from dotenv import load_dotenv

load_dotenv()  

app = FastAPI()

GITHUB_API_URL = "https://api.github.com"
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
HEADERS = {"Authorization": f"token {GITHUB_TOKEN}"}

@app.get("/")
def read_root():
    return {"message": "GitHub MCP Server is running"}

@app.get("/github/user")
def get_github_user():
    """Fetch GitHub user details."""
    response = requests.get(f"{GITHUB_API_URL}/user", headers=HEADERS)
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail=response.json())
    return response.json()

@app.get("/github/repos")
def get_repos():
    """Fetch user repositories."""
    response = requests.get(f"{GITHUB_API_URL}/user/repos", headers=HEADERS)
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail=response.json())
    return response.json()

@app.post("/github/create-issue")
def create_issue(owner: str, repo: str, title: str, body: str = ""):
    """Create a new GitHub issue."""
    url = f"{GITHUB_API_URL}/repos/{owner}/{repo}/issues"
    data = {"title": title, "body": body}
    response = requests.post(url, json=data, headers=HEADERS)
    if response.status_code != 201:
        raise HTTPException(status_code=response.status_code, detail=response.json())
    return response.json()
