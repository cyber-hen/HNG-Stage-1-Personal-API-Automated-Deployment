---

# 🚀 Personal API – Automated Deployment (HNG Stage 1)

`https://img.shields.io/badge/Python-3.10+-blue`
`https://img.shields.io/badge/FastAPI-Framework-green`
`https://img.shields.io/badge/Build-Passing-brightgreen`
`https://img.shields.io/badge/License-MIT-yellow`

A lightweight, high‑performance **Personal API** built with **FastAPI** and deployed on an **AWS EC2** instance.  
This project demonstrates practical backend engineering and DevOps concepts including:

- Nginx reverse proxying  
- Systemd service management  
- Automated SSL/TLS with Certbot  
- Production‑grade directory structure  
- Auto‑run support for easy local execution  

---

## 📁 Project Structure

```
HNG-Stage-1-Personal-API-Automated-Deployment/
│
├── main.py                 # FastAPI application
├── run.sh                  # Auto-run script
├── requirements.txt        # Python dependencies
├── README.md               # Documentation
│
└── venv/                   # Auto-created virtual environment
```

---

## ⚡ Quick Start (Auto‑Run Enabled)

Clone the repository:

```bash
git clone https://github.com/cyber-hen/HNG-Stage-1-Personal-API-Automated-Deployment.git
cd HNG-Stage-1-Personal-API-Automated-Deployment
```

Run the API:

```bash
./run.sh
```

If needed:

```bash
chmod +x run.sh
./run.sh
```

Your API will be available at:

```
http://127.0.0.1:8000
```

---

## 🛠️ Auto‑Run Script (`run.sh`)

```bash
#!/bin/bash

# Create venv if missing
if [ ! -d "venv" ]; then
    python3 -m venv venv
fi

# Activate venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run the API
uvicorn main:app --host 0.0.0.0 --port 8000
```

This script ensures anyone can clone and run your API instantly — no manual setup required.

---

## 🧰 Tech Stack

| Layer | Technology |
|-------|------------|
| **Language** | Python 3.10+ |
| **Framework** | FastAPI |
| **Server** | Uvicorn |
| **Reverse Proxy** | Nginx |
| **Process Manager** | Systemd |
| **Infrastructure** | AWS EC2 (Ubuntu 24.04 LTS) |
| **SSL/TLS** | Certbot (Let’s Encrypt) |

---

## 🧱 System Architecture Diagram

```
                ┌──────────────────────────┐
                │        Client            │
                │  (Browser / Bot / API)   │
                └─────────────┬────────────┘
                              │
                              ▼
                    ┌──────────────────┐
                    │      Nginx       │
                    │ Reverse Proxy    │
                    └─────────┬────────┘
                              │
                              ▼
                    ┌──────────────────┐
                    │     Uvicorn      │
                    │  FastAPI Server  │
                    └─────────┬────────┘
                              │
                              ▼
                    ┌──────────────────┐
                    │   FastAPI App    │
                    └──────────────────┘
```

---

## 🔄 Deployment Flowchart

```
          ┌──────────────┐
          │   Developer   │
          └───────┬──────┘
                  │ git push
                  ▼
        ┌────────────────────┐
        │   EC2 Instance     │
        └─────────┬──────────┘
                  │ systemd starts app
                  ▼
        ┌────────────────────┐
        │   Uvicorn Server   │
        └─────────┬──────────┘
                  │ proxied through
                  ▼
        ┌────────────────────┐
        │       Nginx        │
        └─────────┬──────────┘
                  │ HTTPS via Certbot
                  ▼
        ┌────────────────────┐
        │     End Users      │
        └────────────────────┘
```

---

## 📡 API Endpoints

### **GET /**  
```json
{ "message": "API is running" }
```

### **GET /health**  
```json
{ "message": "healthy" }
```

### **GET /me**  
```json
{
  "name": "Henry Awoseyi",
  "email": "your-email@example.com",
  "github": "https://github.com/cyber-hen"
}
```

---

