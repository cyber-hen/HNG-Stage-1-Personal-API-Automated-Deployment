🚀 Personal API – Automated Deployment (HNG Stage 1)
https://img.shields.io/badge/Python-3.10+-blue
https://img.shields.io/badge/FastAPI-Framework-green
https://img.shields.io/badge/License-MIT-yellow
https://img.shields.io/badge/Build-Passing-brightgreen

A high‑performance Personal API built with FastAPI and deployed on an AWS EC2 instance.
This project demonstrates backend engineering and DevOps fundamentals, including Nginx reverse proxying, Systemd service management, and automated SSL/TLS with Certbot.

This repo now includes auto‑run support, so anyone can clone and run the API instantly.

🧰 Tech Stack
Layer	Technology
Language	Python 3.10+
Framework	FastAPI
Server	Uvicorn
Reverse Proxy	Nginx
Infrastructure	AWS EC2 (Ubuntu 24.04 LTS)
SSL/TLS	Certbot (Let’s Encrypt)
⚡ Quick Start (Auto‑Run Enabled)
Clone the repository:

bash
git clone https://github.com/cyber-hen/HNG-Stage-1-Personal-API-Automated-Deployment.git
cd HNG-Stage-1-Personal-API-Automated-Deployment
Run the API automatically:

bash
./run.sh
If needed:

bash
chmod +x run.sh
./run.sh
Your API will be available at:

Code
http://127.0.0.1:8000
🛠️ Auto‑Run Script (run.sh)
bash
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
📁 Project Structure
Code
HNG-Stage-1-Personal-API-Automated-Deployment/
│
├── main.py
├── run.sh
├── requirements.txt
├── README.md
│
└── venv/ (auto-created)
🧱 System Architecture Diagram
Code
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
                    │    Uvicorn       │
                    │  FastAPI Server  │
                    └─────────┬────────┘
                              │
                              ▼
                    ┌──────────────────┐
                    │   FastAPI App    │
                    └──────────────────┘
🔄 Deployment Flowchart
Code
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
📡 API Endpoints
GET /
json
{ "message": "API is running" }
GET /health
json
{ "message": "healthy" }
GET /me
json
{
  "name": "Henry Awoseyi",
  "email": "your-email@example.com",
  "github": "https://github.com/cyber-hen"
}
🤝 Contributing
Contributions are welcome!

Fork the repository

Create a new branch

Commit your changes

Open a pull request

Please ensure your code follows Python best practices and includes clear commit messages.
