
# 🚀 GitHub MCP Server - FastAPI Implementation

## 🌟 Overview
This project implements a **Model Context Protocol (MCP) server** using **FastAPI**, enabling AI assistants like Claude to interact with GitHub. The server provides API endpoints to fetch user details, manage repositories, create issues, and automate GitHub workflows.

## ✨ Features
- ✅ Fetch **GitHub user details** and repositories
- ✅ **Create and manage issues** in repositories
- ✅ **List all issues** in a repository
- ✅ **Star a repository**
- ✅ AI-powered **GitHub Issue Summarization** (Optional)
- ✅ Secure API with **GitHub OAuth Token**
- ✅ **Asynchronous** FastAPI implementation

---

## 🛠️ Setup & Installation

### **1️⃣ Clone the Repository**
```sh
git clone https://github.com/snehaapratap/mcp-server.git
cd mcp-server
```

### **2️⃣ Create & Activate a Virtual Environment**
```sh
python3 -m venv venv
source venv/bin/activate  
```

### **3️⃣ Install Dependencies**
```sh
pip install -r requirements.txt
```

### **4️⃣ Set Up Environment Variables**
Create a `.env` file in the root directory and add your **GitHub Personal Access Token (PAT)**:

```
GITHUB_TOKEN=your_personal_access_token
```

### **5️⃣ Run the FastAPI Server**
```sh
uvicorn server:app --reload
```
The server will start on **http://127.0.0.1:8000**.

---

## 🔥 API Endpoints

| Method | Endpoint | Description |
|--------|---------|-------------|
| **GET** | `/` | Health check for MCP server |
| **GET** | `/github/user` | Fetch GitHub user details |
| **GET** | `/github/repos` | Get all repositories of the authenticated user |
| **POST** | `/github/create-issue` | Create an issue in a repository |
| **GET** | `/github/list-issues` | List all issues in a repository |
| **PUT** | `/github/star-repo` | Star a repository |
| **POST** | `/github/summarize-issues` | AI-powered issue summarization (Optional) |

---

## ⚡ Usage Examples (cURL)

### 🔹 **Get User Details**
```sh
curl -X GET "http://127.0.0.1:8000/github/user"
```

### 🔹 **Fetch Repositories**
```sh
curl -X GET "http://127.0.0.1:8000/github/repos"
```

### 🔹 **Create an Issue**
```sh
curl -X POST "http://127.0.0.1:8000/github/create-issue?owner=your-username&repo=your-repo&title=New%20Issue&body=This%20is%20a%20test%20issue"
```

### 🔹 **Star a Repository**
```sh
curl -X PUT "http://127.0.0.1:8000/github/star-repo?owner=your-username&repo=your-repo"
```

---

## 🎥 Slides
📌 **[View the Slides](https://gamma.app/docs/GitHub-MCP-Server-with-FastAPI-m9vyprwqynhaln7)**  

---

## 🛡️ Error Handling
The API handles errors gracefully and returns meaningful messages:
```json
{
  "error": "Invalid GitHub Token",
  "hint": "Ensure your token has the 'repo' scope."
}
```

---

## 🎯 Future Enhancements
- 🔹 Support for **pull requests management**
- 🔹 Implement **WebSockets** for real-time GitHub notifications
- 🔹 **Deploy on AWS/GCP** with CI/CD pipeline

---

## 💡 Contributing
Want to improve this project? Feel free to open a **pull request** or file an **issue**!

---

## 👨‍💻 Author
🔹 **Sneha P Pratap**  
🔹 GitHub: [@snehaapratap](https://github.com/snehaapratap)  
🔹 LinkedIn: [Sneha Prem Pratap](https://www.linkedin.com/in/sneha-prem-pratap/)  

---
